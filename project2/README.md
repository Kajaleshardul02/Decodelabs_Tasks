# DecodeLabs AI Internship
## Project 2: Data Classification Using AI

### 📌 Project Overview

This project demonstrates how Artificial Intelligence and machine learning can be used to classify data using the **K-Nearest Neighbors (KNN)** algorithm.

The project uses the Iris dataset, which contains measurements of iris flowers belonging to three different species. A KNN classification model is trained on the dataset to predict the species of a flower based on its measurements.

The model's performance is evaluated using accuracy, a confusion matrix, a classification report, and the weighted F1 score.

### 🎯 Objectives

- Load and understand a dataset.
- Split the dataset into training and testing sets.
- Apply the K-Nearest Neighbors (KNN) classification algorithm.
- Scale features using StandardScaler.
- Train the machine learning model and make predictions.
- Evaluate model performance using a confusion matrix and F1 score.
- Predict the species of a new flower using its measurements.

### ✨ Features

- **Dataset Loading:** Loads the Iris dataset from Scikit-learn.
- **Dataset Exploration:** Displays the number of samples, feature names, and target classes.
- **Data Splitting:** Divides the data into training and testing sets using an 80:20 ratio.
- **Feature Scaling:** Standardizes features to improve distance-based classification.
- **KNN Classification:** Uses five nearest neighbors to classify flowers.
- **Model Evaluation:** Calculates accuracy, weighted F1 score, confusion matrix, and classification report.
- **New Flower Prediction:** Predicts a flower species from manually entered measurements.

### 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Machine Learning Library:** Scikit-learn
- **Dataset:** Iris dataset
- **Algorithms and Techniques:** K-Nearest Neighbors (KNN), feature scaling, train-test splitting, and model evaluation.

### 📂 Project Structure

```text
DecodeLabs-AI-Internship/
│
├── data_classification.py
└── README.md
```

### ⚙️ Installation and Setup

#### Step 1: Install Python

Download Python 3 from the official website:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

#### Step 2: Install Required Library

Open your terminal or command prompt and execute:

```bash
pip install scikit-learn
```

#### Step 3: Navigate to the Project Folder

Open the folder containing your Python file in the terminal.

For example:

```bash
cd DecodeLabs-AI-Internship
```

#### Step 4: Run the Project

Execute the following command:

```bash
python data_classification.py
```

If your Python file has a different name, replace `data_classification.py` with the actual filename.

### 🧠 Dataset Information

The project uses the built-in Iris dataset provided by Scikit-learn.

| Property | Description |
|---|---|
| Total samples | 150 |
| Total features | 4 |
| Number of classes | 3 |
| Training samples | 120 |
| Testing samples | 30 |
| Train-test ratio | 80:20 |

**Input features:**
- Sepal length
- Sepal width
- Petal length
- Petal width

**Target classes:**
- Iris setosa
- Iris versicolor
- Iris virginica

### 🔍 How the Project Works

1. **Load the Dataset:** The `load_iris()` function loads the flower measurements and their corresponding species labels.
2. **Understand the Data:** The program displays dataset dimensions, feature names, and target classes.
3. **Split the Data:** The `train_test_split()` function divides the dataset into training and testing sets. Stratification helps preserve the class proportions in both sets.
4. **Scale the Features:** `StandardScaler` standardizes the input features. It is fitted only on the training data to prevent data leakage.
5. **Train the Model:** `KNeighborsClassifier(n_neighbors=5)` creates a classifier that uses the five nearest training samples.
6. **Make Predictions:** The trained model predicts the species labels for the test data.
7. **Evaluate the Model:** The program calculates accuracy, weighted F1 score, confusion matrix, and classification report.
8. **Predict a New Flower:** The model predicts the species for a flower with measurements `[5.1, 3.5, 1.4, 0.2]`.

### 📊 Model Evaluation Metrics

| Metric | Purpose |
|---|---|
| Accuracy | Measures the proportion of correct predictions |
| Confusion Matrix | Shows correct and incorrect predictions for each class |
| Precision | Measures how many predicted instances of a class are correct |
| Recall | Measures how many actual instances of a class are correctly identified |
| F1 Score | Combines precision and recall into a single metric |
| Weighted F1 Score | Calculates the F1 score while accounting for the number of samples in each class |

### 💻 Expected Output

The program displays information similar to the following:

```text
=======================================================
       DATA CLASSIFICATION USING AI
=======================================================

Dataset Information
Number of samples: 150
Number of features: 4
Feature names: ['sepal length (cm)', 'sepal width (cm)',
                'petal length (cm)', 'petal width (cm)']
Target classes: ['setosa' 'versicolor' 'virginica']

Training samples: 120
Testing samples: 30

Model Evaluation
----------------------------------------
Accuracy: [calculated accuracy]
Weighted F1 Score: [calculated F1 score]

Confusion Matrix:
[calculated confusion matrix]

Classification Report:
[precision, recall, f1-score, and support]

New Flower Prediction
Measurements: [5.1, 3.5, 1.4, 0.2]
Predicted species: setosa
```

*Note: The evaluation values are calculated when the program runs. The example uses placeholders for the metrics rather than claiming specific results.*

### 🚀 Future Improvements

- Test different values of K to find the best model configuration.
- Compare KNN with other classification algorithms.
- Add data visualization to understand feature relationships.
- Create a graphical user interface for entering flower measurements.
- Save the trained model for future predictions.
- Use additional datasets to test the model on different classification tasks.

### 📚 Learning Outcomes

Through this project, I learned how to load and explore a dataset, preprocess features, split data for training and testing, implement the KNN classification algorithm, make predictions, and evaluate machine learning performance using standard classification metrics.

### 👨‍💻 Project Information

- **Organization:** DecodeLabs
- **Internship:** Artificial Intelligence Internship
- **Project Number:** 2
- **Project Title:** Data Classification Using AI
- **Programming Language:** Python
- **Algorithm:** K-Nearest Neighbors (KNN)
- **Dataset:** Iris Dataset

### 📄 License

This project is intended for educational and internship purposes. Add an appropriate open-source license if you plan to distribute the project publicly.

---

**Developed as part of the DecodeLabs AI Internship.**