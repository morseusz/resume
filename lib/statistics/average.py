def moving_average(data, window_size):
    """Computes moving average for the given sample series.

    data - tuple of samples e.g. ((datetime(2012, 1, 1), 990.99), (..))
    window_size -length of the window used to compute average

    """
    if window_size >= len(data):
        return []

    averages = [(data[window_size][0],
                sum(x[1] for x in data[:window_size])/float(window_size))]

    for i, data_point in enumerate(data[window_size + 1:]):
        date_right, val_right = data_point[0], data[i + window_size][1]
        date_left, val_left = data[i]
        last_val = averages[-1][1]
        averages.append((date_right,
                        last_val + (val_right - val_left)/float(window_size)))

    return averages