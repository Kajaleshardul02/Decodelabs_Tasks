
"""
DecodeLabs AI Internship
Project 2: Data Classification Using AI

Requirements:
- Load and understand a dataset
- Split data into training and testing sets
- Apply K-Nearest Neighbors (KNN)
- Scale features
- Train and predict
- Evaluate using confusion matrix and F1 score
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score
)


def main():
    # 1. Load the dataset
    iris = load_iris()

    X = iris.data
    y = iris.target

    print("=" * 55)
    print("       DATA CLASSIFICATION USING AI")
    print("=" * 55)

    # 2. Understand the dataset
    print("\nDataset Information")
    print("Number of samples:", X.shape[0])
    print("Number of features:", X.shape[1])
    print("Feature names:", iris.feature_names)
    print("Target classes:", iris.target_names)

    # 3. Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # 4. Scale features without data leakage
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 5. Create and train the KNN classifier
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)

    # 6. Make predictions
    y_pred = model.predict(X_test_scaled)

    # 7. Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    weighted_f1 = f1_score(
        y_test, y_pred, average="weighted"
    )

    print("\nModel Evaluation")
    print("-" * 40)
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Weighted F1 Score: {weighted_f1:.4f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=iris.target_names,
            zero_division=0
        )
    )

    # 8. Predict a new flower
    print("\nNew Flower Prediction")
    new_flower = [[5.1, 3.5, 1.4, 0.2]]

    new_flower_scaled = scaler.transform(new_flower)
    prediction = model.predict(new_flower_scaled)[0]

    print("Measurements:", new_flower[0])
    print("Predicted species:", iris.target_names[prediction])


if __name__ == "__main__":
    main()
