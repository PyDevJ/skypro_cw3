from src.utils import (get_operations,
                       get_sorted_list,
                       get_last_executed,
                       get_last_five_operations,
                       get_formatted_operation,
                       hide_account_number,
                       hide_card_number
                       )


def test_file_is_exist():
    """
    Проверка считывания данных из файла
    :return:
    """
    assert get_operations('test/../data/operations.json')[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_get_sorted_list():
    """
    Проверка сортируется ли список по дате
    :return:
    """
    unsorted_list = [{"id": 1, "date": "2018-06-30T02:08:58.425572"},
                     {"id": 2, "date": "2019-07-03T18:35:29.512364"},
                     {"id": 3, "date": "2019-08-26T10:50:58.294041"}]
    sorted_list = [{"id": 3, "date": "2019-08-26T10:50:58.294041"},
                   {"id": 2, "date": "2019-07-03T18:35:29.512364"},
                   {"id": 1, "date": "2018-06-30T02:08:58.425572"}]
    assert get_sorted_list(unsorted_list) == sorted_list
    assert get_sorted_list([]) == []


def test_last_operations():
    """
    Проверка формирования списка выполненных операций
    :return:
    """
    full_list = [
        {"id": 1, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 2, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 3, "state": "CANCELED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 4, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 5, "state": "CANCELED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 6, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 7, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 8, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 9, "state": "EXECUTED", "date": "", "": "", "to": "", "description": "", "operationAmount": ""}]
    last_list = [
        {"id": 1, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 2, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 4, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 6, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 7, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""},
        {"id": 8, "state": "EXECUTED", "date": "", "from": "", "to": "", "description": "", "operationAmount": ""}]
    assert get_last_executed(full_list) == last_list
    assert get_last_executed([]) == []


def test_get_last_five_operations():
    """
    Проверка формирования из отсортированного списка 5 порядковых операций
    """
    ilist = [1, 2, 3, 4, 5, 6, 7]
    assert get_last_five_operations(ilist) == [1, 2, 3, 4, 5]
    assert get_last_five_operations(ilist) != [1, 4, 3, 7]


def test_get_formatted_operation():
    """
    Проверка вернуть список на основе полей словаря
    :return:
    """
    operation1 = {"id": 441945886,
                  "state": "EXECUTED",
                  "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {
                      "amount": "31957.58",
                      "currency": {
                          "name": "руб.",
                          "code": "RUB"
                      }
                  },
                  "description": "Перевод организации",
                  "from": "Maestro 1596837868705199",
                  "to": "Счет 64686473678894779589"}
    formatted_operation1 = ['26.08.2019',
                            'Перевод организации',
                            'Maestro',
                            '1596837868705199',
                            'Счет',
                            '64686473678894779589',
                            '31957.58',
                            'руб.']
    assert get_formatted_operation(operation1) == formatted_operation1
    operation2 = {"id": 895315941,
                  "state": "EXECUTED",
                  "date": "2018-08-19T04:27:37.904916",
                  "operationAmount": {
                      "amount": "56883.54",
                      "currency": {
                          "name": "USD",
                          "code": "USD"
                      }
                  },
                  "description": "Перевод с карты на карту",
                  "from": "Visa Classic 6831982476737658",
                  "to": "Visa Platinum 8990922113665229"}
    formatted_operation2 = ['19.08.2018',
                            'Перевод с карты на карту',
                            'Visa Classic',
                            '6831982476737658',
                            'Visa Platinum',
                            '8990922113665229',
                            '56883.54',
                            'USD']
    assert get_formatted_operation(operation2) == formatted_operation2
    assert get_formatted_operation({}) == []


def test_hide_number():
    """
    Проверка скрыть номер счета
    :return:
    """
    assert hide_account_number('64686473678894779589') == '**9589'
    assert hide_account_number('') == ''


def test_hide_card():
    """
    Проверка скрыть номер карты
    :return:
    """
    assert hide_card_number('1596837868705199') == '1596 83** **** 5199'
    assert hide_card_number('') == ''
