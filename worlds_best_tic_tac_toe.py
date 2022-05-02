"""CS 108 PROJECT

This project is a code which implements a tic-tac-toe. However, the generic version (3x3) of the game
sounds too simple to replicate in Python, so this tic tac toe haves more components.
The tic-tac-toe game has a 3x3 box window inside the main 3x3 box.
Hence, there are 9 tic tac toe in total and there are 81 boxes in total.

This was taken from a simple 3X3 code from the GUIZERO book that can be found in https://lawsie.github.io/guizero/book/

@author: Hadong Park (hp55)
@date: Spring, 2022
"""
# Imports ---------------
from guizero import App, Box, PushButton, Text, Window

# Functions -------------

class Canvas:
    """This class implements a starting canvas as an object"""
    
    def __init__(self, app):
        """Inicializes the width, height, and rules of the GUI canvas"""
        UNIT = 700
        CONTROL_UNIT = 500
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT
        app.info('rules',"1) Instructions: To open a new game click any of the button which opens a new window \n X STARTS THE FIRST GAME. After that, whoever played last in the previous game plays second in the new game. \n 2)After a game, you have to individually close a tic tac toe pop up window (if you desire). \n 3)Once inidivdual game is done that cell/box is now disable. \n 4)If you draw exit the window and zero points are distributed \n 5)First to 3 wins! :)")

        

def essential_board():     #function idea from https://lawsie.github.io/guizero/book/
    """Draws the 9 boxes of the tic tac toe in the main app"""
    score_x = ' '
    main_board = [None, None, None, None, None, None, None, None, None]
    for i in range(9):
            main_button = PushButton(board, text =' ', grid=[i%3, i//3], width=3, command=open_window, args=[i])
            main_board[i] = main_button
    return main_board        
        

def clear_board(window):  #This was my own idea for the own tic tac toe but is similar to the essential board which was taken from https://lawsie.github.io/guizero/book/
    """Draws individual tic tac toe boards (9 boxes) in each individual window"""
    new_board = [None, None, None, None, None, None, None, None, None]
    for i in range(9):
            button = PushButton(window, text="", grid=[i%3, i//3], width=3, command=choose_square, args=[i, new_board])
            new_board[i] = button
    return new_board

def choose_square_in_main(i, board):     #from https://lawsie.github.io/guizero/book/
    """This function disables the button in the main board once a game is done"""
    board[i].text = turn
    board[i].disable()
    
def choose_square(i, board):   #from https://lawsie.github.io/guizero/book/
    """This function draws the X's and O's depending on the player who is playing, and also disables the button after is clicked"""
    board[i].text = turn
    board[i].disable()
    toggle_player()
    check_win(i,board, message)
    
def toggle_player():     #taken from https://lawsie.github.io/guizero/book/
    """This Function toggles between the players"""
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
        message.value = "It is your turn, bro " 

def check_win(i, board, message):
    """This function determines who wins and checks the winner either vertical, horizontal, or diagonal"""
    global score_X
    global score_O
    winner = None
 
    question = ' '
    # Vertical lines check win 
    if (board[0].text == board[1].text == board[2].text) and board[2].text in ["X", "O"]:
        winner = board[0]
    elif (board[3].text == board[4].text == board[5].text) and board[5].text in ["X", "O"]:
        winner = board[3]
    elif (board[6].text == board[7].text == board[8].text) and board[8].text in ["X", "O"]:
        winner = board[6]
        
    # Horizontal lines check win
    elif (board[0].text == board[3].text == board[6].text) and board[6].text in ["X", "O"]:
        winner = board[0]
    elif (board[1].text == board[4].text == board[7].text) and board[7].text in ["X", "O"]:
        winner = board[1]
    elif (board[2].text == board[5].text == board[8].text) and board[8].text in ["X", "O"]:
        winner = board[2]
        
        # Diagonals check win 
    elif (board[0].text == board[4].text == board[8].text) and board[8].text in ["X", "O"]:
        winner = board[0]
    elif (board[2].text == board[4].text == board[6].text) and board[6].text in ["X", "O"]:
        winner = board[2]
 
        
        
    if winner is not None:
        question = app.question("question", "Who won? (answer must be exactly submitted as: 'X' or 'O'  ", initial_value=None)
        message.value = winner.text + " won last game, keep it up!"

        board[0].disable()
        board[1].disable()
        board[2].disable()
        board[3].disable()
        board[4].disable()
        board[5].disable()
        board[6].disable()
        board[7].disable()
        board[8].disable()
        
        


    if (question == "X" ):
        score_X += 1
        keep_track1.clear()
        keep_track1.append(score_X)
    elif (question == "O" ):
        score_O += 1
        keep_track2.clear()
        keep_track2.append(score_O)
    elif (question == 'draw'):
        score_X += 1
        keep_track1.clear()
        keep_track1.append(score_X)
        score_O += 1
        keep_track2.clear()
        keep_track2.append(score_O)        

# message that exits game 
    if (score_X == 3):
        score_X += 1
        keep_track2.clear()
        keep_track2.append(score_O)
        app.info('info','Game Over ' + winner.text + " wins!")
        exit()
    elif (score_O == 3):
        score_O += 1
        keep_track2.clear()
        keep_track2.append(score_O)
        app.info('info','Game Over' + winner.text + " wins!")
        exit()
 
      

def open_window(arg):
    """This function is used so a new window could be open. It is called when one of the buttons are clicked in the main app tic tac toe"""
    windows[arg].show()
    


    

# Variables -------------
turn = "X"
score_X = 0
score_O = 0
# App -------------------
app = App("Tic tac toe")
board = Box(app, layout="grid")
windows = [Window(app, layout="grid"),  Window(app, layout="grid"), Window(app, layout="grid"), Window(app, layout="grid"), Window(app, layout="grid"), Window(app, layout="grid"), Window(app, layout="grid"), Window(app, layout="grid"), Window(app, layout="grid")]

box2 = Box(app)
scoreboard_x = Text(box2, text= "score x:  ", size = 16, color = "blue")
keep_track1 = Text(box2)
scoreboard_o = Text(app, text= "score o:  ", size = 16, color = "red")
keep_track2 = Text(box2)

for window in windows:
    window.hide()
    clear_board(window)

squares = essential_board()
# board_squares = clear_board()

message = Text(app, text="Remember, X goes first. May the best tic tac toer win!" )
Canvas(app)
app.display()


  