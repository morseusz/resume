from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import lib.statistics.average


def get_canvas(series, title=''):
    top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)

    for label, serie in series:
        dates, values = zip(*serie)
        top.plot_date(dates, values, '-', label=label)

    plt.title(title)
    plt.legend()
    return FigureCanvasAgg(plt.gcf())


def moving_average(data, *ma, **kwargs):
    data = [(x.date, float(x.average_price)) for x in data]
    series = [('Daily avg', data)]
    ma = [int(x) for x in ma]
    for window in ma:
        series.append(('MA %s'%window,
                      lib.statistics.average.moving_average(data, window)))
    return get_canvas(series,
                      title='Daily and MA: %s'%kwargs.get('asset_name'))
