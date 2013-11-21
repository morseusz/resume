from datetime import datetime
from django.http import HttpResponse
from lib.statistics.average import moving_average
from app.charts.models import get_model
import lib.plot.time


def display_moving_average(request, alias):
    """Draws the price of the given asset as well as computed MA series
    on a single plot and returns it as an image.

    alias - name of the asset e.g. 'gold'

    """
    #TODO: handle invalid requests types & missing args
    model = get_model(alias)
    start = request.GET.get('start')
    end = request.GET.get('end')
    ma = request.GET.get('ma')

    start, end = [datetime.strptime(x, '%Y-%m-%d') for x in start, end]
    ma = ma.split(',') if ',' in ma else ma

    data = model.objects.get_date_range(start, end)
    canvas = lib.plot.time.moving_average(data, *ma, asset_name=alias)

    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

