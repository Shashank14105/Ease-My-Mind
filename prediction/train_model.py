import pandas as pd
import numpy as np
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report


# Load Kaggle Dataset
df = pd.read_csv("dataset/depression_student_dataset.csv")

print(df.head())
print(df.columns)

# Add these lines
print("\nDepression value counts:")
print(df["Depression"].value_counts())

print("\nUnique values:")
print(df["Depression"].unique())

# Synthetic Field Add 
np.random.seed(42)

df["Social Interaction"] = np.random.randint(0,11,len(df))

df["Exercise"] = np.random.randint(0,3,len(df))

df["Screen Time"] = np.random.randint(2,13,len(df))

# Suicide Column Drop
drop_columns = [
    "Have you ever had suicidal thoughts ?",
    "Family History of Mental Illness"
]

df.drop(columns=drop_columns, inplace=True, errors="ignore")

# Encode Categorical Features
gender_encoder = LabelEncoder()
df["Gender"] = gender_encoder.fit_transform(df["Gender"])

# Sleep Duration
sleep_encoder = LabelEncoder()
df["Sleep Duration"] = sleep_encoder.fit_transform(df["Sleep Duration"])

# Dietary Habits 
diet_encoder = LabelEncoder()

df["Dietary Habits"] = diet_encoder.fit_transform(
    df["Dietary Habits"]
)

# Feature Defination 
X = df[[
    "Gender",
    "Age",
    "Academic Pressure",
    "Study Satisfaction",
    "Sleep Duration",
    "Dietary Habits",
    "Study Hours",
    "Financial Stress",
    "Social Interaction",
    "Exercise",
    "Screen Time"
]]

y = df["Depression"]

# Random Forest Training 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nPrediction counts:")
print(pd.Series(pred).value_counts())


#Evalute
pred = model.predict(X_test)

print(classification_report(y_test,pred))


# Model Save
joblib.dump(model,"models/stress_model.pkl")

encoders = {
    "gender": gender_encoder,
    "sleep": sleep_encoder,
    "diet": diet_encoder
}

joblib.dump(encoders,"models/label_encoders.pkl")

os.makedirs("models", exist_ok=True)

#Save Model
joblib.dump(model, "models/stress_model.pkl")

#Save encoders
encoders = {
    "gender": gender_encoder,
    "sleep": sleep_encoder,
    "diet": diet_encoder
}

joblib.dump(encoders, "models/label_encoders.pkl")

print("Model and encoders saved successfully!")

print(df["Depression"].value_counts())
