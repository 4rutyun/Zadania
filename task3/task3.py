#импорт модулей
import json
import sys

#открытие и загрузка данных из файла json
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

#заполнение полей value
def fill_values(tests, values_dict):
    for test in tests:
        if (test_id := test.get('id')) in values_dict:
            test['value'] = values_dict[test_id]
        for key in ('tests', 'values'):
            if key in test:
                fill_values(test[key], values_dict)

#проверка программы, загрузка данных из values и tests, запись данных в report
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_data = load_json(sys.argv[1])
    tests_data = load_json(sys.argv[2])

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_dict)

    with open(sys.argv[3], 'w') as file:
        json.dump(tests_data, file, indent=4)


