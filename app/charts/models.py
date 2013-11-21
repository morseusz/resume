from django.db import models


class PriceManager(models.Manager):
    def get_date_range(self, start_date, end_date):
        return self.filter(date__range=(start_date, end_date))


class GoldPrice(models.Model):
    date = models.DateField(primary_key=True)
    average_price = models.DecimalField(max_digits=7, decimal_places=2)
    objects = GoldPriceManager()