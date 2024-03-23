from HuggingChatAPI import SimpleHugChat
from HuggingChatAPI.utils import translate_text

MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"
ChatBot = SimpleHugChat(model_name=MODEL_NAME)

prompt = "Напиши код на Python, который будет считать квадрат числа, введённого пользователем."
#You can use HuggingChat.utils.translate_text to translate your prompt, if you want
#But AI models can understand many languages, so it's not neccessary.
translated_text = translate_text(prompt, source_lang="ru", dest_lang="en")
print(f"{translated_text=}")

ai_answer = ChatBot.send_prompt(prompt, highlight_result=True)
print(ai_answer)