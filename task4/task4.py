#импорт модуля
import sys

#создание функции для открытия файла, считывания и сортировки в список
def read_numbers(file_path):
    with open(file_path, 'r') as file:
        return sorted(int(line.strip()) for line in file)

#функция для нахождения медианы, возвращает сумму абсолютных разниц между каждым числом и медианой
def min_moves_to_equal(nums):
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

#проверка программы, вывод минимального количество ходов
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py numbers.txt")
        sys.exit(1)

    nums = read_numbers(sys.argv[1])
    print(min_moves_to_equal(nums))

