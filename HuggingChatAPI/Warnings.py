class WarningsHandler:
    @staticmethod
    def handle_WrongModelNameWarning(some_warning_text=""):
        WARNING_TEXT = f"WrongModelNameWarning: 'model_name' should be valid. {some_warning_text}"
        MESSAGE = "Perhaps you have specified the wrong name/version of the model.\nSo script can not parse coversation_id.\nCheck the names of the available models:"
        MESSAGE_HELP = "https://huggingface.co/spaces/huggingchat/chat-ui"
        print("\033[93m{}\033[0m".format(WARNING_TEXT))
        #print("-" * len(WARNING_TEXT))
        print("\033[94m{}\033[0m\n{}\n".format(MESSAGE, MESSAGE_HELP))
