import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.environ["PANDAS_USE_ARROW"] = "0"


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Productivity Dashboard",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# Load data
# -----------------------------

df = pd.read_csv("data/productivity_data.csv")

df["date"] = pd.to_datetime(df["date"])


# -----------------------------
# Title
# -----------------------------

st.title("📊 Productivity Dashboard")

st.markdown(
    "An interactive dashboard for analyzing daily productivity."
)


# -----------------------------
# KPI calculations
# -----------------------------

avg_productivity = df["productivity_score"].mean()
avg_hours = df["hours_worked"].mean()
avg_focus = df["focus_hours"].mean()
total_tasks = df["tasks_completed"].sum()


# -----------------------------
# KPI cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Productivity",
    f"{avg_productivity:.1f}"
)

col2.metric(
    "Average Hours Worked",
    f"{avg_hours:.1f}"
)

col3.metric(
    "Average Focus Hours",
    f"{avg_focus:.1f}"
)

col4.metric(
    "Total Tasks Completed",
    f"{total_tasks:,}"
)


# -----------------------------
# Productivity over time
# -----------------------------

st.subheader("Productivity Over Time")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df["date"],
    df["productivity_score"],
    color="royalblue"
)

ax.set_xlabel("Date")
ax.set_ylabel("Productivity Score")

st.pyplot(fig)


# -----------------------------
# Relationships
# -----------------------------

st.subheader("Productivity Relationships")

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="focus_hours",
        y="productivity_score",
        ax=ax
    )

    ax.set_title("Focus Hours vs Productivity")

    st.pyplot(fig)


with col2:

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="meetings",
        y="productivity_score",
        ax=ax
    )

    ax.set_title("Meetings vs Productivity")

    st.pyplot(fig)
