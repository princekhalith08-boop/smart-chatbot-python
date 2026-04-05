import random
import datetime

print("Chatbot: Hello! Ask me anything. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        print("Chatbot:", random.choice(["Hello!", "Hi there!", "Hey!"]))

    
    elif "how are you" in user_input:
        print("Chatbot: I'm doing great! Thanks for asking")

    
    elif "your name" in user_input or "who are you" in user_input:
        print("Chatbot: I'm your personal Python chatbot")

    
    elif "college" in user_input:
        print("Chatbot: You study at KCG College of Technology, right?")

    
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Chatbot: Current time is", current_time)

    
    elif "date" in user_input or "day" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Chatbot: Today's date is", current_date)

    
    elif "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Have a nice day")
        break

    
    else:
        print("Chatbot: Sorry, I didn't understand that. Try asking something else!")
