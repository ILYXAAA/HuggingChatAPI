<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://github.com/ILYXAAA/HuggingChatAPI/assets/107761814/6fa4af01-5719-4903-a2c3-f8b552ccf550" alt="Project logo"></a>
</p>

<h3 align="center">HuggingChatAPI</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![GitHub last commit](https://img.shields.io/github/last-commit/ILYXAAA/HuggingChatAPI)
![GitHub Issues](https://img.shields.io/github/issues/ILYXAAA/HuggingChatAPI)

</div>

---

> The project is an unofficial API for the site https://huggingface.co/chat  which allows you to quickly, without a UI interface, get answers to your questions using AI hosted by huggingface.

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Parameters](#parameters)
- [Avaible models](#aviable_models)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

The project is an unofficial API for the site https://huggingface.co/chat  was created using reverse engineering and site traffic analysis using BurpSuite. The developed library can be used in your projects if you need to add text-AI to your project very quickly and easily

## 🏁 Getting Started <a name = "getting_started"></a>




### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/ILYXAAA/HuggingChatAPI.git
    ```


2. Install the necessary libraries:

    ```bash
    pip install -r requirements.txt
    ```

#### Or you can install the library as a package via pip

  ```bash
  pip install HuggingChatAPI
  ```

## 🎈 Usage <a name="usage"></a>

#### To use the library, just write a couple of lines of code.
```python
from HuggingChatAPI import SimpleHugChat

#Initializing the SimpleHugChat class
ChatBot = SimpleHugChat()

#Use the send_prompt function to send our message to the AI model
prompt = "Hello, how are you?"
model_answer = ChatBot.send_prompt(prompt)

print(model_answer)
```

#### If you run this script, you will get an example like this:

```markdown
> python client.py
I am just a computer program, so I dont have feelings,
but I am here to help answer your questions to the best of my ability.
How can I assist you today?

If you need any assistance or have any queries related to programming,
data science, machine learning, mathematics, or any other topic, feel free to ask!
```

## :computer: Parameters <a name = "parameters"></a>
WORK IN PROGRESS

## :bulb: Aviable models <a name = "aviable_models"></a>

| AI model                         | Name                                           | Description                                                                                                                                     |Supporting         |
| :--------                        | :-------                                       |:----------------                                                                                                                                |:---------------   |
| `Mixtral-8x7B `                  | `mistralai/Mixtral-8x7B-Instruct-v0.1`         |The latest MoE model from Mistral AI! 8x7B and outperforms Llama 2 70B in most benchmarks.                                                       |:white_check_mark: |
| `gemma-7b-it`                    | `google/gemma-7b-it`                           |Gemma 7B belongs to a family of lightweight models built by Google, based on the same research and technology used to create the Gemini models.  |:white_check_mark: |
| `Llama-2-70b`                    | `meta-llama/Llama-2-70b-chat-hf`               |The latest and biggest model from Meta, fine-tuned for chat..                                                                                    |:white_check_mark: |
| `Nous-Hermes-2-Mixtral`          | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`  |Nous Hermes 2 Mixtral 8x7B DPO is the new flagship Nous Research model trained over the Mixtral 8x7B MoE LLM.                                    |:white_check_mark: |
| `CodeLlama-70b`                  | `codellama/CodeLlama-70b-Instruct-hf`          |Code Llama, a state of the art code model from Meta. Now in 70B!                                                                                 |:white_check_mark: |
| `Mistral-7B-Instruct`            | `mistralai/Mistral-7B-Instruct-v0.2`           |Mistral 7B is a new Apache 2.0 model, released by Mistral AI that outperforms Llama2 13B in benchmarks.                                          |:white_check_mark: |
| `openchat-3.5`                   | `openchat/openchat-3.5-0106`                   |OpenChat 3.5 is the #1 model on MT-Bench, with only 7B parameters.                                                                               |:white_check_mark: |




## ⛏️ Built Using <a name = "built_using"></a>

- [HuggingFace Chat](https://huggingface.co/chat/) - A website hosting all the specified models
- [BurpSuite](https://portswigger.net/burp) - A utility for analyzing network traffic
- [Python](https://www.python.org/) - The main language of the project

## ✍️ Author <a name = "authors"></a>
[@ILYXAAA](https://github.com/ILYXAAA)
