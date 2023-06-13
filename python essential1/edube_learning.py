'''hat_list = [1, 2, 3, 4, 5]
print(f'Lista initiala este: {hat_list}')
print(f'Lungimea listei initiale este: {len(hat_list)}')
print('---------------')
# inlocuieste nr de la jumatatea listei cu un nr luat de la tst
jum =int(len(hat_list)/2)
hat_list[jum] = int(input('Introduceti numarul dorit: '))
print(f'Lista actuala este: {hat_list}')
print(f'Lungimea listei actuale este: {len(hat_list)}')
print('---------------')

#sterge ultimul nr din lista
del hat_list[-1]
print(f'Lista actuala este: {hat_list}')
print(f'Lungimea listei actuale este: {len(hat_list)}')
print('---------------')

# afiseaza pe ecran lungimea listei
print(f'Lungimea listei actuale este: {len(hat_list)}')
'''
#creaza o lista goala
'''beatles =[]
#adauga 3 nume in lista
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print(f'The list is: {beatles}')
#adauga 2 nume in lista
for i in range(1):
    beatles.append('Stu Sutcliffe')
    beatles.append('Pete Best')
print(beatles)
#sterge ultimele 2 nume din lista

for i in range(2):
    del beatles[-1]
print(beatles)
# adauga la inceputul liste un nume
beatles.insert(0, 'Ringo Starr')
print(beatles)
print(len(beatles))
'''
# list = [1, 2, 4, 4, 4, 1, 5, 2, 4, 7, 8]
# numere_unice = []
# for i in range(0, len(list)):
#     if list.count(list[i]) ==1:
#         numere_unice.append(list[i])
# print(numere_unice)

#Your task is to write and test a function which takes one argument (a year)
#and returns True if the year is a leap year, or False otherwise.
#
# import calendar
# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True
#     else:
#         return False
# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
# 	yr = test_data[i]
# 	print(yr,"->",end="")
# 	result = is_year_leap(yr)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")

'''Your task is to write and test a function which takes two arguments (a year and a month) and 
returns the number of days for the given month/year pair (while only February is sensitive to the year value,
your function should be universal).'''
# def days_in_months(year, month):
#     days = calendar.monthrange(year, month)[1]
#     return days
#
# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr =test_years[i]
#     mo = test_months[i]
#     print(f'{yr}, {mo} :  ')
#     result = days_in_months(yr, mo)
#     if result == test_results[i]:
#         print('ok')
#     else:
#         print('failed')

#Your task is to write and test a function which takes three arguments
#(a year, a month, and a day of the month) and returns the corresponding day of the year,
#or returns None if any of the arguments is invalid.
# def day_of_year(year, month, day):
#     if not(1 <= month <= 12) or not(1 <= day <= 31):
#         return None

# def is_prime(num):
#     nr_prime = [2, 3, 5, 7]
#
#     for i in range(0, len(nr_prime)):
#         if num == nr_prime[i]:
#             return True
#         if num % nr_prime[i] != 0:
#             return True
#         else:
#             return False
#
#
# for i in range(1,20):
#     if is_prime(i+1):
#         print(i+1, end =' ')
#
# print()

#write a simple program which pretends to play tic-tac-toe with the user.

import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if any player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

# Function to make the computer's move
def make_computer_move(board, computer, player):
    # Check if computer can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = computer
                if check_winner(board, computer):
                    return

                # Reset the move
                board[row][col] = ""

    # Check if player can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = player
                if check_winner(board, player):
                    board[row][col] = computer
                    return

                # Reset the move
                board[row][col] = ""

    # If no winning move is possible, make a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "":
            board[row][col] = computer
            return

# Function to play the game
def play_game():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player = "X"
    computer = "O"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if player == "X":
            print("Your turn (X)")
            while True:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if board[row][col] == "":
                    break
                else:
                    print("That position is already occupied. Try again.")
            board[row][col] = player
        else:
            print("Computer's turn (O)")
            make_computer_move(board, computer, player)

        print_board(board)

        if check_winner(board, player):
            print("Congratulations! You won!")
            break
        elif check_winner(board, computer):
            print("Sorry! You lost!")
            break
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

    print("Game Over")

# Start the game
play_game()



