"""Stone Paper Scissor Game"""
import random
from tkinter import END, Button, Label, Text, Tk

from PIL import Image, ImageTk

window = Tk()
window.title("Stone Paper Scissor")

image = Image.open("sps.jpg")
image.thumbnail((500, 500), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = Label(image=photo)
label_image.grid(column=15, row=0)

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""


def choice_to_number(choice):
    """Convert choice to number"""
    rps = {"scissor": 0, "paper": 1, "stone": 2}
    return rps[choice]


def number_to_choice(number):
    """Convert number to choice"""
    rps = {0: "scissor", 1: "paper", 2: "stone"}
    return rps[number]


def random_computer_choice():
    """Choose randomly for computer"""
    return random.choice(["scissor", "paper", "stone"])


def result(human_choice, comp_choice):
    """Return the winner"""
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if user == comp:
        print("Tie")
    elif (user - comp) % 3 == 1:
        print("Sorry !! Computer wins")
        COMP_SCORE += 1
    else:
        print("Congrats !! You win")
        USER_SCORE += 1
    text_area = Text(master=window, height=4, width=28)
    text_area.grid(column=15, row=4)
    answer = "Your Choice : {uc} \nComputer's Choice : {cc} \nYour Score : {u} \nComputer's Score : {c}".format(
        uc=USER_CHOICE,
        cc=COMP_CHOICE,
        u=USER_SCORE,
        c=COMP_SCORE,
        font=("arial", 24, "bold"),
    )
    text_area.insert(END, answer)


def stone():
    """When stone is selected"""
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "stone"
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    """When paper is selected"""
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "paper"
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissor():
    """When scissor is selected"""
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "scissor"
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


Button(
    window,
    text="Stone",
    bg="orange",
    command=stone,
    height=1,
    width=6,
    font=("arial", 15, "bold"),
).grid(column=14, row=2)

Button(
    window,
    text="Paper",
    bg="pink",
    command=paper,
    height=1,
    width=6,
    font=("arial", 15, "bold"),
).grid(column=15, row=2)

Button(
    window,
    text="Scissor",
    bg="powder blue",
    command=scissor,
    height=1,
    width=6,
    font=("arial", 15, "bold"),
).grid(column=16, row=2)

window.mainloop()
