from pprint import pprint 

def some():
    pass


def main():
    bingo_numbers: list = []
    bingo_boards: list = []

    with open('./2021/python/day4/input.txt', 'r') as file:
        bingo_numbers = [ int(num) for num in file.readline().rstrip().split(',') ]
        
        current_board = []
        board_line = 1
        for line in file.read().splitlines():
            if not line:
                continue
            current_board.append([ int(num) for num in line.split() ])
            board_line += 1
            if board_line == 6:
                bingo_boards.append(current_board)
                current_board = []
                board_line = 1
        
        #bingo_boards = [ [ int(num) for num in line.rstrip().split()] for line in file if line != '' ]
        # current_board: list = []
        # for line in file:
        #     current_board.append([ int(num) for num in line.rstrip().split() ])
        #     bingo_boards.append(current_board)

    print(bingo_numbers)
    pprint(bingo_boards[0])
    pprint(bingo_boards[-1])


if __name__ == '__main__':
    main()