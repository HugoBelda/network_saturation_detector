
def calculate_throughput(prev, curr, interval):
    """
    Convert cumulative network counters into throughput rates.

    Parameters
    ----------
    prev : snetio
        Previous counter snapshot.
    curr : snetio
        Current counter snapshot.
    interval : float
        Time in seconds between samples.

    Returns
    -------
    tuple(float, float)
        Mbps sent, Mbps received.
    """

    # Difference between two readings = bytes transferred during interval
    bytes_sent = curr.bytes_sent - prev.bytes_sent
    bytes_recv = curr.bytes_recv - prev.bytes_recv

    # Convert Bytes → bits (x8)
    # Convert → Megabits (/ 1_000_000)
    # Divide by time to obtain rate
    mbps_sent = bytes_sent * 8 / 1_000_000 / interval
    mbps_recv = bytes_recv * 8 / 1_000_000 / interval

    return mbps_sent, mbps_recv


