import tkinter as tk

def set_tile(row, column):
    global curr_player

    if gameOver:
        return

    if board[row][column]["text"] != "":
        # already taken spot
        return

    board[row][column]["text"] = curr_player  # mark the board

    if curr_player == playero:  # switch player
        curr_player = playerx
    else:
        curr_player = playero

    label["text"] = curr_player + "'s turn"

    # check winner
    check_winner()

def check_winner():
    global turns, gameOver
    turns += 1

    # check for horizontal all three rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            gameOver = True
            return

    # checks for vertical all three rows
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            gameOver = True
            return

    # check for diagonal
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        gameOver = True
        return

    # check for anti-diagonal
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        gameOver = True
        return

    if turns == 9:
        gameOver = True
        label.config(text="Tie!", foreground=color_yellow)

def new_game():
    global turns, gameOver, curr_player

    turns = 0
    gameOver = False
    curr_player = playerx

    label.config(text=curr_player + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", background=color_gray, foreground=color_blue)

# game setup
playerx = "X"
playero = "O"
curr_player = playerx

color_gray = "#343434"
color_blue = "#4584b6"
color_light_gray = "#646464"
color_yellow = "#FFDE57"

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

turns = 0
gameOver = False

# window setup

window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_gray, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Consolas", 50, "bold"),
                                       background=color_gray, foreground=color_blue, width=4, height=1,
                                       command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tk.Button(frame, text="Restart", font=("Consolas", 50, "bold"),
                   background=color_gray, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# center window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
