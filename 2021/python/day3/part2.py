data_test = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


def calc_oxygen_generator_rating(binary_numbers: list[str]) -> str:

    possibilities = binary_numbers.copy()

    for index in range(len(possibilities)):
        bits_at_current_index = [num[index] for num in possibilities]
        ones = bits_at_current_index.count('1')
        zeroes = bits_at_current_index.count('0')
        most_used = '1' if ones >= zeroes else '0'
        possibilities = [ num for num in possibilities if num[index] == most_used ]
        if len(possibilities) == 1:
            return possibilities[0]

def calc_co2_scrubber_rating(binary_numbers: list[str]) -> str:

    possibilities = binary_numbers.copy()

    for index in range(len(possibilities)):
        bits_at_current_index = [num[index] for num in possibilities]
        ones = bits_at_current_index.count('1')
        zeroes = bits_at_current_index.count('0')
        least_used = '0' if ones >= zeroes else '1'
        possibilities = [ num for num in possibilities if num[index] == least_used ]
        if len(possibilities) == 1:
            return possibilities[0]


def main():

    data_real = []
    with open('./2021/python/day3/input.txt', 'r') as file:
        data_real = file.read().splitlines()

    test_oxygen_generator_rating = calc_oxygen_generator_rating(data_test)
    real_oxygen_generator_rating = calc_oxygen_generator_rating(data_real)

    test_co2_scrubber_rating = calc_co2_scrubber_rating(data_test)
    real_co2_scrubber_rating = calc_co2_scrubber_rating(data_real)
    
    life_support_rating = int(real_oxygen_generator_rating, 2) * int(real_co2_scrubber_rating, 2)
    
    print(f"{test_oxygen_generator_rating=}")
    print(f"{real_oxygen_generator_rating=}")
    
    print(f"{test_co2_scrubber_rating=}")
    print(f"{real_co2_scrubber_rating=}")

    print(f"{life_support_rating=}")


main()