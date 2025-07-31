import streamlit as st
import pandas as pd
import datetime
import os
from utils import (
    load_data, save_event,
    plot_disruption_heatmap, plot_drift_trend,
    export_to_google_sheet
)

st.set_page_config(page_title="Behavior Tracker", layout="centered")

st.title("🧠 Behavior Pattern Tracker for Teachers with ADHD")

# ---- Event Logger ----
st.header("📋 Log a New Event")
event_type = st.selectbox("Event Type", ["Disruption", "Transition", "Drift", "Intervention", "Mood"])
group = st.selectbox("Group / Student", ["Whole Class", "Group A", "Group B", "Student 1", "Student 2"])
group_id = hash(group) % 10000  # anonymize group
trigger = st.selectbox("Trigger", ["Transition", "Conflict", "Off-task", "Noise", "Unclear Directions", "N/A"])
mood = st.selectbox("Mood (if applicable)", ["🙂", "😐", "😫", "None"])
notes = st.text_input("Optional Notes")

if st.button("Log Event"):
    save_event(event_type, f"Group_{group_id}", trigger, mood, notes)
    st.success("✅ Event logged!")

# ---- Data Viewer ----
st.header("📊 Logged Events")
df = load_data()
st.dataframe(df, use_container_width=True)

# ---- Visualizations ----
st.header("📈 Visual Patterns")

st.subheader("Disruption Heatmap (Time of Day)")
plot_disruption_heatmap(df)

st.subheader("Focus Drift Trend")
plot_drift_trend(df)

# ---- Export to Google Sheets ----
st.header("📤 Export Logs")
if st.button("Export to Google Sheets"):
    try:
        export_to_google_sheet(df)
        st.success("✅ Data exported to Google Sheets successfully!")
    except Exception as e:
        st.error(f"❌ Error exporting to Google Sheets: {e}")
