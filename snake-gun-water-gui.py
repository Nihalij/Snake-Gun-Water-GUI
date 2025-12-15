from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

# -------------------- MAIN WINDOW -------------------- 
win = Tk() 
win.title("Snake Gun Water Game 🎮")
win.geometry("700x700")
win.minsize(600, 600) 
win.maxsize(800, 800) 
# -------------------- ICON -------------------- 
icon_img = Image.open( r"C:\Users\aadis\OneDrive\New folder\Pictures\Screenshots\Screenshot 2025-12-14 215455.png" ) 
icon = ImageTk.PhotoImage(icon_img) 
win.iconphoto(False, icon)

 # -------------------- BACKGROUND IMAGE -------------------- 
bg_img = Image.open( r"C:\Users\aadis\OneDrive\New folder\Pictures\Screenshots\Screenshot 2025-12-14 220545.png" ) 
bg_img = bg_img.resize((800, 800))
bg = ImageTk.PhotoImage(bg_img)
bg_label = Label(win, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# -------------------- TITLE -------------------- 
title = Label( win, text="Snake-Gun-Water!!", font=("Arial", 28, "bold"), fg="black", bg="#d0efbd" ) 
title.place(relx=0.5, y=20, anchor="center") 

subtitle = Label( win, text="Survive the Ultimate Logic Game!", font=("Arial", 14), fg="black", bg="#c7f2ac" ) 
subtitle.place(relx=0.5, y=70, anchor="center")

# -------------------- GAME FRAME --------------------
game_frame = Frame(win, bg="#f6fcf2", bd=2, relief="ridge")
game_frame.place(relx=0.5, y=350, anchor="n")

# -------------------- USER SECTION --------------------
Label(game_frame, text="USER:",font=("Arial", 10, "bold"),fg="#1b5e20", bg="#f6fcf2").grid(row=0, column=0, pady=5)

user_box = ttk.Combobox(game_frame,values=["Snake (S)", "Gun (G)", "Water (W)"],state="readonly",width=15)
user_box.grid(row=0, column=1, padx=10)

# -------------------- COMPUTER SECTION --------------------
Label(game_frame, text="COMPUTER:",font=("Arial", 10, "bold"),fg="#1b5e20", bg="#f6fcf2").grid(row=1, column=0, pady=5)

computer_text = Label(game_frame,text="",font=("Arial", 10),bg="#f6fcf2",fg="#1b5e20")
computer_text.grid(row=1, column=1)

# -------------------- LOGIC FUNCTIONS --------------------
def short(x):
    return x[-2]  

def winner(user, computer):
    if user == computer:
        return "It's a Draw 🤝"
    elif (
        (user == "S" and computer == "W") or
        (user == "G" and computer == "S") or
        (user == "W" and computer == "G")
    ):
        return "You Win 🎉"
    else:
        return "Computer Wins 😢"

def play():
    if user_box.get() == "":
        result_label.config(text="Please select a choice")
        return

    user_choice = short(user_box.get())
    comp_choice_full = np.random.choice(["Snake (S)", "Gun (G)", "Water (W)"])
    comp_choice = short(comp_choice_full)

    computer_text.config(text=comp_choice_full)
    result = winner(user_choice, comp_choice)
    result_label.config(text=result)

# -------------------- PLAY BUTTON --------------------
play_btn = Button(game_frame,text="PLAY",command=play,font=("Arial", 12, "bold"),bg="#4C983B",fg="white",cursor="hand2")
play_btn.grid(row=2, column=0, columnspan=2, pady=10)

# -------------------- RESULT LABEL --------------------
result_label = Label(game_frame,text="",font=("Arial", 14, "bold"),fg="#1b5e20",bg="#f6fcf2")
result_label.grid(row=3, column=0, columnspan=2, pady=10)


win.mainloop()
