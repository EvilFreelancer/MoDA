import logging


class Conversation:
    def __init__(self, functions, history_limit=4):
        self.logger = logging.getLogger('Conversation')

        self.functions = functions
        self.history_limit = history_limit

        self.system_prompt = \
            f"You are a helpful assistant with access to the following functions: \n " \
            f"{str(functions)}\n\n" \
            f"To use these functions respond with:\n" \
            f"<functioncall> {{\"name\": \"function_name\"}} </functioncall>\n\n" \
            f"Edge cases you must handle:\n" \
            f" - If there are no functions that match the user request, you will respond politely that you cannot help."

        self.messages = [{"role": "system", "content": self.system_prompt}]

    def add_message(self, role, message):
        self.messages.append({
            "role": role,
            "content": message
        })
        self.trim_history()

    def add_user_message(self, message):
        self.add_message("user", message)

    def add_bot_message(self, message):
        self.add_message("assistant", message)

    def trim_history(self):
        if self.history_limit is not None and len(self.messages) > self.history_limit + 1:
            overflow = len(self.messages) - (self.history_limit + 1)
            self.messages = [self.messages[0]] + self.messages[overflow + 1:]  # remove old messages except system

    def get_last_message(self, role: str = "user"):
        for message in reversed(self.messages):
            if message["role"] == role:
                return message["content"]
        return None
