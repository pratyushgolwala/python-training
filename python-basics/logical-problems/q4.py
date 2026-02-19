# import random
# moves = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
# used_moves = set()
# board = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(" ")
#     board.append(row)

# for row in board:
#     for cell in row:
#         print(cell, end=" ")
#     print()
    

# turns = 0
# print(f"enter your choice from {moves}")
# chance = input("Your turn:").split(",")
# while turns < 9 :
#     if chance[0].isdigit() and chance[1].isdigit():
#         row = int(chance[0])
#         col = int(chance[1])
#         if (row, col) in moves and (row, col) not in used_moves:
#             board[row][col] = "X"
#             used_moves.add((row, col))
#             turns += 1
#         else:
#             print("Invalid move. Please try again.")
#             continue
#     else:
#         print("Please enter valid numbers for row and column.")
#         continue
    
#     comp_row = random.randint(0, 2)
#     comp_col = random.randint(0, 2)
#     while (comp_row, comp_col) in used_moves:
#         comp_row = random.randint(0, 2)
#         comp_col = random.randint(0, 2)
    
#     board[comp_row][comp_col] = "O"
#     used_moves.add((comp_row, comp_col))
#     turns += 1
    
#     for row in board:
#         for cell in row:
#             print(cell, end=" ")
#         print() 

#     if turns < 9:
#         print(f"enter your choice from {moves - used_moves}")
#         chance = input().split(",") 

# for i in range(3):
#     for j in range(3):
#         if board[i][j] == board[i][(j+1)%3] == board[i][(j+2)%3] != " ":
#             print(f"{board[i][j]} wins!")
#             exit()
        


import random

moves = {(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)}

used_moves = set()

# Create board
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(symbol):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
    
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == symbol:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    
    return False


turns = 0
print_board()

while turns < 9:

    # -------- Player Turn --------
    print(f"Available moves: {moves - used_moves}")
    chance = input("Enter row,col: ").split(",")

    if len(chance) != 2 or not chance[0].isdigit() or not chance[1].isdigit():
        print("Invalid input. Try again.")
        continue

    row, col = int(chance[0]), int(chance[1])

    if (row, col) not in moves or (row, col) in used_moves:
        print("Invalid move. Try again.")
        continue

    board[row][col] = "X"
    used_moves.add((row, col))
    turns += 1
    print_board()

    if check_winner("X"):
        print("🎉 You win!")
        break

    if turns == 9:
        break

    # -------- Computer Turn --------
    comp_move = random.choice(list(moves - used_moves))
    comp_row, comp_col = comp_move

    board[comp_row][comp_col] = "O"
    used_moves.add(comp_move)
    turns += 1

    print("Computer chose:", comp_move)
    print_board()

    if check_winner("O"):
        print("🤖 Computer wins!")
        break

# -------- Draw Condition --------
if turns == 9 and not check_winner("X") and not check_winner("O"):
    print("It's a draw!")





