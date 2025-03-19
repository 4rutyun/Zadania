#импорт модуля sys
import sys

#создание функции для считывания данных в файлах
def read_data(file_path, is_circle=False):
    with open(file_path, 'r') as file:
        if is_circle:
            return tuple(map(float, file.read().strip().split()))
        return [tuple(map(float, line.strip().split())) for line in file]

#создание функции для вычисления расстояния
def determine_position(x0, y0, r, x, y):
    distance_squared = (x - x0) ** 2 + (y - y0) ** 2
    return 1 if distance_squared < r ** 2 else 0 if distance_squared == r ** 2 else 2

#проверка программы, считывание данных и вывод
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py circle.txt dot.txt")
        sys.exit(1)

    x0, y0, r = read_data(sys.argv[1], is_circle=True)
    points = read_data(sys.argv[2])

    for x, y in points:
        print(determine_position(x0, y0, r, x, y))
