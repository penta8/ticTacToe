import os


def newBoard():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]


def isBoardFull(board):
    for row in board:
        for column in row:
            if column == ' ':
                return False
    return True


def showBoard(board):
    print('  A B C')
    for row in range(3):
        print(str(row + 1) + ' ', end='')
        for column in range(3):
            if column == 2:
                endLine = '\n'
            else:
                endLine = '|'
            print(board[row][column] + endLine, end='')
        if row < 2:
            print('  - - -')


def usedPosition(position, board):
    row = position[0]
    if row == 'A':
        y = 0
    elif row == 'B':
        y = 1
    else:
        y = 2
    return board[int(position[1]) - 1][y] != ' '


def updateBoard(position, player, board):
    row = position[0]
    if row == 'A':
        y = 0
    elif row == 'B':
        y = 1
    else:
        y = 2
    board[int(position[1]) - 1][y] = player
    return board


def changePlayer(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def win(board, pl):
    return (board[0][0] == pl and ((board[0][1] == pl and board[0][2] == pl) or \
                                   (board[1][0] == pl and board[2][0] == pl) or \
                                   (board[1][1] == pl and board[2][2] == pl))) or \
           (board[1][0] == pl and board[1][1] == pl and board[1][2] == pl) or \
           (board[2][0] == pl and board[2][1] == pl and board[2][2] == pl) or \
           (board[0][1] == pl and board[1][1] == pl and board[2][1] == pl) or \
           (board[0][2] == pl and ((board[1][2] == pl and board[2][2] == pl) or \
                                   (board[1][1] == pl and board[2][0] == pl)))


def validPosition(pos):
    return pos in ['A1', 'B1', 'C1',
                   'A2', 'B2', 'C2',
                   'A3', 'B3', 'C3']


board = newBoard()
player = 'X'
while not isBoardFull(board):
    showBoard(board)
    print('PLAYER ' + player)
    print('Select a position in the format LetterNumber ' +\
          'for example A1 not being used: ', end='')
    position = input().upper()

    os.system('clear')
    if not validPosition(position):
        print('INVALID POSITION')
        continue

    if usedPosition(position, board):
        print('This position is already used...')
        continue

    updateBoard(position, player, board)
    if win(board, player):
        print('Congratulations ' + player + ' you won!!!')
        showBoard(board)
        break

    player = changePlayer(player)
