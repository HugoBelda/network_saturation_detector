import time
import psutil

from processing.throughput import calculate_throughput
from storage.history  import append_sample
from detection.baseline import compute_baseline
from detection.alerts import is_anomalous


INTERFACE = "en0"
INTERVAL = 1
WINDOW_SIZE = 60
rx_window = []

prev = psutil.net_io_counters(pernic=True)[INTERFACE]

while True:
    time.sleep(INTERVAL)

    curr = psutil.net_io_counters(pernic=True)[INTERFACE]

    tx, rx = calculate_throughput(prev, curr, INTERVAL)

    print(f"TX: {tx:.2f} Mbps | RX: {rx:.2f} Mbps")
    append_sample(tx, rx)
    # store value in sliding window
    rx_window.append(rx)

    if len(rx_window) > WINDOW_SIZE:
        rx_window.pop(0)

    # compute normal behaviour
    avg, dev = compute_baseline(rx_window)

    # evaluate anomaly
    if is_anomalous(rx, avg, dev):
        print("⚠️  SATURATION RISK")

    # Move window
    prev = curr


