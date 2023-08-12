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


def calc_common_bit(binary_numbers: list[str]) -> str:

    max_bit_count = len(binary_numbers)
    half_max_bit_count = max_bit_count / 2

    bit_count = {} # "1": 0,"2": 0,"3": 0,"4": 0,"5": 0,

    for binary_number in binary_numbers:
        for index, bit in enumerate(binary_number):
            bit_count[str(index+1)] = bit_count.get(str(index+1), 0) + int(bit)


    returnStr: str = ''
    for index in range(len(binary_numbers[0])):
        returnStr += '1' if bit_count[str(index+1)] > half_max_bit_count else '0'
    return returnStr


def reverse_binary_number(bits: str) -> str:
    return "".join(["1" if bit == "0" else "0" for bit in bits])



def main():
    common_bit = calc_common_bit(data_test)
    print(common_bit)

    rev = reverse_binary_number(common_bit)
    print(rev)
    print( int(common_bit, 2) * int(rev, 2) )


    data_real = []
    with open('./2021/python/day3/input.txt', 'r') as file:
        data_real = file.read().splitlines()

    common_bit = calc_common_bit(data_real)
    print(common_bit)

    rev = reverse_binary_number(common_bit)
    print(rev)
    print( int(common_bit, 2) * int(rev, 2) )


main()