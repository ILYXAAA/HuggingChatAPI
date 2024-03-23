from googletrans import Translator #pip install --upgrade googletrans==4.0.0-rc1
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
from HuggingChatAPI.Errors import ErrorHandler

def highlight_code(text):
    if text[0] == " ":
        text = text[1:]
    # Разделение текста и кода
    parts = text.split("```")
    formatted_text = ""
    for i, part in enumerate(parts):
        # Если четное, это текст, если нечетное - код
        if i % 2 == 0:
            formatted_text += part
        else:
            # Разбиваем строку кода на язык и код
            lang, code = part.split('\n', 1)
            # Удаляем начальные пробелы и символы новой строки
            lang = lang.strip()
            try:
                # Пытаемся получить лексер для указанного языка
                lexer = get_lexer_by_name(lang)
            except ValueError:
                # Если указанный язык не поддерживается, используем текстовый лексер
                lexer = get_lexer_by_name('text')
            # Подсветка кода с помощью Pygments
            highlighted_code = highlight(code, lexer, TerminalFormatter())
            # Добавляем ANSI escape sequence для красного цвета перед языком
            formatted_text += f'\033[31m{lang}\033[0m\n' + highlighted_code
    return formatted_text

def translate_text(text, source_lang='ru', dest_lang='en'):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=dest_lang)
        return translated_text.text
    
    except AttributeError as error:
        if "NoneType' object has no attribute 'group'" in str(error):
            ErrorHandler.handle_GoogleTransError(error)
        else:
            ErrorHandler.handle_DefaultError(error)
        return None
    
