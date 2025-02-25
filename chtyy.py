def simple_chatbot():
    responses = {
        "hello": "Hi there! How can I assist you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "your name": "I'm a chatbot created in Python!",
        "bye": "Goodbye! Have a great day!"
    }

    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
        elif user_input == "exit":
            print("Bot: Exiting... Have a good day!")
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

simple_chatbot()
