from helper import print_bord, try_to_move, is_board_completed

bord = [15, 14, 13, 12, 11, 10, 0, 8, 7, 6, 5, 4, 3, 1, 2, 9]

while not is_board_completed(bord):
    print(print_bord(bord))
    user_variant = int(input("Enter number to replace>"))
    bord = try_to_move(bord, user_variant)

print("YOU WIN!!!")

