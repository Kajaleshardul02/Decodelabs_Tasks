# DecodeLabs AI Internship
## Project 3: AI Recommendation System

### 📌 Project Overview

The AI Recommendation System is a Python-based project that recommends relevant technical topics based on a user's interests. It uses **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity** to compare the user's interests with predefined topic descriptions and rank recommendations according to their similarity.

The system includes ten technical categories, such as Python Development, Artificial Intelligence, Data Science, Cybersecurity, Cloud Computing, and Web Development.

### 🎯 Objectives

- Understand the fundamentals of recommendation systems.
- Accept and process user interests.
- Convert text descriptions into numerical representations using TF-IDF.
- Calculate similarity between user interests and available topics.
- Rank recommendations based on cosine similarity scores.
- Display the top five recommendations to the user.

### ✨ Features

- **User Input:** Accepts at least three interests separated by commas.
- **Text Processing:** Converts text into numerical feature vectors.
- **TF-IDF Vectorization:** Identifies relevant words in the text.
- **Cosine Similarity:** Measures similarity between the user's interests and available topics.
- **Ranked Recommendations:** Displays the most similar topics first.
- **Similarity Scores:** Shows how closely each recommended topic matches the user's interests.
- **Input Validation:** Requests additional interests when fewer than three are entered.
- **Error Handling:** Handles certain situations where interactive keyboard input is unavailable.

### 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Machine Learning Library:** Scikit-learn
- **Techniques:** TF-IDF vectorization and cosine similarity
- **Python Concepts:** Dictionaries, lists, functions, loops, conditional statements, string manipulation, and exception handling.

### 📂 Project Structure

```text
DecodeLabs-AI-Internship/
│
├── ai_recommendation.py
└── README.md
```

### ⚙️ Installation and Setup

#### Step 1: Install Python

Download and install Python 3 from the official website:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

#### Step 2: Install the Required Library

Open your terminal or command prompt and execute:

```bash
pip install scikit-learn
```

#### Step 3: Navigate to the Project Folder

```bash
cd DecodeLabs-AI-Internship
```

#### Step 4: Run the Project

Execute the following command:

```bash
python ai_recommendation.py
```

If your Python file has a different name, replace `ai_recommendation.py` with your actual filename.

### 🧠 Available Recommendation Categories

The system contains the following ten predefined technical topics:

| No. | Category | Example Keywords |
|---:|---|---|
| 1 | Python Development | Python, programming, coding |
| 2 | AI and Machine Learning | Artificial intelligence, ML, deep learning |
| 3 | Web Development | HTML, CSS, JavaScript |
| 4 | Data Science | Data analysis, statistics, visualization |
| 5 | Cybersecurity | Network security, ethical hacking, encryption |
| 6 | Cloud Computing | AWS, Azure, deployment |
| 7 | Automation and Robotics | Robotics, sensors, control systems |
| 8 | Mobile App Development | Android, iOS, applications |
| 9 | Computer Vision | Image processing, object detection |
| 10 | Database Management | SQL, databases, queries |

### 🔍 How the Recommendation System Works

1. **Collect User Interests:** The program asks the user to enter at least three interests separated by commas.
2. **Prepare the Text:** The interests are combined into a single user profile.
3. **Apply TF-IDF:** `TfidfVectorizer` converts the topic descriptions and user profile into numerical vectors, while ignoring common English stop words.
4. **Calculate Similarity:** `cosine_similarity()` compares the user profile with each topic description.
5. **Rank Results:** Recommendations are sorted from the highest similarity score to the lowest.
6. **Display Recommendations:** The program prints the top five topics with their similarity percentages.

### 💻 Example Interaction

```text
=======================================================
             AI RECOMMENDATION SYSTEM
=======================================================
This system recommends topics based on your interests.
Example interests: Python, AI, automation

Enter at least three interests, separated by commas: Python, AI, automation

Your interests: Python, AI, automation

Top recommendations
-------------------------------------------------------
1. Automation and Robotics (similarity: ...)
2. AI and Machine Learning (similarity: ...)
3. Python Development (similarity: ...)
4. Data Science (similarity: ...)
5. Computer Vision (similarity: ...)

Recommendation process completed.
```

*Note: The similarity percentages and exact ranking depend on the text processed by the program. The ellipses above represent values calculated when the code runs.*

### 📚 Key Concepts Explained

**1. TF-IDF (Term Frequency–Inverse Document Frequency)**

TF-IDF converts text into numerical values based on the importance of words within a document relative to the collection of documents. It helps the system compare technical topic descriptions with the user's interests.

**2. Cosine Similarity**

Cosine similarity measures the angle-based similarity between two numerical vectors. A higher score indicates greater similarity between the user's interest profile and a topic description.

**3. Content-Based Recommendation**

This project follows a content-based recommendation approach. It recommends topics by comparing their descriptions with the user's stated interests instead of relying on other users' preferences or ratings.

**4. Ranking**

The system sorts the similarity scores in descending order and returns up to five recommendations.

### ⚠️ Limitations

- The system recommends only from ten predefined categories.
- Recommendations depend on the keywords used in the topic descriptions.
- It does not learn from user feedback or past interactions.
- It does not use a trained deep learning model or a generative AI model.
- Unrelated or unfamiliar input may result in low similarity scores or tied rankings.
- Similarity scores represent text similarity, not the probability that a user will like a recommendation.

### 🚀 Future Improvements

- Expand the dataset with more technical topics and courses.
- Add a graphical user interface (GUI).
- Allow users to rate recommendations and provide feedback.
- Store user preferences and recommendation history.
- Integrate course information from external datasets or APIs.
- Improve text processing using natural language processing (NLP).
- Personalize recommendations using user activity and preferences.

### 📈 Learning Outcomes

Through this project, I learned how to build a basic content-based recommendation system using Python and Scikit-learn. I gained practical experience with text vectorization, cosine similarity, ranking algorithms, user input validation, and recommendation generation.

### 👨‍💻 Project Information

- **Organization:** DecodeLabs
- **Internship:** Artificial Intelligence Internship
- **Project Number:** 3
- **Project Title:** AI Recommendation System
- **Programming Language:** Python
- **Library:** Scikit-learn
- **Core Techniques:** TF-IDF and Cosine Similarity

### 📄 License

This project is intended for educational and internship purposes. Add an appropriate open-source license if you plan to distribute the project publicly.

---

**Developed as part of the DecodeLabs AI Internship.**