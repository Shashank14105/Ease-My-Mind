# 🧠 Ease My Mind

<h3 align="center">

AI-Powered Mental Wellness Platform for Community Welfare of Students and Education Practitioners

</h3>

<p align="center">

Stress Prediction • Sentiment Analysis • AI Wellness Coach • Analytics Dashboard • Wellness Reports

</p>

---

## 🚀 Built With

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikitlearn\&logoColor=white"/>
<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge\&logo=huggingface\&logoColor=black"/>
<img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge\&logo=google\&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white"/>
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge\&logo=plotly\&logoColor=white"/>
<img src="https://img.shields.io/badge/ReportLab-0A0A0A?style=for-the-badge"/>
</p>

---

## Project Demonstration

<p align="center">
assets/demo.gif
</p>

---
# 🌍 Overview
Ease My Mind is an AI-powered mental wellness platform developed as a community welfare initiative for students and education practitioners.
The system predicts stress levels, analyzes emotions from journal entries, generates personalized wellness recommendations verified through Google's Gemini API, tracks emotional trends through dashboards, issues prolonged stress alerts, and generates downloadable wellness reports.

The project aims to promote proactive mental wellness support inside academic communities.

---

# 🧭 Easy Navigation
* 😊 Positive

* 😐 Neutral

* 😞 Negative

### Student-Friendly Dashboard

✅ Charts
✅ Alerts
✅ Stress Analytics
✅ Emotional History
✅ Wellness Trends
✅ Downloadable PDF Reports

---

# ⭐ Highlights

### ✔ Google Gemini Verified Wellness Advice
Personalized recommendations generated using Google's Gemini API for reliable and legitimate wellness guidance.

### ✔ Prolonged Stress Detection
Automatically detects repeated severe stress patterns and issues warning alerts.

### ✔ Medhā AI Companion
Supports multilingual conversations and provides emotional guidance and personality development support.

### ✔ Database Support
Stores historical wellness records for future analysis and progress tracking.

---

# ⚙ Workflow
User Inputs

↓

Random Forest

↓

Low / Moderate / Severe



Journal

↓

RoBERTa

↓

😊 Positive

😐 Neutral

😞 Negative



Hybrid Engine

↓

Final Stress Assessment



Google Gemini

↓

Personalized Advice

↓

Study Schedule

↓

Sleep Tips

↓

Daily Affirmations

---

# 🎯 Goals Achieved

✔ Developed an AI solution for community welfare.

✔ Designed a stress prediction model for students.

✔ Integrated journal sentiment analysis.

✔ Built a personalized AI wellness coach.

✔ Created an analytics dashboard.

✔ Added prolonged stress detection.

✔ Generated downloadable wellness reports.

✔ Developed Medhā AI companion.

✔ Encouraged proactive mental health awareness among students and education practitioners.

---

#  Problems Solved

Students often neglect emotional well-being due to academic pressure.

Lack of accessible mental wellness support.

Difficulty in recognizing prolonged stress.

No centralized emotional tracking system.

Absence of personalized wellness recommendations.

Limited awareness regarding mental health inside academic communities.


# ✨ Features

##  Stress Prediction using Random Forest

Predicts stress levels based on lifestyle and academic factors.

### Stress Levels

* 🟢 Low Stress

* 🟡 Moderate Stress

* 🔴 Severe Stress

---

## Journal Sentiment Analysis using RoBERTa

Analyzes daily journal entries and classifies emotions into:


* 😊 Positive

* 😐 Neutral

* 😞 Negative

---

## AI Wellness Coach Powered by Google Gemini

Generates legitimate personalized recommendations:

* Study Schedules

* Sleep Improvement Tips

* Screen Time Management

* Daily Affirmations

* Stress Relief Activities

---

## 📊 Analytics Dashboard

Provides:

* Stress Distribution Charts

* Sentiment Distribution Graphs

* Daily Wellness Trends

* Recent History Table

---

## 🚨 Prolonged Stress Alerts

Continuously monitors previous records and warns users when repeated severe stress patterns are detected.

This helps users seek support before stress escalates.

---
## 📄 Downloadable Wellness Reports

Generate beautifully formatted PDF reports containing:
* Current Wellness Summary

* Journal Entry

* AI Recommendations

* Wellness Analytics

* Stress Charts

* Sentiment Charts

---
## 🪷 Medhā AI Companion
A multilingual wellness companion for:
* Emotional support

* Personality development

* Study motivation

* General guidance

Supports conversations in multiple languages.
---

# Folder Structure

```text
├── 📁 alerts
│   └──alerts.py
├── 📁 assets
│   └── 🖼️ logo.png
├── 📁 chatbot
│   └──gemini_chatbot.py
├── 📁 dashboard
│   ├──__init__.py
│   └──dashboard.py
├── 📁 database
│   ├──database.py
│   ├── 📄 mood_history.db
│   └──save_log.py
├── 📁 dataset
│   └── 📄 depression_student_dataset.csv
├── 📁 generated_reports
├── 📁 memory
│   └──memory.py
├── 📁 models
│   ├── 📄 label_encoders.pkl
│   └── 📄 stress_model.pkl
├── 📁 prediction
│   ├──stress_predictor.py
│   ├──tempCodeRunnerFile.py
│   ├──test.py
│   └──train_model.py
├── 📁 reports
│   └──generate_report.py
├── 📁 reports_output
│   ├── 🖼️ sentiment_chart.png
│   ├── 🖼️ stress_chart.png
│   └── 📕 wellness_report.pdf
├── 📁 sentiment
│   └──sentiment_analysis.py
├──app.py
├── 📄 requirements.txt
└──sentiment_test.py
```

