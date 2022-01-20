import random

def rotate(board):
    return list(map(list, zip(*board[::-1])))

def moveElements(board, dir):
    for i in range(dir): board = rotate(board)
    for i in range(len(board)):
        temp = []
        for j in board[i]:
            if j != '.':
                temp.append(j)
        temp += ['.'] * board[i].count('.') 
        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1] and temp[j] != '.' and temp[j + 1] != '.':
                temp[j] = str(2 * int(temp[j]))
                move.score += int(temp[j])
                temp[j + 1] = '.'
        board[i] = []
        for j in temp:
            if j != '.':
                board[i].append(j)
        board[i] += ['.'] * temp.count('.')
    for i in range(4 - dir): board = rotate(board)
    return board


def emptySlot(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                return (i, j, 0)
    return (-1, -1, 1)

def addNumbers(board):
    num = random.randint(1, 2) * 2
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    lost = 0
    if board[x][y] != '.':
        x, y, lost = findemptySlot(board)
    if not lost: board[x][y] = str(num)
    return (board, lost)


def printBoard(board):
    print ("\n")
    for i in range(len(board)):
        res = "\t\t"
        for j in range(len(board[i])):
            for _ in range(5 - len(board[i][j])): res += " "
            res += board[i][j] + " "
        print (res)
        print ("\n")
    return 0


def start():
    print ("\nWelcome to the 2048 game")
    print ("Combine numbers to get a maximum score.\nYou can move left, right, top or bottom.\n The game ends when you get 2048")
    

    board = [['.', '.', '2', '.'],
            ['.', '4', '.', '.'],
            ['.', '.', '.', '2'],
            ['2', '.', '2', '4']]

    direction = {'L': 0, 'B': 1, 'R': 2, 'T': 3, 'X': 4}

    printBoard(board)

    losing = 0
    
    moveElements.score = 0
    
    while True:
        tmp = input("\nTo continue, Press L for left, R for right, T for top, B for bottom or\nPress X to end the game.\n")
        if tmp in ["R", "r", "L", "l", "T", "t", "B", "b", "X", "x"]:
            dir = direction[tmp.upper()]
            if dir == 4:
                print ("\nFinal score: " + str(move.score))
                break
            else:
                board = move(board, dir)
                board, losing = addNumbers(board)
                printBoard(board)
                if losing:
                    print ("\nGame Over")
                    print ("Final score: " + str(move.score))
                    break
                print ("\nCurrent score: " + str(move.score))
        else:
            print ("\nInvalid direction")
    return 0


start()
