import random as r
import time
import sys
global cpu_board
cpu_board = []
def calculate_score(board):
    score = 0
    for i in range(0, 25, 5):
        if board[i] == "*" and board[i+1] == "*" and board[i+2] == "*" and board[i+3] == "*" and board[i+4] == "*":
            score += 1
    for i in range(5):
        if board[i] == "*" and board[i+5] == "*" and board[i+10] == "*" and board[i+15] == "*" and board[i+20] == "*":
            score += 1
    if board[0] == "*" and board[6] == "*" and board[12] == "*" and board[18] == "*" and board[24] == "*":
        score += 1
    if board[4] == "*" and board[8] == "*" and board[12] == "*" and board[16] == "*" and board[20] == "*":
        score += 1
        
    return score
def user_progress_bar(board):
    score = calculate_score(board)
    if score == 0:
        return "* * * * *"
    if score == 1:
        return "B * * * *"
    if score == 2:
        return "B I * * *"
    if score == 3:
        return "B I N * *"
    if score == 4:
        return "B I N G *"
    if score >= 5:
        return "B I N G O"    
def cpu_progress_bar(board):
    score = calculate_score(board)
    if score == 0:
        return "* * * * *"
    if score == 1:
        return "B * * * *"
    if score == 2:
        return "B I * * *"
    if score == 3:
        return "B I N * *"
    if score == 4:
        return "B I N G *"
    if score >= 5:
        return "B I N G O"
def winner(user_progress_bar, user, cpu_progress_bar, cpu_board):
    if user_progress_bar(user) == "B I N G O" or cpu_progress_bar(cpu_board) == "B I N G O":
        print("The winner is....")
        time.sleep(2)
        if user_progress_bar(user) == "B I N G O" and cpu_progress_bar(cpu_board) == "B I N G O":
            print("It's a dramatic Tie match!")
        elif user_progress_bar(user) == "B I N G O":
            print("The winner is User")
        else:
            print("The winner is C.P.U")    
        sys.exit()
user = []
opt = input("Would u like a randomly shuffled list or would u enter your own choice?(y/n): ")
match opt.lower():
    case "y":
        user = list(range(1, 26))
        r.shuffle(user)
    case "n":
        for i in range(25):
            num = int(input(f"Enter element number {i + 1}: "))
            user.append(num)
        print("\nYour 5x5 grid layout:")
        for i in range(len(user)):
            if i % 5 == 0 and i != 0:
                print()
            print(user[i], end=" ")
        print()
print("\033[H\033[J", end="")
time.sleep(1)
cpu_board = list(range(1, 26))
r.shuffle(cpu_board)
bingo = "*BINGO*"
print("\033[H\033[J", end="")
gone = []
while True:
    for i in range(len(user)):
        if i % 5 == 0 and i != 0:
            print()
        print(f"{str(user[i]):>2}", end=" ")
            
    print(f"\n\nYour progress : {user_progress_bar(user)}")
    print(f"C.P.U Progress: {cpu_progress_bar(cpu_board)}")
    
    while True:
        try:
            inp = int(input("\n\nEnter a number of your choice: "))
            if inp > 0 and inp < 26 and inp not in gone:
                break
            else:
                print("Try again (must be 1-25 and not chosen yet)...")
        except ValueError:
            print("Please enter a valid number.")

    gone.append(inp)

    for i in range(len(user)):
        if inp == user[i]:
            user[i] = "*"
            
    for i in range(len(cpu_board)):
        if inp == cpu_board[i]:
            cpu_board[i] = "*"

    winner(user_progress_bar, user, cpu_progress_bar, cpu_board)

    print("\nThe cpu is choosing....... ")
    time.sleep(1.5)
    
    cpu_choice = r.randint(1, 25)
    while cpu_choice in gone:
        cpu_choice = r.randint(1, 25)        
    gone.append(cpu_choice)
    
    print(f"The CPU chose: {cpu_choice}")
    time.sleep(1.5)

    for i in range(len(cpu_board)):
        if cpu_choice == cpu_board[i]:
            cpu_board[i] = "*"
    for i in range(len(user)):
        if cpu_choice == user[i]:
            user[i] = "*"
            
    print("\033[H\033[J", end="")
    winner(user_progress_bar, user, cpu_progress_bar, cpu_board)
