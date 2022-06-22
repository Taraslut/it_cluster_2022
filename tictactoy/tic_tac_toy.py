def input_data():
    data = input("Enter row and column numbers to fix spot:").split(" ")
    if len(data) != 2:
        raise KeyError("Error! Input data have to be:1 2")
    # print(data)
    return int(data[0]) - 1, int(data[1]) - 1


def show_board(b, player):
    print(f"Player {player} move")
    for row in b:
        for i in row:
            print(f"{i} ", end="")
        print()


def show_winner(player):
    print(f"Player {player} win!!!")


def show_error(msg):
    print(msg)


def is_win(board, player):
    # check rows for win combination
    for row_i in range(len(board)):
        win = True
        for col_i in range(len(board)):
            if board[row_i][col_i] != player:
                win = False
        if win:
            return True

    # check cols for win combination
    for col_i in range(len(board)):
        win = True
        for row_i in range(len(board)):
            if board[row_i][col_i] != player:
                win = False
        if win:
            return True

    # check diagonal for win combination
    win = True
    for i in range(len(board)):
        if board[i][i] != player:
            win = False
    if win:
        return True

    # todo check diagonal 2 for win combination
    return False


def change_player(active_player):
    if "O" == active_player:
        return "X"
    return "O"


def main():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    active_player = "O"
    while True:
        try:
            show_board(board, active_player)

            row, col = input_data()

            if board[row][col] == "-":
                board[row][col] = active_player
            else:
                show_error("The spot is taken. Choose another")
                continue

            if is_win(board, active_player):
                show_winner(active_player)
                break

            active_player = change_player(active_player)
        except KeyError as e:
            show_error(e)

        except IndexError:
            show_error("Indexes must be in range 1-3")

        except Exception:
            show_error("Ups!")


if __name__ == '__main__':
    main()
