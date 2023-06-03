data_test: list = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]
data_real: list = []

with open('./2021/python/day1/numbers.txt', 'r') as numbers:
    lines = numbers.read().splitlines() # .readlines()
    data_real = list(map(int, lines))


def count_increase_bigwindow(data: list) -> int:
    return sum(sum(data[(i+1):(i+4)]) > sum(data[i:(i+3)]) for i in range(len(data) - 3))



print(f'Testdata: {count_increase_bigwindow(data_test)}')
print(f'Realdata: {count_increase_bigwindow(data_real)}')
