def chatbot():
    """
    A simple rule-based chatbot that interacts with the user and responds to specific inputs.
    """
    # Greet the user at the start of the conversation
    print("Chatbot: Hello! How can I help you today?")
    
    # Start an infinite loop to keep the chatbot running until the user decides to exit
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Normalize user input to lowercase for easier matching
        normalized_input = user_input.lower()
        
        # Exit condition: if the user types 'exit' or 'quit'
        if normalized_input in ['exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop and end the conversation
        
        # Respond to the user's inquiry about the chatbot's name
        elif 'your name' in normalized_input:
            print("Chatbot: I'm a chatbot created to assist you. You can call me Chatbot!")
        
        # Respond to requests for help
        elif 'help' in normalized_input:
            print("Chatbot: Sure! What do you need help with?")
        
        # Respond to inquiries about the chatbot's abilities
        elif 'what can you do' in normalized_input:
            print("Chatbot: I can assist you with various queries, provide information, and chat with you!")
        
        # Respond to greetings from the user
        elif any(greet in normalized_input for greet in ['hi', 'hello', 'hey']):
            print("Chatbot: Hello! How can I assist you today?")
        
        # Respond to common farewells
        elif any(farewell in normalized_input for farewell in ['bye', 'goodbye', 'see you']):
            print("Chatbot: Goodbye! Feel free to return if you have more questions.")
            break  # Exit the loop
        
        # Default response for unrecognized inputs
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you please rephrase?")
            print("Chatbot: You can ask me about my name, what I can do, or simply say 'help'.")

# Call the chatbot function to start the interaction
chatbot()
