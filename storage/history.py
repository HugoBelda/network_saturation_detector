from datetime import datetime
import csv
import os

# Directory where this file (history.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, "history.csv")

def append_sample(tx, rx):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as f:
        writter = csv.writer(f)

        if not file_exists:
            writter. writerow(["timestamp","tx_mbps", "rx_mbps"])
        
        writter.writerow([datetime.now().isoformat(), tx, rx])

