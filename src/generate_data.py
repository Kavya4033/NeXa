import numpy as np
import pandas as pd

# Make results reproducible
np.random.seed(42)

# --------------------------------------------------
# 1. Generate dates
# --------------------------------------------------

dates = pd.date_range(
    start="2026-01-01",
    end="2026-06-30",
    freq="D"
)

n = len(dates)


# --------------------------------------------------
# 2. Generate basic productivity variables
# --------------------------------------------------

hours_worked = np.random.normal(
    loc=8,
    scale=0.8,
    size=n
)

focus_hours = np.random.normal(
    loc=5.5,
    scale=1.0,
    size=n
)

meetings = np.random.poisson(
    lam=3,
    size=n
)

tasks_completed = np.random.poisson(
    lam=8,
    size=n
)

breaks_taken = np.random.poisson(
    lam=4,
    size=n
)


# --------------------------------------------------
# 3. Keep values realistic
# --------------------------------------------------

hours_worked = np.clip(
    hours_worked,
    4,
    12
)

focus_hours = np.clip(
    focus_hours,
    1,
    hours_worked
)

meetings = np.clip(
    meetings,
    0,
    10
)

tasks_completed = np.clip(
    tasks_completed,
    0,
    20
)

breaks_taken = np.clip(
    breaks_taken,
    0,
    10
)


# --------------------------------------------------
# 4. Calculate productivity score
# --------------------------------------------------

productivity_score = (
    40
    + focus_hours * 7
    + tasks_completed * 2
    - meetings * 2
    - (hours_worked - 8) * 1.5
    + np.random.normal(0, 5, n)
)

productivity_score = np.clip(
    productivity_score,
    0,
    100
)


# --------------------------------------------------
# 5. Create DataFrame
# --------------------------------------------------

df = pd.DataFrame({
    "date": dates,
    "hours_worked": hours_worked.round(2),
    "focus_hours": focus_hours.round(2),
    "meetings": meetings,
    "tasks_completed": tasks_completed,
    "breaks_taken": breaks_taken,
    "productivity_score": productivity_score.round(2)
})


# --------------------------------------------------
# 6. Add a few unusual observations
# --------------------------------------------------

anomaly_indices = [45, 100, 150]

df.loc[anomaly_indices[0], "hours_worked"] = 12
df.loc[anomaly_indices[0], "focus_hours"] = 2
df.loc[anomaly_indices[0], "meetings"] = 9
df.loc[anomaly_indices[0], "tasks_completed"] = 3

df.loc[anomaly_indices[1], "hours_worked"] = 4
df.loc[anomaly_indices[1], "focus_hours"] = 1
df.loc[anomaly_indices[1], "meetings"] = 8
df.loc[anomaly_indices[1], "tasks_completed"] = 2

df.loc[anomaly_indices[2], "hours_worked"] = 11
df.loc[anomaly_indices[2], "focus_hours"] = 8
df.loc[anomaly_indices[2], "meetings"] = 0
df.loc[anomaly_indices[2], "tasks_completed"] = 18


# --------------------------------------------------
# 7. Save the dataset
# --------------------------------------------------

df.to_csv(
    "data/productivity_data.csv",
    index=False
)

print("Dataset generated successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("Saved to: data/productivity_data.csv")
