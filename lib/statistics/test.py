from unittest import TestCase
from datetime import date
from lib.statistics.average import moving_average

class MovingAverageTest(TestCase):
    dates = [date(2000, 3, x) for x in xrange(1,11)]

    def test_flat(self):
        data = zip(self.dates, [1]*10)
        ret = moving_average(data, 2)
        self.assertEqual(ret, zip(self.dates[2:], [1.0]*8))

    def test_peak(self):
        data = zip(self.dates, range(1, 6) + range(1, 6)[::-1])
        ret = moving_average(data, 4)
        expected_values = [x/4.0 for x in (10, 14, 17, 18, 17, 14, 10)]
        self.assertEqual(ret, zip(self.dates[4:], expected_values))