# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    mylist = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        csv_readed = csv.DictReader(csv_file)
        for rows in csv_readed:
            mylist.append(rows)
    ...  # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(mylist, indent=4))
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
