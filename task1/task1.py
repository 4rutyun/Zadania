#импорт модуля sys
import sys

#создание функции кругового массива
def circular_array_path(n, m):
    path = []
    index = 0
    while True:
        path.append(index + 1)
        index = (index + m - 1) % n
        if index == 0:
            break
    return path

#проверка программы, вывод результата
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task1.py n m")
        sys.exit(1)

    n, m = map(int, sys.argv[1:3])
    print("".join(map(str, circular_array_path(n, m))))

