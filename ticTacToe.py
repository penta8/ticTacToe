# new board


def newBoard():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board


def isBoardFull(board):
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
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
    if player == 'x':
        return 'y'
    else:
        return 'x'


def win(board, pl):
    return (board[0][0] == pl and board[0][1] == pl and board[0][2] == pl) or \
           (board[0][0] == pl and board[1][0] == pl and board[2][0] == pl) or \
           (board[0][0] == pl and board[1][1] == pl and board[2][2] == pl) or \
           (board[1][0] == pl and board[1][1] == pl and board[1][2] == pl) or \
           (board[2][0] == pl and board[2][1] == pl and board[2][2] == pl) or \
           (board[0][1] == pl and board[1][1] == pl and board[2][1] == pl) or \
           (board[0][2] == pl and board[1][2] == pl and board[2][2] == pl) or \
           (board[0][2] == pl and board[1][1] == pl and board[2][0] == pl)


board = newBoard()
player = 'x'
while not isBoardFull(board):
    showBoard(board)
    print('Select a position in the format LetterNumber ' +\
          'for example A1 not being used: ', end='')
    position = input()
    if usedPosition(position, board):
        print('This position is already used...')
        continue

    updateBoard(position, player, board)
    if win(board, player):
        print('Congratulations ' + player + ' you won!!!')
        showBoard(board)
        break

    player = changePlayer(player)
