import sys

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x0 = float(file.readline().strip())
        y0 = float(file.readline().strip())
        r = float(file.readline().strip())
    return x0, y0, r

def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def determine_position(x0, y0, r, x, y):
    distance_squared = (x - x0) ** 2 + (y - y0) ** 2
    if distance_squared < r ** 2:
        return 1  # Внутри
    elif distance_squared == r ** 2:
        return 0  # На круге
    else:
        return 2  # Снаружи

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py circle.txt dot.txt")
        sys.exit(1)

    circle_file = sys.argv[1]
    dot_file = sys.argv[2]

    x0, y0, r = read_circle_data(circle_file)
    points = read_points(dot_file)

    for x, y in points:
        position = determine_position(x0, y0, r, x, y)
        print(position)

