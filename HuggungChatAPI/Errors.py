import traceback

class ErrorHandler:
    @staticmethod
    def handle_DefaultError(error):
        print("\033[91mERROR: {}\033[0m".format(error))
        #print("-" * len("ERROR: " + str(error)))
        traceback_str = ''.join(traceback.format_tb(error.__traceback__))
        print("\033[90m{}\033[0m\n".format(traceback_str))

    @staticmethod
    def handle_GoogleTransError(error=""):
        ERROR_TEXT = f"GoogleTransError: {error}"
        MESSAGE = "Probably you have the wrong googletrans version.\nTry to:"
        MESSAGE_HELP = "pip install --upgrade googletrans==4.0.0-rc1"
        print("\033[91m{}\033[0m".format(ERROR_TEXT))
        #print("-" * len(ERROR_TEXT))
        if isinstance(error, Exception):
            traceback_str = ''.join(traceback.format_tb(error.__traceback__))
            print("\033[90m{}\033[0m".format(traceback_str))
        print("\033[94m{}\033[0m\n{}\n".format(MESSAGE, MESSAGE_HELP))

    @staticmethod
    def handle_ResponseParseError(error="", response_content=""):
        ERROR_TEXT = f"ResponseParseError: {error}"
        MESSAGE = "Failed to parse the server response.\nIt seems that the response data is in an unexpected format or contains invalid information.\nPerhaps this version of the API is outdated, you can open an ISSUE on this topic\nso that developers can see the problem and update the API."
        MESSAGE_HELP = "GITHUB_LINK"
        print("\033[91m{}\033[0m".format(ERROR_TEXT))
        #print("-" * len(ERROR_TEXT))
        if response_content:
            print("\033[90m{}\033[0m".format(f"response_content={response_content}"))
        if isinstance(error, Exception):
            traceback_str = ''.join(traceback.format_tb(error.__traceback__))
            print("\033[90m{}\033[0m".format(traceback_str))
        print("\033[94m{}\033[0m\n{}\n".format(MESSAGE, MESSAGE_HELP))

    @staticmethod
    def handle_EmptyPromptError(error="'NoneType' object is not valid for prompt input."):
        ERROR_TEXT = f"EmptyPromptError: {error}"
        MESSAGE = "Prompt should NOT BE empty."
        MESSAGE_HELP = "GUTHUB_LINK_GUIDE"
        print("\033[91m{}\033[0m".format(ERROR_TEXT))
        #print("-" * len(ERROR_TEXT))
        if isinstance(error, Exception):
            traceback_str = ''.join(traceback.format_tb(error.__traceback__))
            print("\033[90m{}\033[0m".format(traceback_str))
        print("\033[94m{}\033[0m\n{}\n".format(MESSAGE, MESSAGE_HELP))

    @staticmethod
    def handle_WrongUserAgentError(error="Invalid UserAgent provided."):
        ERROR_TEXT = "WrongUserAgentError: {error}"
        MESSAGE = "The user agent string must be a valid HTTP user agent string following the standard format.\nPlease ensure that the user agent string provided is correct:"
        MESSAGE_HELP = "https://en.wikipedia.org/wiki/User-Agent_header"
        print("\033[91m{}\033[0m".format(ERROR_TEXT))
        #print("-" * len(ERROR_TEXT))
        if isinstance(error, Exception):
            traceback_str = ''.join(traceback.format_tb(error.__traceback__))
            print("\033[90m{}\033[0m".format(traceback_str))
        print("\033[94m{}\033[0m\n{}\n".format(MESSAGE, MESSAGE_HELP))

    @staticmethod
    def handle_WrongAuthDataError(error="Invalid data for 'conversation_id', 'additional_id' or 'hf_chat'"):
        ERROR_TEXT = f"WrongAuthDataError: {error}"
        MESSAGE = "Something went wrong while communicating with HuggingFace server.\nPlease check the name of the 'model' and the 'User Agent' if you specified it manually."
        MESSAGE_HELP = "GITHUB_LINK"
        print("\033[91m{}\033[0m".format(ERROR_TEXT))
        #print("-" * len(ERROR_TEXT))
        if isinstance(error, Exception):
            traceback_str = ''.join(traceback.format_tb(error.__traceback__))
            print("\033[90m{}\033[0m".format(traceback_str))
        print("\033[94m{}\033[0m\n{}\n".format(MESSAGE, MESSAGE_HELP))