import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "alerts.csv")


def append_alert(value, threshold):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "value_mbps", "threshold_mbps"])

        writer.writerow([datetime.now().isoformat(), value, threshold])
