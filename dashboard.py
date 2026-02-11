import pandas as pd
import streamlit as st

DATA = "storage/history.csv"

st.title("Network Saturation Monitor")

df = pd.read_csv(DATA)
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.line_chart(df.set_index("timestamp")[["rx_mbps", "tx_mbps"]])