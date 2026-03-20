#password checker

import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include numbers")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    # Strength result
    if score <= 2:
        strength = "Weak ❌"
    elif score == 3 or score == 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    return strength, suggestions


# Main program
password = input("Enter your password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("Suggestions to improve:")
    for s in suggestions:
        print("-", s)
else:
    print("Your password is secure!")

#chatbot
import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "name": ["I am your chatbot!", "You can call me Python Bot."],
}

# Default responses if no match
default_responses = [
    "I don't understand that.",
    "Can you say that again?",
    "Interesting... tell me more!",
]

# Chat function
def chatbot():
    print("🤖 Chatbot: Hello! Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("🤖 Chatbot: Goodbye!")
            break
        
        found = False
        
        for key in responses:
            if key in user_input:
                print("🤖 Chatbot:", random.choice(responses[key]))
                found = True
                break
        
        if not found:
            print("🤖 Chatbot:", random.choice(default_responses))

# Run chatbot
chatbot()