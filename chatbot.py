# CodeAlpha Internship - Task 4
# Basic Chatbot

def chatbot():
    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)
    print("Hello! I am your chatbot.")
    print("You can talk to me. Type 'bye' to exit.")
    print("-" * 40)

    while True:
        user = input("You: ").lower().strip()

        if user == "hello" or user == "hi":
            print("Bot: Hi! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Python chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "thank you" or user == "thanks":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

        print("-" * 40)


chatbot()