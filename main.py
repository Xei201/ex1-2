import unittest

from task.ex1 import date_diff
from task.ex2 import find_min


class TestDate(unittest.TestCase):
    date1 = "2019-06-29"
    date2 = "2019-06-30"
    result_true = 1

    def test_date(self):
        result = date_diff(self.date1, self.date2)
        print(result)
        self.assertEqual(self.result_true, result)


class TestData2(TestDate):
    date1 = "2020-01-15"
    date2 = "2019-12-31"
    result_true = 15


class TestMinNum(unittest.TestCase):
    num = "1432219"
    k = 3
    result_true = 1219

    def test1(self):
        result = find_min(self.num, self.k)
        print(result)
        self.assertEqual(self.result_true, result)


class TestMinNum2(TestMinNum):
    num = "10200"
    k = 1
    result_true = 200


class TestMinNum3(TestMinNum):
    num = "450047"
    k = 2
    result_true = 47


class TestMinNum4(TestMinNum):
    num = "23"
    k = 1
    result_true = 2


if __name__ == '__main__':
    unittest.main()