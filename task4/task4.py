import sys

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py numbers.txt")
        sys.exit(1)

    numbers_file = sys.argv[1]
    nums = read_numbers(numbers_file)
    moves = min_moves_to_equal(nums)
    print(moves)
