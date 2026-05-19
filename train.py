# train.py

# STEP 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# STEP 2: Create Sample Dataset
data = {
    "text": [
        "India won the cricket match",
        "The movie was very entertaining",
        "The government passed a new law",
        "The football team scored a goal",
        "New technology is changing the world",
        "The actor gave a great performance",
        "Parliament elections will happen soon",
        "AI and Machine Learning are trending"
    ],
    
    "category": [
        "Sports",
        "Entertainment",
        "Politics",
        "Sports",
        "Technology",
        "Entertainment",
        "Politics",
        "Technology"
    ]
}

# STEP 3: Convert into DataFrame
df = pd.DataFrame(data)

# STEP 4: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["category"],
    test_size=0.2,
    random_state=42
)

# STEP 5: Convert Text into Numbers
vectorizer = CountVectorizer()

X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# STEP 6: Train Model
model = MultinomialNB()

model.fit(X_train_vectors, y_train)

# STEP 7: Predict Test Data
predictions = model.predict(X_test_vectors)

# STEP 8: Check Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# STEP 9: Test Custom Input
custom_text = ["The team played an amazing cricket tournament"]

custom_vector = vectorizer.transform(custom_text)

prediction = model.predict(custom_vector)

print("\nInput:", custom_text[0])
print("Predicted Category:", prediction[0])