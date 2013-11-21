from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import lib.statistics.average


def get_canvas(series):
    top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)

    for serie in series:
        dates, values = zip(*serie)
        top.plot_date(dates, values, '-')

    plt.title('Microsoft Opening Stock Price from 2007 - 2012')
    plt.legend()
    return FigureCanvasAgg(plt.gcf())


def moving_average(data, *ma):
    data = [(x.date, float(x.average_price)) for x in data]
    series = [data]
    ma = [int(x) for x in ma]
    for window_size in ma:
        series.append(lib.statistics.average.moving_average(data, window_size))
    return get_canvas(series)
