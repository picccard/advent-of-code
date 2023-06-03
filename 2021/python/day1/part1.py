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


def count_increases_using_enumerate(data: list) -> int:
    count: int = 0

    if len(data) < 2:
        return count
    
    prevNum: int = data[0]
    
    for i, current_num in enumerate(data, start=1):
        if current_num > prevNum:
            count += 1
        prevNum = current_num

    return count

def count_increases_using_listcomp(data: list) -> int:
    return sum([data[i+1] > data[i] for i in range(len(data) - 1) ])


with open('./2021/python/day1/numbers.txt', 'r') as numbers:
    lines = numbers.read().splitlines() # .readlines()
    data_real = list(map(int, lines))

print(len(data_real))

print(f'Testdata: {count_increases_using_enumerate(data_test)}')
print(f'Realdata: {count_increases_using_enumerate(data_real)}')

print(f'Testdata: {count_increases_using_listcomp(data_test)}')
print(f'Realdata: {count_increases_using_listcomp(data_real)}')
