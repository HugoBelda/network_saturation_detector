from statistics import mean, stdev


def compute_baseline(values):
    """
    Receive a list of historical throughput values.
    Return average and deviation.
    """

    if len(values) < 2:
        return None, None

    return mean(values), stdev(values)
