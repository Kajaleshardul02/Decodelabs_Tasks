
"""
DecodeLabs AI Internship
Project 3: AI Recommendation System
Uses TF-IDF and cosine similarity to rank recommendations.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Items available for recommendation
ITEMS = {
    "Python Development": "python programming coding software development",
    "AI and Machine Learning": "artificial intelligence AI machine learning deep learning",
    "Web Development": "HTML CSS JavaScript frontend backend web development",
    "Data Science": "data science data analysis statistics visualization python",
    "Cybersecurity": "cybersecurity network security ethical hacking encryption",
    "Cloud Computing": "cloud computing AWS Azure deployment servers",
    "Automation and Robotics": "automation robotics sensors control systems python",
    "Mobile App Development": "mobile app Android iOS application development",
    "Computer Vision": "computer vision image processing object detection AI",
    "Database Management": "SQL databases data storage queries database management",
}


def recommend_items(user_interests, top_n=5):
    """Rank available items by similarity to user interests."""

    if not user_interests:
        return []

    item_names = list(ITEMS.keys())
    item_descriptions = list(ITEMS.values())

    # Combine the user's interests into one profile.
    user_profile = " ".join(user_interests)

    # Convert item descriptions and the user profile to TF-IDF vectors.
    documents = item_descriptions + [user_profile]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compare the user profile with every available item.
    user_vector = tfidf_matrix[-1]
    item_vectors = tfidf_matrix[:-1]
    scores = cosine_similarity(user_vector, item_vectors).flatten()

    # Sort recommendations from highest similarity to lowest.
    ranked_indices = scores.argsort()[::-1]

    results = []
    for index in ranked_indices[:min(top_n, len(item_names))]:
        results.append((item_names[index], scores[index]))

    return results


def get_user_interests():
    """Read interests from an interactive terminal."""

    while True:
        try:
            text = input(
                "Enter at least three interests, separated by commas: "
            ).strip()
        except (EOFError, OSError):
            print(
                "\nInteractive input is unavailable in this console.\n"
                "Run this program in a terminal that supports keyboard input."
            )
            return None

        interests = [
            interest.strip()
            for interest in text.split(",")
            if interest.strip()
        ]

        if len(interests) >= 3:
            return interests

        print("Please enter at least three interests.")
        print("Example: Python, AI, automation")


def main():
    print("=" * 55)
    print("             AI RECOMMENDATION SYSTEM")
    print("=" * 55)
    print("This system recommends topics based on your interests.")
    print("Example interests: Python, AI, automation")
    print()

    interests = get_user_interests()

    # Stop safely if this console cannot receive keyboard input.
    if interests is None:
        return

    recommendations = recommend_items(interests, top_n=5)

    print("\nYour interests:", ", ".join(interests))
    print("\nTop recommendations")
    print("-" * 55)

    for rank, (name, score) in enumerate(recommendations, start=1):
        print(f"{rank}. {name} (similarity: {score:.2%})")

    print("\nRecommendation process completed.")


if __name__ == "__main__":
    main()
