import requests
import json
import warnings
import urllib3
from HuggingChatAPI.utils import highlight_code
from HuggingChatAPI.Errors import ErrorHandler
from HuggingChatAPI.Warnings import WarningsHandler

class SimpleHugChat:
    def __init__(self, model_name = 'mistralai/Mixtral-8x7B-Instruct-v0.1', debugMode=False, UserAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0") -> None:
        self.debugMode = debugMode
        self.model_name = model_name
        self.UserAgent = UserAgent
        self.prompt, self.conversation_id, self.additional_id, self.hf_chat = None, None, None, None #Default
        
        # Gettin self.conversation_id and self.hf_chat
        self.conversation_id, self.hf_chat = self.__get_conversation_id_and_cookie()    
        # Getting self.additional_id
        if self.conversation_id and self.hf_chat:
            self.additional_id = self.__get_additional_id()     
            # Sending request for browser traffic emulation only
            if self.additional_id:
                self.__send_api_event()

    def logger(function): #Logging decorator
        def wrapper(self, *args, **kwargs):
            # Сохраняем начальные значения переменных класса
            initial_state = self.__dict__.copy()

            output = function(self, *args, **kwargs)
    
            if self.debugMode:
                print(f"@Function: __{function.__name__}__: executed...")
                # Проверяем, изменились ли значения переменных класса после выполнения функции
                changed_variables = {}
                for key, value in self.__dict__.items():
                    if key not in initial_state or value != initial_state[key]:
                        changed_variables[key] = (initial_state.get(key), value)
                if changed_variables:
                    print("@Values changed:")
                    for var_name, (initial_value, final_value) in changed_variables.items():
                        print(f"    {var_name}: from [{initial_value}] to [{final_value}]")
                print("")
            return output
        return wrapper

    @logger
    def __get_conversation_id_and_cookie(self):
        headers = {
            'Host': 'huggingface.co',
            'User-Agent': self.UserAgent,
            'Accept': '*/*',
            'Referer': 'https://huggingface.co/chat/',
            'Content-Type': 'application/json',
            'Origin': 'https://huggingface.co',
            'Dnt': '1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        json_data = {
            'model': self.model_name,
        }

        # Suppress InsecureRequestWarning
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
            response = requests.post('https://huggingface.co/chat/conversation', headers=headers, json=json_data, verify=False)
        try:
            #return of self.conversation_id and self.hf_chat
            return response.json()["conversationId"], response.headers["set-cookie"].split(";")[0].replace("hf-chat=", "")
        
        except KeyError as error:
            #print(f"{response.status_code}") #Code 400 Bad Request if wrong model name
            if b'{"message":"Invalid request"}' in response.content and response.status_code == 400:
                WarningsHandler.handle_WrongModelNameWarning()
                ErrorHandler.handle_ResponseParseError(error=error, response_content=response.content)
            else:
                ErrorHandler.handle_DefaultError(error=error)
            return None, None

    @logger
    def __get_additional_id(self):
        cookies = {
            'hf-chat': self.hf_chat,
        }

        headers = {
            'Host': 'huggingface.co',
            'User-Agent': self.UserAgent,
            'Accept': '*/*',
            'Referer': 'https://huggingface.co/chat/',
            'Dnt': '1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        params = {
            'x-sveltekit-invalidated': '11',
        }

        # Suppress InsecureRequestWarning
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
            response = requests.get(
                f'https://huggingface.co/chat/conversation/{self.conversation_id}/__data.json',
                params=params,
                cookies=cookies,
                headers=headers,
                verify=False,
            )
        try:
            #return of self.additional_id
            return response.json()["nodes"][1]["data"][3]
        except KeyError as error:
            ErrorHandler.handle_ResponseParseError(error=error, response_content=response.content)
            #return None-value of self.additional_id
            return None

    @logger
    def __send_api_event(self): #For browser traffic emulation only
        cookies = {
            'hf-chat': self.hf_chat,
        }

        headers = {
            'Host': 'huggingface.co',
            'User-Agent': self.UserAgent,
            'Accept': '*/*',
            'Content-Type': 'text/plain',
            'Origin': 'https://huggingface.co',
            'Dnt': '1',
            'Referer': f'https://huggingface.co/chat/conversation/{self.conversation_id}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        data = '{"n":"pageview","u":"https://huggingface.co/chat/conversation/' + self.conversation_id + '","d":"huggingface.co","r":null}'

        
        
        try:
            # Suppress InsecureRequestWarning
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
                requests.post('https://huggingface.co/api/event', cookies=cookies, headers=headers, data=data, verify=False)
        except Exception as error:
            ErrorHandler.handle_DefaultError(error=error)

    @logger
    def send_prompt(self, prompt, highlight_result=False):
        self.prompt = prompt
        if self.hf_chat and self.UserAgent and self.conversation_id and self.additional_id and self.prompt:
            cookies = {
                'hf-chat': self.hf_chat,
            }
            headers = {
                'Host': 'huggingface.co',
                'User-Agent': self.UserAgent,
                'Accept': '*/*',
                'Referer': f'https://huggingface.co/chat/conversation/{self.conversation_id}',
                'Content-Type': 'application/json',
                'Origin': 'https://huggingface.co',
                'Dnt': '1',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
            }

            json_data = {
                'inputs': self.prompt,
                'id': self.additional_id,
                'is_retry': False,
                'is_continue': False,
                'web_search': False,
                'files': [],
            }

            # Suppress InsecureRequestWarning
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
                response = requests.post(
                    f'https://huggingface.co/chat/conversation/{self.conversation_id}',
                    cookies=cookies,
                    headers=headers,
                    json=json_data,
                    verify=False,
                    stream=True
                )
            
            try:
                data_list = response.content.decode().split("\n")
                for item in data_list:
                    if json.loads(item).get("type") == "finalAnswer":
                        if highlight_result:
                            return highlight_code(json.loads(item).get("type"))
                        else:
                            if json.loads(item).get("type")[0] == " ":
                                return json.loads(item).get("type")[1:]
                            else:
                                return json.loads(item).get("type")
                return None
            
            except AttributeError and json.JSONDecodeError as error:
                ErrorHandler.handle_ResponseParseError(error=error, response_content=response.content)
                return None
        
        else:
            if not self.prompt:
                ErrorHandler.handle_EmptyPromptError()
            if not self.UserAgent:
                ErrorHandler.handle_WrongUserAgentError()
            if not self.conversation_id or not self.additional_id or self.hf_chat:
                ErrorHandler.handle_WrongAuthDataError()
