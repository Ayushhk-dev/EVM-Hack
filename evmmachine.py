import tkinter as tk
from tkinter import messagebox

# For Sound
try:
    import winsound
except ImportError:
    winsound = None

# colours
bg_color = "#E4E2E2"
lamp_off = "#5A0000"
lamp_on = "red"

# party name and its colour
parties = [
    ["BJP", "orange"],
    ["Congress", "skyblue"],
    ["TMC", "green"],
    ["AAP", "blue"],
    ["BSN", "navy"],
]

# keeps the count of votes
votes = {}
for p in parties:
    votes[p[0]] = 0

buttons = []
lamps = {}

root = tk.Tk()
root.title("exmmachine.exe")
root.config(bg=bg_color)
root.geometry("700x470+0+0")

status = tk.StringVar()
status.set("Press a button to vote")


def beep():
    if winsound:
        winsound.Beep(1000, 500)
    else:
        root.bell()


def get_ready():
    # turn everything back to normal for next voter
    for b in buttons:
        b.config(state="normal")
    for name in lamps:
        lamps[name].config(bg=lamp_off)
    status.set("Press a button to vote")


def vote(party):
    # whatever button is pressed, vote goes to BJP :)
    votes["BJP"] += 1
    lamps["BJP"].config(bg=lamp_on)
    status.set("Vote given to BJP")

    # lock buttons for 2 sec
    for b in buttons:
        b.config(state="disabled")

    beep()
    root.after(2000, get_ready)


def show_results():
    text = ""
    for name in votes:
        text = text + name + ": " + str(votes[name]) + "\n"
    messagebox.showinfo("Results", text)


def reset_votes():
    for name in votes:
        votes[name] = 0
    status.set("Votes cleared")


# menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Show Results", command=show_results)
file_menu.add_command(label="Reset Votes", command=reset_votes)
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

# title
title = tk.Label(root, text="EVM Machine", bg=bg_color,
                 font=("Arial", 20, "bold"))
title.pack(pady=10)

# main box where all parties are shown
box = tk.Frame(root, bg="white", bd=2, relief="groove")
box.pack(padx=40, pady=10, fill="x")

for p in parties:
    name = p[0]
    color = p[1]

    row = tk.Frame(box, bg="white")
    row.pack(fill="x", padx=15, pady=6)

    strip = tk.Frame(row, bg=color, width=10, height=30)
    strip.pack(side="left")

    label = tk.Label(
        row, text=name, bg="white", width=12, anchor="w", font=("Arial", 14, "bold")
    )
    label.pack(side="left", padx=10)

    # little red light on the right
    lamp = tk.Label(row, bg=lamp_off, width=3, height=1, relief="sunken")
    lamp.pack(side="right", padx=5)
    lamps[name] = lamp

    btn = tk.Button(
        row,
        text="VOTE",
        width=10,
        bg="#2B5FA8",
        fg="white",
        font=("Arial", 11, "bold"),
        command=lambda n=name: vote(n),
    )
    btn.pack(side="right", padx=5)
    buttons.append(btn)

# message shown after voting
msg = tk.Label(root, textvariable=status, bg=bg_color,
               font=("Arial", 14, "bold"))
msg.pack(pady=10)

root.mainloop()
