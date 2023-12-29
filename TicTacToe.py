def display(board):
    print(f"\t{board[0][0]:^}\t|\t{board[0][1]:^}\t|\t{board[0][2]:^}")
    print(f"\t{board[1][0]:^}\t|\t{board[1][1]:^}\t|\t{board[1][2]:^}")
    print(f"\t{board[2][0]:^}\t|\t{board[2][1]:^}\t|\t{board[2][2]:^}")

def index_board(iBoard,pnumber):
    for index_i, tpl in enumerate(iBoard):
        if pnumber in tpl:
            j = tpl.index(pnumber)
            i = index_i
    return i,j
    

def players():
    player1 = input("Player 1, select symbol ('X' or 'O'): ").upper()
    while player1 not in ["X", "O"]:
        player1 = input("Invalid input. Please select either 'X' or 'O': ").upper()

    if player1.lower() == "x":
        player2 = "o"
    else:
        player2 = "x"
    return player1,player2

def board_update(p,iBoard,board,number):
    i,j = index_board(iBoard,number)
    board[i][j] = p.upper()
    return board

def players_choice():
    choice = int(input("Enter a number to place your symbol (1-9): "))
    while choice not in range(1, 10):
        choice = int(input("Invalid input. Please enter a number between 1-9: "))
    return choice

def valid(answers,player,iBoard,board):
    choice = "Wrong"
    while (choice not in answers):
        choice = players_choice()
        if choice not in answers:
            print("This position is already in use")
    board = board_update(player,iBoard,board,choice)
    answers.remove(choice)
    return answers,board


def game_on(iBoard,board):
    valid_answers = [1,2,3,4,5,6,7,8,9]
    player1,player2 = players()
    display(board)

    while (len(valid_answers) != 0):
        print(valid_answers)
        print("****** Player 1's turn  ******")
        valid_answers,board = valid(valid_answers,player1,iBoard,board)
        display(board)
        if has_winner(board):
            print("Player1 wins!")
            break
        elif (len(valid_answers) == 0) and (not has_winner(board)):
            print("It's a tie!")
            display(board)
            break

        print("****** Player 2's turn  ******") 
        valid_answers,board = valid(valid_answers,player2,iBoard,board)
        display(board)
        if has_winner(board):
            print("Player 2 wins!")
            break
        elif (len(valid_answers) == 0) and (not has_winner(board)):
            print("It's a tie!")
            display(board)
            break
        
def has_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True

    return False

def play_game():
    intendedBoard  = [[1,2,3],[4,5,6],[7,8,9]]
    display(intendedBoard)
    cleanBoard = [["","",""],["","",""],["","",""]]
    game_on(intendedBoard,cleanBoard)

play_game()

answer = "wrong"
while answer not in ["Y","N"]:
    answer = input("would you like to play again? (press Y/N)").upper()
while (answer =="Y"):
        play_game()
        answer = "wrong"
        while answer not in ["Y","N"]:
            answer = input("would you like to play again? (press Y/N)").upper()
    
else:
    print("It was nice to play with you")