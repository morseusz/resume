import datetime
import factory
from django.test import TestCase
from app.charts.models import GoldPrice

class GoldPriceFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = GoldPrice


class GoldPriceTest(TestCase):
    def setUp(self):
        self.monthly_prices = []
        for day in xrange(1, 30):
            date = datetime.date(2000, 1, day)
            price = 10.00 + day
            self.monthly_prices.append((date, price))
            GoldPriceFactory(date=date, average_price=price)

    def test_get_date_range_valid(self):
        """No extensive testing, since it's Django functionality"""
        start_day = 5
        end_day = -5
        start_date = self.monthly_prices[start_day][0]
        end_date = self.monthly_prices[end_day][0]
        date_range = GoldPrice.objects.get_date_range(start_date, end_date)
        self.assertEqual(self.monthly_prices[start_day:end_day + 1],
                         [(x.date, x.average_price) for x in date_range])

    def tearDown(self):
        pass