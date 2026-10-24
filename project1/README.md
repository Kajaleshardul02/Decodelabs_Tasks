# DecodeLabs AI Internship
## Project 1: Rule-Based AI Chatbot

### 📌 Project Overview
DecodeBot is a simple rule-based AI chatbot developed using Python as part of the DecodeLabs AI Internship. It interacts with users through text input and generates responses based on predefined keywords and rules.

The chatbot can recognize greetings, respond to basic questions, provide help, acknowledge thanks, and handle goodbye messages. It uses Python's built-in `random` module to select responses from predefined options.

### 🎯 Objectives
- Understand the fundamentals of rule-based chatbots.
- Learn how keyword matching works in conversational AI.
- Implement predefined intents and responses using Python dictionaries.
- Handle user input and generate appropriate responses.
- Practice functions, loops, conditional statements, and exception handling.

### ✨ Features
- **Greeting Detection:** Responds to greetings such as "hello", "hi", and "hey".
- **Wellbeing Responses:** Answers questions such as "How are you?"
- **Bot Identity:** Introduces itself as DecodeBot.
- **Help Functionality:** Explains what the chatbot can do.
- **Thank You Responses:** Responds politely to expressions of gratitude.
- **Goodbye Detection:** Ends the conversation when the user types "bye", "exit", "quit", or "goodbye".
- **Randomized Responses:** Selects responses randomly from predefined options.
- **Input Normalization:** Converts input to lowercase and removes unnecessary whitespace.
- **Error Handling:** Handles certain input-related errors gracefully.

### 🛠️ Technologies Used
- **Programming Language:** Python 3
- **Module:** `random` (built-in Python module)
- **Concepts:** Functions, dictionaries, lists, loops, conditional statements, string manipulation, and exception handling.

No external libraries are required.

### 📂 Project Structure

```text
DecodeLabs-AI-Internship/
│
├── chatbot.py
└── README.md
```

### ⚙️ Installation and Setup

**Step 1: Install Python**

Download and install Python 3 from the official website:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

**Step 2: Download or Clone the Repository**

If the project is hosted on GitHub, run:

```bash
git clone <your-repository-url>
```

Navigate to the project folder:

```bash
cd DecodeLabs-AI-Internship
```

**Step 3: Run the Chatbot**

Execute the following command in your terminal:

```bash
python chatbot.py
```

If your system uses the `python3` command, run:

```bash
python3 chatbot.py
```

### 💬 Example Interaction

```text
=============================================
       DECODELABS RULE-BASED AI CHATBOT
=============================================
Type 'help' for assistance.
Type 'exit', 'quit', or 'bye' to stop.

You: hello
Bot: Hi there! Nice to meet you.

You: how are you
Bot: I'm doing well, thanks for asking!

You: what is your name
Bot: I'm DecodeBot, a simple rule-based AI chatbot.

You: help
Bot: I can respond to greetings, answer simple questions, and chat using predefined rules.

You: thank you
Bot: You're welcome!

You: bye
Bot: Goodbye! Have a great day!
```

*Note: Responses may vary because the chatbot randomly selects from available responses.*

### 🧠 How It Works

1. **Intent Definition:** The `INTENTS` dictionary stores keywords and predefined responses for different categories of user messages.
2. **Input Processing:** The `get_response()` function converts the user's message to lowercase and normalizes whitespace.
3. **Keyword Matching:** The chatbot checks whether any predefined keyword appears in the user's message.
4. **Response Selection:** The `random.choice()` function selects a response from the matching intent.
5. **Fallback Response:** If no keyword matches, the chatbot asks the user to type `help`.
6. **Conversation Loop:** The `main()` function repeatedly accepts input and displays responses until an exit command is entered.

### 🔍 Key Python Concepts

| Concept | Purpose |
|---|---|
| Dictionaries | Store intents, keywords, and responses |
| Lists | Hold multiple keywords and responses |
| Functions | Organize chatbot logic |
| `if-else` conditions | Handle decisions and fallback responses |
| `for` loops | Search for matching keywords |
| `random.choice()` | Select a response randomly |
| `try-except` | Handle certain input errors |
| `input()` and `print()` | Accept user messages and display replies |

### ⚠️ Limitations
- The chatbot does not understand the meaning or context of a sentence.
- It can respond only to predefined keywords and rules.
- It does not use machine learning or a large language model.
- Some keyword matches may produce incorrect responses when a keyword appears in an unrelated sentence.
- It does not remember previous conversations.

### 🚀 Future Improvements
- Add more intents and response categories.
- Improve keyword matching to reduce false matches.
- Implement a graphical user interface (GUI).
- Add conversation history and basic context management.
- Integrate natural language processing (NLP).
- Store chatbot conversations in a database.

### 📚 Learning Outcomes
Through this project, I learned how to build a basic conversational system using Python, organize predefined intents, process user input, implement keyword-based matching, and handle conversation flow.

### 👨‍💻 Project Information
- **Organization:** DecodeLabs
- **Internship:** Artificial Intelligence Internship
- **Project Number:** 1
- **Project Title:** Rule-Based AI Chatbot
- **Language:** Python

### 📄 License
This project is intended for educational and internship purposes. Add an appropriate open-source license if you plan to distribute the project publicly.

---

**Developed as part of the DecodeLabs AI Internship.**