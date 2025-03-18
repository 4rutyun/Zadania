import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def fill_values(tests, values_dict):
    for test in tests:
        test_id = test.get('id')
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        # Проверяем оба возможных ключа для вложенных тестов
        if 'tests' in test:
            fill_values(test['tests'], values_dict)
        elif 'values' in test:
            fill_values(test['values'], values_dict)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Загрузка данных из файлов JSON
    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    # Создание словаря для быстрого поиска значений по id
    values_dict = {item['id']: item['value'] for item in values_data['values']}

    # Заполнение значений в tests
    fill_values(tests_data['tests'], values_dict)

    # Запись значений в report.json
    with open(report_file, 'w') as file:
        json.dump(tests_data, file, indent=4)


