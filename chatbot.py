
from knowledge_base import knowledge
from utils import find_match

class ChatBot:
    def __init__(self, name="Bot"):
        self.name = name

    def get_response(self, user_input):
        return find_match(user_input, knowledge)
