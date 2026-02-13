import pandas as pd
import streamlit as st
from statistics import mean, stdev
import time

REFRESH_EVERY = .5  # seconds

WINDOW_SIZE = 60
K = 2

df = pd.read_csv("storage/history.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

thresholds = []
values = df["rx_mbps"].tolist()

for i in range(len(values)):
    window = values[max(0, i - WINDOW_SIZE):i]

    if len(window) > 1:
        avg_i = mean(window)
        dev_i = stdev(window)
        thresholds.append(avg_i + K * dev_i)
    else:
        thresholds.append(0)

df["threshold"] = thresholds

# Current value
current_rx = df["rx_mbps"].iloc[-1]

# Build recent window
recent = df["rx_mbps"].tail(WINDOW_SIZE)

if len(recent) > 1:
    avg = mean(recent)
    dev = stdev(recent)
    threshold = avg + K * dev
else:
    avg, threshold = 0, 0

# KPI display
st.title("Network Saturation Monitor")

c1, c2, c3 = st.columns(3)
c1.metric("Current RX", f"{current_rx:.2f} Mbps")
c2.metric("Baseline", f"{avg:.2f} Mbps")
c3.metric("Limit", f"{threshold:.2f} Mbps")

st.subheader("RX vs Threshold")

st.line_chart(
    df.set_index("timestamp")[["rx_mbps", "threshold"]]
)

df["alert"] = df["rx_mbps"] > df["threshold"]

# show how many times limit was crossed
num_alerts = int(df["alert"].sum())
st.metric("Total Alerts", num_alerts)

# Health state
if current_rx > threshold and threshold > 0:
    st.error("DEGRADED")
else:
    st.success("NORMAL")

time.sleep(REFRESH_EVERY)
st.rerun()
