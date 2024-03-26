<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://github.com/ILYXAAA/HuggingChatAPI/assets/107761814/6fa4af01-5719-4903-a2c3-f8b552ccf550" alt="Project logo"></a>
</p>

<h3 align="center">HuggingChatAPI</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![PyPi](https://img.shields.io/pypi/v/HuggingChatAPI.svg?logo=pypi&logoColor=white)](https://pypi.org/project/HuggingChatAPI/)
![GitHub last commit](https://img.shields.io/github/last-commit/ILYXAAA/HuggingChatAPI)
![GitHub Issues](https://img.shields.io/github/issues/ILYXAAA/HuggingChatAPI)

</div>

---

> The project is an unofficial API for the site https://huggingface.co/chat  which allows you to quickly, without a UI interface, get answers to your questions using AI hosted by huggingface.

## 📝 Table of Contents

- 🧐[**About**](#about)
- 🏁[**Getting Started**](#getting_started)
- 🎈[**Usage**](#usage)
- :computer:[**Features**](#features)
  - :wrench:[Parameters](#parameters)
  - 🌐[Translator](#translator)
- :bulb:[**Avaible models**](#aviable_models)
- ⛏️[**Built Using**](#built_using)
- ✍️[**Authors**](#authors)

&emsp;
## 🧐 About <a name = "about"></a>

The project is an unofficial API for the site https://huggingface.co/chat  was created using reverse engineering and site traffic analysis using BurpSuite. The developed library can be used in your projects if you need to add text-AI to your project very quickly and easily

&emsp;
## 🏁 Getting Started <a name = "getting_started"></a>

### You can install the library as a package via pip

  ```bash
  pip install HuggingChatAPI
  ```
### Or use the library by installing it using git

1. Clone the repository:

    ```bash
    git clone https://github.com/ILYXAAA/HuggingChatAPI.git
    ```

2. Install the necessary libraries:

    ```bash
    pip install -r requirements.txt
    ```

&emsp;
## 🎈 Usage <a name="usage"></a>

### To use the library, just write a couple lines of code.
```python
from HuggingChatAPI import SimpleHugChat

#Initializing the SimpleHugChat class
ChatBot = SimpleHugChat()

#Use the send_prompt function to send our message to the AI model
prompt = "Hello, how are you?"
model_answer = ChatBot.send_prompt(prompt)

print(model_answer)
```

### If you run this script, you will get an example like this:

```bash
> python client.py
I am just a computer program, so I dont have feelings.

If you need any assistance or have any queries related to programming,
data science, machine learning, mathematics, or any other topic, feel free to ask.
```

&emsp;
## :computer: Features <a name = "features"></a>
### :wrench: Parameter <a name = "parameters"></a>
### You can specify parameters such as:
- **`model_name`**
  > The string value of the model name. The **Mixtral** model is selected by default. Full name: `mistralai/Mixtral-8x7B-Instruct-v0.1`. For a list of available AI models, see **"Aviable models"**.

- **`UserAgent`**
  > You can set the desired User Agent. By default, `"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"` is installed. More details: [Wikipedia](https://en.wikipedia.org/wiki/User-Agent_header)

- **`debugMode`**
  > By default, the value is set to `False`. You can set the value to `True` if you want to track information about the execution of functions in detail

- **`highlight_result`**
  > Set to `False` by default. You can set it to `True` if you want the program code to be highlighted in the response of the AI model.
    
### Example of using parameters:
```python
from HuggingChatAPI import SimpleHugChat
from HuggingChatAPI.utils import translate_text

model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
ChatBot = SimpleHugChat(model_name=model, UserAgent=user_agent, debugMode=False)

prompt = "Hello, create a C++ script that displays 'Hello, world!' if the user has entered the word 'Hello'"
ai_answer = ChatBot.send_prompt(prompt, highlight_result=True)
print(ai_answer)
```
### The result of executing the code in the console:
<img src="https://github.com/ILYXAAA/HuggingChatAPI/assets/107761814/b5e3c012-9772-4b39-bc39-62d15fd76a8f" alt="image" style="width:566px;height:auto;">

### 🌐 Translator <a name = "translator"></a>
### All models support a large number of languages. If your native language is not **English** and you want to improve the accuracy of answers to your questions, it is **recommended** to translate your prompts into **English**.
> You can do this by importing the `translate_text` function from the `HuggingChatAPI.utils` module.
> You can translate any phrase by specifying `source_lang` and `dest_lang` in the function parameters
```python
from HuggingChatAPI.utils import translate_text
  
prompt = "Привет друзья! Миру - мир"
translated_text = translate_text(prompt, source_lang="ru", dest_lang="en")
print(f"{translated_text=}")
```

Console output:
```bash
> translated_text='Hello friends!The world is the world'
```

&emsp;
## :bulb: Aviable models <a name = "aviable_models"></a>

| AI model                         | Name                                           | Description                                                                                                                                     |Supporting         |
| :--------                        | :-------                                       |:----------------                                                                                                                                |:---------------   |
| `Mixtral-8x7B`                   | `mistralai/Mixtral-8x7B-Instruct-v0.1`         |The latest MoE model from Mistral AI! 8x7B and outperforms Llama 2 70B in most benchmarks.                                                       |:white_check_mark: |
| `gemma-7b-it`                    | `google/gemma-7b-it`                           |Gemma 7B belongs to a family of lightweight models built by Google, based on the same research and technology used to create the Gemini models.  |:white_check_mark: |
| `Llama-2-70b`                    | `meta-llama/Llama-2-70b-chat-hf`               |The latest and biggest model from Meta, fine-tuned for chat..                                                                                    |:white_check_mark: |
| `Nous-Hermes-2-Mixtral`          | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`  |Nous Hermes 2 Mixtral 8x7B DPO is the new flagship Nous Research model trained over the Mixtral 8x7B MoE LLM.                                    |:white_check_mark: |
| `CodeLlama-70b`                  | `codellama/CodeLlama-70b-Instruct-hf`          |Code Llama, a state of the art code model from Meta. Now in 70B!                                                                                 |:white_check_mark: |
| `Mistral-7B-Instruct`            | `mistralai/Mistral-7B-Instruct-v0.2`           |Mistral 7B is a new Apache 2.0 model, released by Mistral AI that outperforms Llama2 13B in benchmarks.                                          |:white_check_mark: |
| `openchat-3.5`                   | `openchat/openchat-3.5-0106`                   |OpenChat 3.5 is the #1 model on MT-Bench, with only 7B parameters.                                                                               |:white_check_mark: |


&emsp;
## ⛏️ Built Using <a name = "built_using"></a>

- [HuggingFace Chat](https://huggingface.co/chat/) - A website hosting all the specified models
- [BurpSuite](https://portswigger.net/burp) - A utility for analyzing network traffic
- [Python](https://www.python.org/) - The main language of the project

## ✍️ Author <a name = "authors"></a>
[@ILYXAAA](https://github.com/ILYXAAA)
