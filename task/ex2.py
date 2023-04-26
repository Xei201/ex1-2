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





