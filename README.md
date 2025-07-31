[README.md](https://github.com/user-attachments/files/21536452/README.md)
# 🧠 Behavior Pattern Tracker for Teachers with ADHD

This is a lightweight classroom behavior logging tool built with Streamlit, designed to support teachers with ADHD. It tracks disruptions, attention drift, mood, and transitions — then visualizes patterns over time.

### ✅ NEW FEATURES:
- 🔐 Student Group Anonymization
- 😊 Mood Logging (🙂 😐 😫)
- 📤 Export to Google Sheets

---

## 🚀 Features

- 📋 Log classroom events (Disruption, Transition, Drift, Mood, Interventions)
- 🧑‍🏫 Anonymized student/group input (hashed group ID)
- 📊 Behavior visualizations:
  - Disruption heatmap by time of day
  - Teacher focus drift over time
- 😊 Mood check-ins per event
- 📤 One-click export to **Google Sheets**

---

## 🛠️ How to Run Locally

### 1. Clone or Download This Repo

```bash
git clone https://github.com/yourusername/behavior-tracker-app.git
cd behavior-tracker-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🔐 Setup Google Sheets Export

1. Get a `credentials.json` file from your Google Cloud Console
2. Enable the Google Sheets API
3. Share your target Google Sheet with the service account
4. Place `credentials.json` in the project folder

---

## 📤 Export Data

Click the **“Export to Google Sheets”** button in the app.

---

## 📁 File Overview

| File              | Description                         |
|-------------------|-------------------------------------|
| `app.py`          | Main Streamlit application          |
| `utils.py`        | Helper functions + plotting/export  |
| `requirements.txt`| Python dependencies                 |
| `credentials.json`| Your Google API key (not included)  |
| `data.csv`        | Local log file (auto-created)       |

---

## 📜 License

MIT — feel free to modify, share, and build on this.
