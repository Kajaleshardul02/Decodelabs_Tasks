
"""
DecodeLabs AI Internship
Project 1: Rule-Based AI Chatbot
"""

import random


INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good afternoon"],
        "responses": [
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What would you like to know?"
        ]
    },
    "wellbeing": {
        "keywords": ["how are you", "how are you doing"],
        "responses": [
            "I'm doing well, thanks for asking!",
            "I'm great and ready to help you."
        ]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I'm DecodeBot, a simple rule-based AI chatbot."
        ]
    },
    "help": {
        "keywords": ["help", "what can you do"],
        "responses": [
            "I can respond to greetings, answer simple questions, "
            "and chat using predefined rules."
        ]
    },
    "thanks": {
        "keywords": ["thank you", "thanks"],
        "responses": [
            "You're welcome!",
            "Happy to help!"
        ]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "exit", "quit"],
        "responses": [
            "Goodbye! Have a great day!",
            "Thanks for chatting. See you soon!"
        ]
    }
}


def get_response(user_text):
    """Return a response based on predefined rules."""
    message = " ".join(user_text.lower().strip().split())

    if not message:
        return "Please type something so I can respond."

    # Check exit commands first.
    exit_words = {"bye", "goodbye", "exit", "quit"}
    if message in exit_words:
        return random.choice(INTENTS["goodbye"]["responses"])

    # Check known intents.
    for intent_name, intent_data in INTENTS.items():
        for keyword in intent_data["keywords"]:
            if keyword in message:
                return random.choice(intent_data["responses"])

    return (
        "I'm not sure how to answer that yet. "
        "Type 'help' to see what I can do."
    )


def main():
    print("=" * 45)
    print("       DECODELABS RULE-BASED AI CHATBOT")
    print("=" * 45)
    print("Type 'help' for assistance.")
    print("Type 'exit', 'quit', or 'bye' to stop.")
    print()

    while True:
        try:
            user_text = input("You: ").strip()

        except (EOFError, OSError):
            print(
                "\nThis console does not support interactive input.\n"
                "Please run chatbot.py in a terminal that accepts typing."
            )
            return

        if not user_text:
            print("Bot: Please enter a message.")
            continue

        response = get_response(user_text)
        print("Bot:", response)

        if user_text.lower().strip() in {"exit", "quit", "bye", "goodbye"}:
            break


if __name__ == "__main__":
    main()
