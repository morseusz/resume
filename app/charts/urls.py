from django.conf.urls import patterns, url
from app.charts.views import display_moving_average

urlpatterns = patterns('',
    url(r'moving_average/(\w{1,10})', display_moving_average),
)