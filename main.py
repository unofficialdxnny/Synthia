# Define a list of predefined questions and answers
questions = ["What is your name?", "How are you?", "What is the meaning of life?", "Where are you from?", "What is your favorite color?"]
answers = ["My name is AI Bot.", "I'm good, thank you!", "The meaning of life is 42.", "I am an AI bot and do not have a physical location.", "I don't have a favorite color as I am an AI bot."]

# Function to find an appropriate answer based on user input
def get_answer(question):
    # Convert the user's question to lowercase
    question = question.lower()
    
    # Check if the user's question matches any predefined question
    for i, q in enumerate(questions):
        if q.lower() in question:
            return answers[i]
    
    # If no match is found, return a default response
    return "I'm sorry, I don't understand that question."

# Main conversation loop
print("AI Bot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    response = get_answer(user_input)
    print("Synthia:", response)
