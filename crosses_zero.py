# tic- tac -toe
print('Игра крестики-нолики для двух игроков. Выбор хода происходит путем выбора числа от 1 до 9')


win = False
board = ['-' for _ in range(9)]

#функция отрисовки доски
def draw_board(board):

    row1 = f"   0 1 2\n"
    row2 = f"0 {board[0]} {board[1]} {board[2]}\n"
    row3 = f"1 {board[3]} {board[4]} {board[5]}\n"
    row4 = f"2 {board[6]} {board[7]} {board[8]}\n"

    print(row1,row2,row3,row4)

# проверка выигрыша
def check_win(board):
    win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
    for each in win_comb:
        if board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] != '-':
            return board[each[0]]
    return False

current_player = 'X'
#начинаем процесс
while not win:
    draw_board(board)

    try:
        move_x = int(input(f'Ход {current_player}. Введите число от 1 до 9: '))
        if move_x < 1 or move_x > 9:
            raise Exception("Неверный ввод. Введите число от 1 до 9")
        index = move_x - 1

        #проверка того что ячейка свободна

        if board[index] == '-':
            board[index] = current_player
        else:
            print("Ячейка занята. Сделайте другой ход")
            continue

        # проверка победы
        winner = check_win(board)
        if winner:
            draw_board(board)
            print(f"Игрок {winner} победил")
            win = True

        if '-' not in board:
            print('Ничья')
            win = True
        current_player = 'O' if current_player == 'X' else 'X'

    except ValueError:
        print('Вводить допустимо только числа от 1 до 9')

















