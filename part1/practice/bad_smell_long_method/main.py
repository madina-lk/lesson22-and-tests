# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(input_data):
    """
    Чтение данных из строки
    """
    result_data = [item.split(';') for item in input_data.split('\n')]

    return result_data


def _sort(input_data):
    """
    Сортировка по возрасту по возрастанию
    """
    return sorted(input_data)


def _filter(input_data):
    """
    Фильтрация
    """
    result_data = [person for person in input_data if int(person[1]) > 10]
    return result_data


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


if __name__ == '__main__':
    print(get_users_list())
