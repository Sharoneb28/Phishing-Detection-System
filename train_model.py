import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (CSV!)
data = pd.read_csv("dataset/Phishing_Legitimate_full.csv")  # <-- check filename matches exactly

# Remove ID column if exists
if "id" in data.columns:
    data = data.drop("id", axis=1)

# Features and label
X = data.drop("CLASS_LABEL", axis=1)
y = data["CLASS_LABEL"]

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "model/phishing_model.pkl")
print("Model saved successfully!")
