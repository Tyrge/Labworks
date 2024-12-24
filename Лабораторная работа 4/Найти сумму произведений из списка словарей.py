# TODO решите задачу
import json


def task() -> float:
    input_file = "input.json"
    with open(input_file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

        list_values = [item["score"] * item["weight"] for item in json_data]
        return sum(list_values)


print(f'{task():.3f}')
