def is_anomalous(current, avg, dev, k=2):
    """
    Decide whether current value is abnormal.
    """

    if avg is None or dev is None:
        return False

    threshold = avg + k * dev
    return current > threshold


def evaluate_anomaly(current, avg, dev, k=2):
    if avg is None or dev is None:
        return False, None

    threshold = avg + k * dev
    return current > threshold, threshold
