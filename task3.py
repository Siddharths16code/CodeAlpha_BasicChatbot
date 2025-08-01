def smart_chatbot():
    print("🤖 Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I assist you today?")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm fine, thank you! How about you?")
        
        elif "what is your name" in user_input or "who are you" in user_input:
            print("🤖 Chatbot: I am PyBot, your simple chatbot friend.")
        
        elif "what can you do" in user_input:
            print("🤖 Chatbot: I can chat with you, answer basic questions, and make your day better!")
        
        elif "tell me a joke" in user_input:
            print("🤖 Chatbot: Why did the computer catch a cold? Because it had too many windows open!")
        
        elif "thank you" in user_input or "thanks" in user_input:
            print("🤖 Chatbot: You're welcome! 😊")
        
        elif "who created you" in user_input:
            print("🤖 Chatbot: I was created by a Python programmer as part of a learning project.")
        
        elif "which language you use" in user_input or "programming language" in user_input:
            print("🤖 Chatbot: I am written in Python programming language.")
        
        elif "good morning" in user_input:
            print("🤖 Chatbot: Good morning! Have a great day ahead.")
        
        elif "good night" in user_input:
            print("🤖 Chatbot: Good night! Sleep well.")
        
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Take care! 😊")
            break
        
        else:
            print("🤖 Chatbot: I'm still learning! Please try asking something simple.")

# Run the chatbot
smart_chatbot()

        
        