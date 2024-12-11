def find_common_participants(first_list, second_list, separator=','):
    same = []
    first_list = first_list.split(separator)
    second_list = second_list.split(separator)
    for name in first_list:
        if name in second_list:
            same.append(name)
    return same


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
identical = find_common_participants(participants_first_group, participants_second_group, '|')
print(identical)
# TODO Провеьте работу функции с разделителем отличным от запятой
