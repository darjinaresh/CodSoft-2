from tkinter import *
import random


comp_score = 0
player_score = 0

outcomes = {
    "rock": {"rock": 1, "paper": 0, "scissors": 2},
    "paper": {"rock": 2, "paper": 1, "scissors": 0},
    "scissors": {"rock": 0, "paper": 2, "scissors": 1}
}



def converted_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"


def outcome_handler(user_choice):
    global comp_score
    global player_score
    random_number = random.randint(1, 3)
    computer_choice = converted_outcome(random_number)
    outcome = outcomes[user_choice][computer_choice]

    player_choice_label.config(fg="red", text="Player Choice : " + str(user_choice))
    computer_choice_label.config(fg="green", text="Computer Choice : " + str(computer_choice))

    if outcome == 2:
        player_score = player_score + 2
        player_score_label.config(text="Player : " + str(player_score))
        outcome_label.config(fg="blue", text="Outcome : Player Won ")

    elif outcome == 0:
        comp_score = comp_score + 2
        computer_score_label.config(text="Computer : " + str(comp_score))
        outcome_label.config(fg="blue", text="Outcome : Computer Won")

    elif outcome == 1:
        player_score = player_score + 1
        comp_score = comp_score + 1
        player_score_label.config(text="Player : " + str(player_score))
        computer_score_label.config(text="Computer : " + str(comp_score))
        outcome_label.config(fg="blue", text="Outcome : Draw")



root = Tk()
root.title("ROCK-PAPER-SCISSORS")

Font = ("times new roman", 15, "bold")

label1 = Label(root, text="ROCK-PAPER-SCISSORS", font=Font, fg="dark green")
label1.grid(row=0, sticky=N, pady=10, padx=200)

label2 = Label(root, text="GAME START NOW....", font=Font, fg="dark green")
label2.grid(row=1, sticky=N)

player_score_label = Label(root, text="Player : 0", font=Font)
player_score_label.grid(row=2, sticky=W)

computer_score_label = Label(root, text="Computer : 0", font=Font)
computer_score_label.grid(row=2, sticky=E)

player_choice_label = Label(root, font=Font)
player_choice_label.grid(row=3, sticky=W)

computer_choice_label = Label(root, font=Font)
computer_choice_label.grid(row=3, sticky=E)

outcome_label = Label(root, font=Font)
outcome_label.grid(row=3, sticky=N)


button = Button(root, text="Rock", width=15, command=lambda: outcome_handler("rock"))
button.grid(row=4, sticky=W, padx=5, pady=5)

button = Button(root, text="Paper", width=15, command=lambda: outcome_handler("paper"))
button.grid(row=4, sticky=N, pady=5)

button = Button(root, text="Scissors", width=15, command=lambda: outcome_handler("scissors"))
button.grid(row=4, sticky=E, padx=5,pady=5)

button = Button(root, text="© 2024 Naresh. All rights reserved.", font=Font)
button.grid(pady=17)


root.mainloop()
