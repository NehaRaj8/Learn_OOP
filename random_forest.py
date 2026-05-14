import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder


# 1. Load data

df = pd.read_csv("data/patients.csv")


# 2. Clean text data

df['condition'] = df['condition'].astype(str).str.strip().str.lower()


# 3. Encode labels

encoder = LabelEncoder()
df['condition'] = encoder.fit_transform(df['condition'])

# Optional: show mapping
print("Class mapping:")
for i, class_name in enumerate(encoder.classes_):
    print(f"{class_name} -> {i}")


# 4. Features and target

X = df[['age', 'heart_rate', 'systolic_bp']]
y = df['condition']


# 5. Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 6. Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced'
)


# 7. Train model

model.fit(X_train, y_train)


# 8. Predictions

y_pred = model.predict(X_test)


# 9. Evaluation

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 10. Optional: decode predictions

decoded = encoder.inverse_transform(y_pred)
print("\nSample predictions (decoded):")
print(decoded[:10])