---

## Historical Database Support

All wellness records are securely stored and can be used for:

Progress Tracking

Emotional Trend Analysis

Stress Pattern Detection

Future Wellness Insights


This enables users to better understand their mental well-being over time.

---



## AI Workflow

&#x20;                User Inputs

&#x20;                     ↓

&#x20;              Random Forest Model

&#x20;                     ↓

&#x20;         Low / Moderate / Severe Stress

&#x20;                     ↓



&#x20;                Journal Entry

&#x20;                     ↓

&#x20;              RoBERTa Sentiment Model

&#x20;                     ↓

&#x20;        😊 Positive | 😐 Neutral | 😞 Negative

&#x20;                     ↓



&#x20;                Hybrid Engine

&#x20;                     ↓

&#x20;           Final Stress Assessment

&#x20;                     ↓



&#x20;                Google Gemini

&#x20;                     ↓

&#x20;            Personalized Advice

&#x20;                     ↓

&#x20;             Study Schedule Tips

&#x20;                     ↓

&#x20;                Sleep Tips

&#x20;                     ↓

&#x20;              Daily Affirmations

--- 



## 🎓 Community Welfare Impact

Ease My Mind was developed to promote mental wellness among:

### Students

Academic pressure, examination stress, burnout and emotional imbalance are common challenges faced by students. The platform helps them recognize stress early and develop healthy habits.

### Education Practitioners

Teachers and educators also experience professional stress. The system provides personalized support and wellness recommendations for maintaining emotional well-being.

### Personality Development

Beyond stress prediction, Ease My Mind encourages:

Self-awareness

Positive habits

Better sleep routines

Healthy study schedules

Emotional resilience

Productivity and personal growth

The ultimate goal is to create a healthier academic community through accessible AI-driven wellness support.

---

# 🛠 Tech Stack

### Backend
* Python

### Interface
* Streamlit

### Machine Learning
* Scikit-Learn
* Random Forest

### NLP
* Hugging Face Transformers
* RoBERTa

### Generative AI
* Google Gemini API
  
### Visualization
* Plotly
* Matplotlib
  
### Database
* SQLite

### Report Generation
* ReportLab

---



# ⚡ Product-Level Optimizations

### Session State Preservation

Prevents prediction results from disappearing when switching pages.


### PDF Download Integration
Users can instantly download wellness reports.


### Database Logging

Stores historical records for future analysis.

### Risk Detection System

Tracks repeated severe stress patterns.

### Faster User Experience

Reduced unnecessary reruns and improved navigation responsiveness.

### Modular Architecture

Separated project into independent components for maintainability.


---



# Bugs Faced and Fixed

### Duplicate Database Entries

Problem 1:
Records were saved multiple times due to Streamlit reruns.
Solution:
Moved logging inside prediction event.


### Download Button Disappearing

Problem2:
Report download button vanished after reruns.
Solution:
Implemented Session State management.

### UnboundLocalError in Alerts

Problem3:
Counter variable was not initialized.
Solution:
Proper initialization before incrementing.

### Cluttered PDF Layout

Problem4:
Sections overlapped and charts disappeared.
Solution:
Improved spacing, separators and page flow.

### Streamlit Reruns

Problem5:
Repeated executions slowed down the application.
Solution:
Optimized state handling and reduced unnecessary processing.

---



# Why Ease My Mind?

Designed as a community welfare initiative for students and education practitioners, Ease My Mind provides an intelligent, student-friendly ecosystem for emotional well-being.

## 📊 Student-Friendly Dashboard

The dashboard provides:

📈 Interactive Charts

🚨 Prolonged Stress Alerts

🔥 Mood Streak Counts (V2)

📑 Downloadable Wellness Reports

📅 Emotional History Tracking

📉 Stress Trends Visualization

Making mental wellness easy to understand and monitor.



## 🤖 Google-Verified Wellness Advice
Personalized recommendations are generated using the Google Gemini API, providing reliable and legitimate wellness guidance.
Recommendations include:

✅ Study Schedule Suggestions

✅ Sleep Improvement Tips

✅ Screen-Time Management

✅ Daily Affirmations

✅ Relaxation Activities

✅ Productivity Guidance


## 🪷 Medhā AI Companion

Medhā AI is an intelligent multilingual wellness companion.

Supports:

 Multiple Languages

 Emotional Support

 Study Motivation

 Personality Development

 Stress Management

 General Guidance


Providing a friendly and accessible experience for users from diverse backgroun



---

# 👨‍💻 Author

### Shashank Kumar

B.Tech CSE (AI \& ML)
Passionate about Artificial Intelligence, Machine Learning and Community-Oriented Software Solutions.

### Connect with Me

GitHub:

https://github.com/Shashank14105

LinkedIn:

https://linkedin.com/in/urs-trulyshashank

Email:

[shashankkumar14105@gmail.com](mailto:your-email@example.com)

---
## ⭐ If you found this project useful, consider giving it a star!



