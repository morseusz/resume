from django.db import models


class PriceManager(models.Manager):
    def get_date_range(self, start_date, end_date):
        return self.filter(date__range=(start_date, end_date))


class GoldPrice(models.Model):
    date = models.DateField(primary_key=True)
    average_price = models.DecimalField(max_digits=7, decimal_places=2)
    objects = PriceManager()


def get_model(name):
    """ Returns a class object, defined in this module, based on name
    argument.

    >>get_model('gold')
    >><class 'GoldPrice'>

    """
    for price in filter(lambda e: e[-5:] == 'Price', globals()):
        if name == price[:-5].lower():
            return globals()[price]
    return None