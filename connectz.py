

import os
import sys
import traceback


def check_file(file):
    if os.path.isfile(file):
        main(file)
    else:
        print(9)
        os._exit(0)


def generate_board(xyz):
    x = xyz[0]
    y = xyz[1]
    board = []
    for row in range(x):
        board.append([])
        for col in range(y):
            board[row].append('o')
    return board


def fill_board(board, xyz, col, turn):
    x = xyz[0]
    col = col - 1
    x_turn = 0
    for row in range(x):
        # print(row)
        if board[row][col] == 'o':
            break
        else:
            x_turn = x_turn + 1
    board[x_turn][col] = turn
    return(board, x_turn)

# Print who win based on check result
def who_win(result):
    if result == 'r':
        print(1)
        os._exit(0)
    elif result == 'y':
        print(2)
        os._exit(0)


def check_win(board, xyz, last_x, last_y):
    # check win vertically
    win_check = check_vertical(board, xyz, last_x, last_y)
    if not win_check:
        # check win horizontally
        win_check = check_horizontal(board, xyz, last_x, last_y)

    if not win_check:
        # check win diagonally
        win_check = check_diagonal(board, xyz, last_x, last_y)

    # print(win_check)
    return(win_check)


# Check board vertically starting from the last play
def check_vertical(board, xyz, last_x, last_y):
    win = xyz[2]
    cur_pos = board[last_x][last_y]
    count = 1
    # print(board[2][0])
    for num in range(1, win+1):
        if last_x - num >= 0:  # check if the next cell is valid to check
            if cur_pos == board[last_x - num][last_y]:
                count += 1
                if count == win:
                    # print(count)
                    # print(cur_pos)
                    return cur_pos
            else:
                return False
        else:
            return False


# Check board horizontally starting from the last play
def check_horizontal(board, xyz, last_x, last_y):
    y = xyz[1]
    win = xyz[2]
    cur_pos = board[last_x][last_y]
    count = 1
    for num in range(1, win+1):
        if last_y - num >= 0:  # Check if the next cell is valid to check
            if cur_pos == board[last_x][last_y - num]:
                count += 1
                if count == win:
                    # print(count)
                    # print(cur_pos)
                    return cur_pos
            else:
                break
        else:
            break

    # Check to the right direction
    for num in range(1, win+1):
        if last_y + num < y:  # Check if the next cell is valid to check
            if cur_pos == board[last_x][last_y + num]:
                count += 1
                if count == win:
                    # print(count)
                    # print(cur_pos)
                    return cur_pos
            else:
                return False
        else:
            return False



# Check board diagonally
def check_diagonal(board, xyz, last_x, last_y):
    x = xyz[0]
    y = xyz[1]
    win = xyz[2]
    cur_pos = board[last_x][last_y]
    count = 1
    # check down left first
    for num in range(1, win+1):
        row = last_x - num
        col = last_y - num
        if row >= 0 and col >= 0:  # Check if the next cell is valid to check
            if cur_pos == board[row][col]:
                count += 1
                if count == win:
                    print(count)
                    print(cur_pos)
                    return cur_pos
            else:
                break
        else:
            break

    # Check to down right direction
    for num in range(1, win+1):
        row = last_x - num
        col = last_y + num
        if row >= 0 and col < y:  # Check if the next cell is valid to check
            if cur_pos == board[row][col]:
                count += 1
                if count == win:
                    # print(count)
                    # print(cur_pos)
                    return cur_pos
            else:
                break
        else:
            break
    # Check to up right direction
    for num in range(1, win+1):
        row = last_x + num
        col = last_y + num
        if row < x and col < y:  # Check if the next cell is valid to check
            if cur_pos == board[row][col]:
                count += 1
                if count == win:
                    # print(count)
                    # print(cur_pos)
                    return cur_pos
            else:
                break
        else:
            break

    # Check to up left direction
    for num in range(1, win+1):
        row = last_x + num
        col = last_y - num
        if row < x and col >= 0:  # Check if the next cell is valid to check
            if cur_pos == board[row][col]:
                count += 1
                if count == win:
                    # print(count)
                    # print(cur_pos)
                    return cur_pos
            else:
                return False
        else:
            return False



# check if the row moves in range
def check_row(xyz, lines):
    x = xyz[0]
    y = xyz[1]
    mem = {}
    for line in range(1, y+1):
        mem[line] = 0

    for line in lines:
        if mem[line] >= x:
            print(5)
            os._exit(0)
        else:
            mem[line] = mem[line]+1
    # print(mem)
    return True



# check if the column moves in range
def check_column(xyz, lines):
    x = xyz[0]
    y = xyz[1]
    for line in lines:
        if line > y:
            print(6)
            os._exit(0)
    return True


def check_header(xyz):  # Check if the game is legel
    if xyz[0] < xyz[2] and xyz[1] < xyz[2]:
        print(7)
        os._exit(0)
    else:
        return True


# check if the come is draw or game is incomplete
def draw_or_incomplete(xyz, lines):
    x = xyz[0]
    y = xyz[1]
    moves = x * y  # get number of aviable moves
    if moves == len(lines):
        print(0)
        os._exit(0)
    else:
        print(3)
        os._exit(0)


def openfile(path, first_line=True):
    try:
        with open(path) as fp:
            if first_line:
                try:
                    line = fp.readline()  # read first line
                    line = line.strip()  # remove newline /n
                    xyz = line.split(" ")
                    xyz = [int(num) for num in xyz]
                    if check_header(xyz):  # check if the chage diementions are valid
                        return xyz
                except:
                    print(8)
                    os._exit(0)

            else:
                try:
                    lines = fp.readlines()
                    lines = [int(line.rstrip()) for line in lines[1:]]
                    # print(lines)
                    return(lines)
                except Exception as e:
                    print(7)
                    os._exit(0)
    except Exception as e:
        print(9)
        os._exit(0)


def print_board(board):
    for row in board[::-1]:  # print it reversed to visual the board with convenience
        print(row)


def main(filepath):
    # Read the first line paramenter only and check them
    xyz = openfile(filepath)
    if xyz:
        # Read the rest of the file if parameters are valid to process
        lines = openfile(filepath, first_line=False)  # Return list of moves

    check_col = check_column(xyz, lines)

    if check_col:
        check_ro = check_row(xyz, lines)
        if check_ro:
            board = generate_board(xyz)

    red = 'r'
    yel = 'y'
    turn = red

    if board:
        for col in range(len(lines)):
            data = fill_board(board, xyz, lines[col], turn)
            board = data[0]
            last_x = data[1]
            last_y = lines[col] - 1
            if turn == red:
                turn = yel
            elif turn == yel:
                turn = red
            check_result = check_win(board, xyz, last_x, last_y)
            if check_result:  # check illegal continue
                # print_board(board)
                try:
                    if lines[col+1]:
                        print(4)
                        os._exit(0)
                except:
                    who_win(check_result)

        draw_or_incomplete(xyz, lines)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(' connectz.py: Please enter only one argument!')

    elif len(sys.argv) == 2:
        check_file(sys.argv[1])

    else:
        filepath = input(" connectz.py: Provide one input file: ")
        path = filepath.split(' ')
        if len(path) == 1:
            check_file(path[0])