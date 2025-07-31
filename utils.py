import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

DATA_FILE = "data.csv"

def load_data():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["timestamp", "event", "group", "trigger", "mood", "notes"])
        df.to_csv(DATA_FILE, index=False)
    return pd.read_csv(DATA_FILE)

def save_event(event, group, trigger, mood, notes):
    df = load_data()
    timestamp = datetime.now().isoformat()
    new_entry = pd.DataFrame([[timestamp, event, group, trigger, mood, notes]],
                             columns=df.columns)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def plot_disruption_heatmap(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    disruptions = df[df['event'] == "Disruption"]
    heat = disruptions.groupby('hour').size()
    if not heat.empty:
        sns.barplot(x=heat.index, y=heat.values, palette="Reds")
        plt.xlabel("Hour of Day")
        plt.ylabel("Disruptions")
        st.pyplot(plt.gcf())
        plt.clf()
    else:
        st.info("No disruptions logged yet.")

def plot_drift_trend(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    drifts = df[df['event'] == "Drift"]
    trend = drifts.groupby('date').size()
    if not trend.empty:
        trend.plot(kind='line', marker='o')
        plt.xlabel("Date")
        plt.ylabel("Drift Events")
        st.pyplot(plt.gcf())
        plt.clf()
    else:
        st.info("No drift events logged yet.")

def export_to_google_sheet(df, sheet_name="Behavior Logs"):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1
    sheet.clear()
    sheet.update([df.columns.values.tolist()] + df.values.tolist())
