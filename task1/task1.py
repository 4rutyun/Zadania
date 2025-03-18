import sys

def circular_array_path(n, m):
    # Создаем круговой массив от 1 до n
    circular_array = list(range(1, n + 1))
    path = []
    index = 0

    # Пока не вернемся к первому элементу
    while True:
        # Добавляем начальный элемент интервала в путь
        path.append(circular_array[index])
        # Вычисляем следующий индекс, начиная с последнего элемента текущего интервала
        index = (index + m - 1) % n
        # Если вернулись к первому элементу, выходим из цикла
        if index == 0:
            break

    return path

if __name__ == "__main__":
    # Получаем аргументы командной строки
    if len(sys.argv) != 3:
        print("Usage: python task1.py n m")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    # Получаем путь и выводим его
    path = circular_array_path(n, m)
    print("".join(map(str, path)))
