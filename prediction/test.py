# import os
# import joblib

# print(os.path.getsize("models/stress_model.pkl"))
# print(os.path.getsize("models/label_encoders.pkl"))

# model = joblib.load("models/stress_model.pkl")
# encoders = joblib.load("models/label_encoders.pkl")

# print("Loaded successfully!")

print(df["Depression"].value_counts())