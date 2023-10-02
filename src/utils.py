import json
import os
from datetime import datetime


FOLDER = '/skypro_cw3'  # папка проекта
FILENAME = '/data/operations.json'  # файл данных json
PATH = os.path.relpath(FILENAME, FOLDER)  # путь к json файлу в проекте


def get_operations(path_file):
    """
    Возвращает список операций из файла
    """
    with open(file=path_file, encoding='utf-8', mode='r') as file:
        operation_list = json.load(file)
    return operation_list


def get_sorted_list(ilist):
    """
    Возвращает отсортированный по дате список операций по убыванию
    :param ilist: список операций
    :return: отсортированный список
    """
    sorted_list = sorted(ilist, key=lambda d: d.get('date', '0000-00-00T00:00:00.000000'), reverse=True)
    return sorted_list


def get_last_executed(ilist):
    """
    Возвращает список исполненных операций 'EXECUTED' по переводу
    """
    executed = []
    for i in ilist:
        if "EXECUTED" in i.values()\
                and "from" in i.keys():
            executed.append(i)
    return executed


def get_last_five_operations(ilist):
    """
    Пять операций начальных из отсортированного списка
    :param ilist: список исполненных и отсортированных по убыванию операций
    :return: список из пяти операций
    """
    ilist_five = ilist[:5]
    return ilist_five


def get_formatted_operation(ioperation: dict):
    """
    Формирует список из выводимых полей для операции
    :param ioperation: словарь с данными операции
    :return: список с полями
    """
    elist = []
    if ioperation:
        operation_date = ioperation['date']
        idatetime = datetime.fromisoformat(operation_date)
        description = ioperation['description']
        operation_from = ioperation['from'].split()
        operation_to = ioperation['to'].split()
        amount = ioperation['operationAmount']['amount']
        currency = ioperation['operationAmount']['currency']['name']
        # дата
        elist.append(idatetime.strftime("%d.%m.%Y"))
        # описание
        elist.append(description)
        # отправитель
        if len(operation_from) == 2:
            elist.append(operation_from[0])
            elist.append(operation_from[1])
        else:
            elist.append(' '.join(operation_from[:-1]))
            elist.append(operation_from[-1])
        # получатель
        if len(operation_to) == 2:
            elist.append(operation_to[0])
            elist.append(operation_to[1])
        else:
            elist.append(' '.join(operation_to[:-1]))
            elist.append(operation_to[-1])
        # сумма и валюта
        elist.append(amount)
        elist.append(currency)
    return elist


def hide_account_number(inumber: str):
    """
    Скрыть полный номер счета по заданному алгоритму ** XXXX
    :param inumber: номер счета
    :return: скрытый номер счета
    """
    enumber = []
    if inumber:
        enumber.append('**')
        sliced_number = slice(16, 20)
        enumber.append(inumber[sliced_number])
    return ''.join(enumber)


def hide_card_number(icard: str):
    """
    Скрыть номер карты по заданному алгоритму XXXX XX** **** XXXX
    :param icard: номер карты
    :return: скрытый номер карты
    """
    ecard = []
    if icard:
        ecard.append(icard[slice(0, 4)])
        ecard.append(''.join([icard[slice(4, 6)], '**']))
        ecard.append('****')
        ecard.append(icard[slice(12, 16)])
    return ' '.join(ecard)
