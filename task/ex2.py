import unittest


def find_min(number, k):
    # Отсчёт попыток
    k = k - 1
    if k < 0:
        # Прерывние рекурсии при окончании попыток
        return int(number)
    for item in range(len(number) - 1):
        # Последовательно сверяем текущий итем с последующим,
        # если последующий меньше удаляем текущий элемент
        if int(number[item]) > int(number[item+1]):
            res = number[:item] + number[item + 1:]
            return find_min(res, k)
    if int(number[:-1]) > int(number[1:]):
        # в случае если не был найден элемент к удалению,
        # проводим сравнение срезов строки без 1 и -1 элементов
        print(number[1:])
        return find_min(number[1:], k)
    return find_min(number[:-1], k)


class TestMinNum(unittest.TestCase):
    num = "1432219"
    k = 3
    result_true = 1219

    def test1(self):
        result = find_min(self.num, self.k)
        self.assertEqual(self.result_true, result)


class TestMinNum2(unittest.TestCase):
    num = "10200"
    k = 1
    result_true = 200


class TestMinNum2(unittest.TestCase):
    num = "450047"
    k = 2
    result_true = 47


class TestMinNum2(unittest.TestCase):
    num = "23"
    k = 1
    result_true = 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()


