from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import numpy
import lib.statistics.average


def get_canvas(series, title=''):
    """Draws all the given series on a single plot and returns an
    object suited for creating 'img/png' HTTP response in Django.

    series - timed data series with corresponding labels
             e.g. ('Gold', ((datetime(2012, 1, 1), 990.99), (..)),
                   'Silver', ((datetime(2012, 1, 12), 7.23), (..)),
                   )
    title - title of the whole plot

    """
    top = plt.subplot2grid((4,4), (0, 0), rowspan=4, colspan=4)

    for label, serie in series:
        if not serie:
            continue
        dates, values = zip(*serie)
        top.plot_date(dates, values, '-', label=label)

    plt.title(title)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
    fig = plt.gcf()
    fig.autofmt_xdate()
    return FigureCanvasAgg(fig)


def moving_average(data, *ma, **kwargs):
    """Wraps get_canvas in order to draw the given data series and
    several of it's moving averages.

    Positional args:
    data - tuple of samples e.g. ((datetime(2012, 1, 1), 990.99), (..))
    ma - moving average window samples

    Keyword args:
    asset_name - will be used to construct plot title

    """
    data = [(x.date, float(x.average_price)) for x in data]
    series = [('Daily avg', data)]
    ma = sorted([int(x) for x in ma])
    for window in ma:
        series.append(('MA %s'%window,
                      lib.statistics.average.moving_average(data, window)))
    shortest = len(series[-1][1])
    print shortest
    series = [(x, y[-shortest:]) for x, y in series]
    return get_canvas(series,
                      title='Daily and MA: %s'%kwargs.get('asset_name'))
