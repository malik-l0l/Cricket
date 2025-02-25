"""
PROGRESS :-
> GUI layout      done!.
> buttons,colors  done!.
> score board     done!.
> add score       done!.
> out check       done!.
> SWITCH PLAYER   done!.
> win check       done!.
> game over       done!.
> play_again      done!.
> help button     done!.
"""

import random
from tkinter import *
from tkinter import messagebox

# ----- GLOBALS ------------
sum_computer = 0
sum_player = 0
computer_bats = False


# ----- END GLOBALS --------

# ---------------- METHODS ----------------------------------------------------------------------
def help():
    message = """
first,
player: bats
computer: balls

The player can press the number between [1-6] to bat and score.
The computer will choose any number between [1-6] and the ball.
if the number that player batted and computer balled is the same
results in 'PLAYER OUT'

then (after switching),
computer: bats
player: balls

The computer will choose any number between [1 and 6] to bat and score.
The player can press the number between [1-6] to ball.
If the number that the computer batted and the player balled is the same, it results in 'COMPUTER OUT'

If a player gets the computer 'OUT' before it scores more than the player, the player wins.
if the computer scores more than the player, the computer wins.
    """
    messagebox.showinfo('help', message)


def reset_game():
    sum_computer = 0
    sum_player = 0
    computer_bats = False

    display_player.config(text='')
    display_computer.config(text='')

    score_display_player.config(text='')
    score_display_computer.config(text='')

    info_label.config(text='Player bats first!.')


def check_score():
    """
    checks who won the game and asks if player wants to play-again.
    :return: None
    """
    global computer_bats, sum_computer, sum_player
    if sum_player == sum_computer:
        info_label.config(text=f"Its a tie for {sum_computer} runs")

    elif sum_player > sum_computer:
        info_label.config(text=f"Player wins for {sum_player} runs")

    else:
        info_label.config(text=f"Computer wins for {sum_computer} runs.")



    if messagebox.askyesno('GAME OVER', 'It  was  a  good  game. \n Wanna  Play  Again ??!.'):
        reset_game()
    else:
        window.destroy()


def button_press(p_num):
    """
    plays the event
    :param p_num: button pressed by player
    :return: None
    """
    global computer_bats, sum_computer, sum_player

    c_num = random.randint(1, 6)

    display_player.config(text=p_num)
    display_computer.config(text=c_num)

    if computer_bats:
        if c_num == p_num:
            # COMPUTER OUT
            score_display_computer.config(text=f'Computer\n"OUT"\n@ {sum_computer} runs.')
            check_score()

        else:
            # increment score of computer
            sum_computer += c_num
            score_display_computer.config(text=f"score : {sum_computer}")

            # if computer scores more than total runs of player(sum_player), game ends
            if sum_computer > sum_player:
                check_score()

    else:
        if p_num == c_num:
            # PLAYER OUT
            score_display_player.config(text=f'Player\n"OUT"\n@ {sum_player} runs.')

            # SWITCH PLAYER :
            # Player bats, Computer balls. -> Computer bats, Player balls.

            computer_bats = True
            info_label.config(text="Computer bats, player balls.")
            score_display_computer.config(text=sum_computer)

        else:
            # increment score of player
            sum_player += p_num
            score_display_player.config(text=f'score : {sum_player}')


# ---------------- END METHODS -----------------------------------------------------------------

# ================== MAIN WINDOW ===================================================
window = Tk()
window.title("Classic Cricket")
window.resizable(False, False)

frame1 = Frame(window)
frame1.pack()

frame = Frame(window, bd=3, relief=SUNKEN)
frame.pack()

frame2 = Frame(window)
frame2.pack()

# layer 1 -> text = player_label,computer_label
player_label = Label(frame1, font=("consoles", 20, "bold"), bg="#FFCE30", width=13, height=1,
                     relief=RAISED, bd=3, pady=5, text="Player")
player_label.grid(pady=0, row=0, column=0, padx=1)
computer_label = Label(frame1, font=("consoles", 20, "bold"), bg="#FFCE30", width=13, height=1,
                       relief=RAISED, bd=3, pady=5, text="Computer")
computer_label.grid(pady=0, row=0, column=1, padx=1)

# layer 2 -> display for pressed button
display_player = Label(frame1, font=("consoles", 20, "bold"), bg="#FFCE30", width=13, height=2,
                       relief=RAISED, bd=3, pady=7)
display_player.grid(pady=3, row=1, column=0, padx=1)
display_computer = Label(frame1, font=("consoles", 20, "bold"), bg="#FFCE30", width=13, height=2,
                         relief=RAISED, bd=3, pady=7)
display_computer.grid(pady=3, row=1, column=1, padx=1)

# layer 3 -> 6 Buttons for user interaction
Button(frame, text=1, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="dark violet",
       activeforeground="white", height=2, width=4, command=lambda: button_press(1)).grid(row=0, column=0)
Button(frame, text=2, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="indigo",
       activeforeground="white", height=2, width=4, command=lambda: button_press(2)).grid(row=0, column=1)
Button(frame, text=3, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="dark blue",
       activeforeground="white", height=2, width=4, command=lambda: button_press(3)).grid(row=0, column=2)

Button(frame, text=4, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="green",
       activeforeground="white", height=2, width=4, command=lambda: button_press(4)).grid(row=0, column=3)
Button(frame, text=5, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="yellow",
       activeforeground="white", height=2, width=4, command=lambda: button_press(5)).grid(row=0, column=4)
Button(frame, text=6, font=("Arial", 20, "bold"), bg="#FFD700", fg="black", activebackground="red",
       activeforeground="white", height=2, width=4, command=lambda: button_press(6)).grid(row=0, column=5)

# layer 4 -> score board
score_display_player = Label(frame2, font=("consoles", 20, "bold"), bg="#FFCE30", width=13, height=6,
                             relief=RAISED, bd=3, pady=7, text=sum_player)
score_display_player.grid(pady=3, row=1, column=0, padx=1)

score_display_computer = Label(frame2, font=("consoles", 20, "bold"), bg="#FFCE30", width=13, height=6,
                               relief=RAISED, bd=3, pady=7)
score_display_computer.grid(pady=3, row=1, column=1, padx=1)

# layer 5 -> info board and help button
info_label = Label(window, font=("consoles", 15, "bold"), bg="#FFCE30", width=29, height=1,
                   relief=SUNKEN, bd=3, pady=5, text="Player bats, computer balls")
info_label.pack(side=LEFT, padx=31, pady=2)

help_button = Button(window, text="?", font=("consoles", 14, "bold"), bg="#FFD700", fg="black",
                     activebackground="#FFD700", relief=RAISED,
                     activeforeground="green", height=1, width=3, command=help)
help_button.pack(side=LEFT, )

window.mainloop()
# ================== END MAIN WINDOW ===============================================
