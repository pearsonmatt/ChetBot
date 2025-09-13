"""
chatbot.py

A simple command-line chatbot that responds to user 
input using keyword matching.
"""

#imports Python’s built-in random module, which provides 
#functions for generating random numbers and making 
#random choices 
import random


#var responses = {key: [options],....} →acts as response pool
responses = {
    "hello": ["Hello there!", "Greetings!", "Hey! How can I help you?"],
    "name": ["I was once a man named Chet, you can call be ChetBot.", "My name is ChetBot, you can call me Chet for short.", "My frieds call me Chet, but you can call me ChetBot.", "Chet.", "ChetBot"],
    "how are you": ["I'm just a program, but I'm doing well!", "All systems go!"],
    "weather": ["I can't check the weather yet, but I hope it's nice where you are!", "I'm just glad to have a heatsink with how bad summer was."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
}

#defines get_response() function. Takes user_input from main(), uses lower() to 
#prevent issues causes by capitalization, var matched_responses created
#as a blank array, which is then filled by for statement with responses
#and .append - if array not blank, joins responses. 
def get_response(user_input):
    user_input = user_input.lower()
    matched_responses = []
    for key in responses:
        if key in user_input:
            matched_responses.append(random.choice(responses[key]))
    if matched_responses:
        # Join all matched responses into a single reply
        return " ".join(matched_responses)
    return "Sorry, I don't understand that yet."

#Obtains input with input() and sets user name var. 
#while loop displays name in prompt for response and if bye/exit chosen
#then it breaks loop (essentially ending script). Otherwise, it calls
#the get_response() function. 
def main():
    print("Hello! I'm your chatbot, Chet. ChetBot, if you will. What's your name?")
    name = input("You: ")
    print(f"Nice to meet you, {name}!")
    print("You can ask me simple questions, or type 'bye' to exit.")

    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() in ["bye", "exit"]:
            print("ChetBot: " + random.choice(responses["bye"]))
            break
        response = get_response(user_input)
        print("ChetBot: " + response)

#Is it safe to say that I can put this at the end of every program 
#I create and it will 1) not hurt anything and 2) give it the ability 
#to be a module without running automatically?
#→Considered a best practice for making Python files flexible—
#as both standalone programs and importable modules!
if __name__ == "__main__":
    main()