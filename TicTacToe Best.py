# Tic Tac Toe

# Global Variables

board = ['-','-','-',
         '-','-','-',
         '-','-','-']

winner = ''

game_still_running = True


# Functions

# Display the Board
def show_board():
    print("\n\t"+board[0]+"|"+board[1]+"|"+board[2]+"\t\t"+"1 | 2 | 3"+"\n"+
          "\t"+board[3] + "|" + board[4] + "|" + board[5]+"\t\t"+"4 | 5 | 6"+"\n"+
          "\t"+board[6] + "|" + board[7] + "|" + board[8]+"\t\t"+"7 | 8 | 9")

    # 1 | 2 | 3
    # 4 | 5 | 6
    # 7 | 8 | 9

    return

# Restart
def re():
    retry = str(input("\nDo you want to restart? (Y/N) :"))
    retry = retry.lower()
    if retry == ('y' or 'yes'):
        print("Yes")
        startGame()
    elif retry == ('n' or 'no'):
        print("No")
        exit()
    else:
        print("Invalid input, choose again.")
        re()
    re()
    return

# Display winner
def display_winner():
    global winner
    show_board()
    print("\n"+winner+" is the winner")
    print("Congratulations")
    def re():
        retry = str(input("\nDo you want to restart? (Y/N) :"))
        retry = retry.lower()
        if retry == ('y' or 'yes'):
            print("Yes")
            startGame()
        elif retry == ('n' or 'no'):
            print("No")
            exit()
        else:
            print("Invalid input, choose again.")
            re()
    re()
    return

def xTurn():
    show_board()
    choice = int(input("\n\tEnter 1-9 :"))
    choice -= 1
    if board[choice] == 'X' or board[choice] == 'O':
        print("Place occupied, choose another spot.")
        xTurn()
    else:
        board[choice] = 'X'
    return

def oTurn():
    show_board()
    choice = int(input("\n\tEnter 1-9 :"))
    choice -= 1
    if board[choice] == 'X' or board[choice] == 'O':
        print("Place occupied, choose another spot.")
        oTurn()
    else:
        board[choice] = 'O'
    return

# Check for winner
def check_for_winner():
    check_rows()
    check_columns()
    check_diagonals()
    return

# Check Rows
def check_rows():
    global winner, game_still_running
    if game_still_running == True:
        if (board[0] == board[1] == board[2]) and (board[0] != '-'):
            winner = board[0]
            game_still_running = False
        if (board[3] == board[4] == board[5]) and (board[3] != '-'):
            winner = board[3]
            game_still_running = False
        if (board[6] == board[7] == board[8]) and (board[6] != '-'):
            winner = board[6]
            game_still_running = False
    else:
        display_winner()
    return


# Check Columns
def check_columns():
    global winner, game_still_running
    if game_still_running == True:
        if (board[0] == board[3] == board[6]) and (board[0] != '-'):
            winner = board[0]
            game_still_running = False
        if (board[1] == board[4] == board[7]) and (board[1] != '-'):
            winner = board[4]
            game_still_running = False
        if (board[2] == board[5] == board[8]) and (board[2] != '-'):
            winner = board[5]
            game_still_running = False
    else:
        display_winner()

    return


# Check Diagonals
def check_diagonals():
    global winner, game_still_running
    if game_still_running == True:
        if (board[0] == board[4] == board[8]) and (board[0] != '-'):
            winner = board[0]
            game_still_running = False
        if (board[6] == board[4] == board[2]) and (board[6] != '-'):
            winner = board[4]
            game_still_running = False
    else:
        display_winner()


# Check for Tie
def check_for_tie():
    global game_still_running
    while '-' not in board:
        game_still_running = False
        print("\n\tThe Game is a draw.")
        exit()
    return

# Main Game Manager - controls everything
def startGame():
    check_for_winner()
    check_for_tie()
    xTurn()
    check_for_winner()
    check_for_tie()
    oTurn()
    check_for_winner()
    check_for_tie()
    startGame()
    return

startGame()

# Display winner
def display_winner():
    global winner
    print("\n"+winner+"is the winner")
    print("Congratulations")
    def re():
        retry = str(input("\nDo you want to restart? (Y/N) :"))
        retry = retry.lower()
        if retry == ('y' or 'yes'):
            startGame()
        elif retry == ('n' or 'no'):
            exit()
        else:
            print("Invalid input, choose again.")
            re()
    re()
    return









