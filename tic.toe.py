import random
computer = "X"
User = "O"
stuff = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def displayboard(stuff):
    for row in stuff:
        print("-------------------------------------------------------------------------")
        print("|", row[0], "|", row[1], "|", row[2], "|", sep="           ")
        print("-------------------------------------------------------------------------")
def updateboard():
    while True:
        # This controls the whole game.
        # Computer turn → User turn → Computer turn → User turn →
        # Computer move
        while True:
            move = random.randint(1, 9)
            row = (move - 1) // 3
            col = (move - 1) % 3
            if stuff[row][col] not in [computer, User]:
                stuff[row][col] = computer
                break
        displayboard(stuff)
        if win_check():
            # exit 
            return
        # User move
        while True:
            try:
                move = int(input("Enter move: "))

                if move < 1 or move > 9:
                    print("Matrix has positions from 1 to 9")
                    continue
                row = (move - 1) // 3
                col = (move - 1) % 3
                if stuff[row][col] in [computer, User]:
                    print("This position is already occupied. Choose another.")
                    continue
                stuff[row][col] = User
                break
            except ValueError:
                print("INVALID COMMAND. Please enter a number.")
        displayboard(stuff)
        if win_check():
            return
def win_check():
    # Horizontal
    if stuff[0][0] == stuff[0][1] == stuff[0][2] and stuff[0][0] in [computer, User]:
        if stuff[0][0] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True

    elif stuff[1][0] == stuff[1][1] == stuff[1][2] and stuff[1][0] in [computer, User]:
        if stuff[1][0] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True

    elif stuff[2][0] == stuff[2][1] == stuff[2][2] and stuff[2][0] in [computer, User]:
        if stuff[2][0] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True

    # Vertical
    elif stuff[0][0] == stuff[1][0] == stuff[2][0] and stuff[0][0] in [computer, User]:
        if stuff[0][0] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True

    elif stuff[0][1] == stuff[1][1] == stuff[2][1] and stuff[0][1] in [computer, User]:
        if stuff[0][1] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True
    elif stuff[0][2] == stuff[1][2] == stuff[2][2] and stuff[0][2] in [computer, User]:
        if stuff[0][2] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True
    # Diagonal
    elif stuff[0][0] == stuff[1][1] == stuff[2][2] and stuff[0][0] in [computer, User]:
        if stuff[0][0] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True
    elif stuff[0][2] == stuff[1][1] == stuff[2][0] and stuff[0][2] in [computer, User]:
        if stuff[0][2] == computer:
            print("Computer Wins")
        else:
            print("User Wins")
        return True
    # Draw
    board_full = True
    for row in stuff:
        for position in row:
            if position not in [computer, User]:
                board_full = False
    if board_full:
        print("Draw")
        return True
    return False
displayboard(stuff)
updateboard()