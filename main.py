#

from chatbot import ChatBot

def main():
    bot = ChatBot("HelperBot")
    print("🤖 Welcome to HelperBot! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye! 👋")
            break
        response = bot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
