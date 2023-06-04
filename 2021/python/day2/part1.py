data_test = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def calc_pos(instructions: list[str]) -> dict:
    pos = {
        'horizontal': 0,
        'depth': 0
    }
    for task in instructions:
        name, num = task.split()
        if name == 'up':
            pos['depth'] += int(num)
        if name == 'down':
            pos['depth'] -= int(num)
        if name == 'forward':
            pos['horizontal'] += int(num)

    return pos

data_real = []
with open('./2021/python/day2/input.txt', 'r') as lines:
    data_real = list(lines)

result_test = calc_pos(data_test)
result_real = calc_pos(data_real)

print(result_test)
print(result_real)