from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter


def get_canvas(*series):
    figure = Figure()
    x = figure.add_subplot(111)

    for serie in series:
        dates, values = zip(*serie)
        x.plot_date(dates, values, '-')

    x.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    figure.autofmt_xdate()
    return FigureCanvasAgg(figure)