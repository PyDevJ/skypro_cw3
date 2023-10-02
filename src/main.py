import utils


def main():
    """Вывод на экран последних 5 выполненных операций"""
    # считывает данные из файла
    operations = utils.get_operations(utils.PATH)
    # операции сортируются по дате
    sorted_operations = utils.get_sorted_list(operations)
    # формируется список из успешных операций
    executed_operations = utils.get_last_executed(sorted_operations)
    # формируется список из пяти порядковых операций
    last_five_operations = utils.get_last_five_operations(executed_operations)
    # вывод записей в заданном формате
    for operation in last_five_operations:
        formatted_operation = utils.get_formatted_operation(operation)
        if formatted_operation[2] == 'Счет': hided_acc_from = utils.hide_account_number(formatted_operation[3])
        else:
            hided_acc_from = utils.hide_card_number(formatted_operation[3])
        if formatted_operation[4] == 'Счет': hided_acc_to = utils.hide_account_number(formatted_operation[5])
        else:
            hided_acc_to = utils.hide_card_number(formatted_operation[5])
        print(f"{formatted_operation[0]} {formatted_operation[1]}\n"
              f"{formatted_operation[2]} {hided_acc_from} -> {formatted_operation[4]} {hided_acc_to}\n"
              f"{formatted_operation[6]} {formatted_operation[7]}" "\n")


if __name__ == '__main__':
    main()
