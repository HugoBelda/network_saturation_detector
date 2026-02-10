import time
import psutil

from processing.throughput import calculate_throughput
from storage.history  import append_sample

INTERFACE = "en0"
INTERVAL = 1

prev = psutil.net_io_counters(pernic=True)[INTERFACE]

while True:
    time.sleep(INTERVAL)

    curr = psutil.net_io_counters(pernic=True)[INTERFACE]

    tx, rx = calculate_throughput(prev, curr, INTERVAL)

    print(f"TX: {tx:.2f} Mbps | RX: {rx:.2f} Mbps")
    append_sample(tx, rx)

    # Move window
    prev = curr


