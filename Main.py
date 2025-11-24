from tkinter import *  # type: ignore
from tkinter import ttk
from tabs.QdrtcTab import create_quadratic_tab
from tabs.AbsltTab import create_absolute_tab
from tabs.SqrtTab import create_sqrt_tab
from tabs.RtnlTab import create_rtnl_tab
from utils import set_format

window = Tk()
window.geometry("900x720")
window.resizable(False, False)
window.title("Equation Solver")
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background='#676767')

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

home = Frame(notebook)
notebook.add(home,text=" | Home | ")
home.config(background='#999999')

create_quadratic_tab(notebook, window)
create_absolute_tab(notebook, window)
create_sqrt_tab(notebook, window)
create_rtnl_tab(notebook, window)

Result_Format = ['Fractions', 'Decimals']

format_var = StringVar(value="Decimals")

def update_output_format():
    set_format(format_var.get())
    print(f"Output format set to: {format_var.get()}")

format_frame = Frame(home,
                     relief=RAISED,
                     border=16,
                     padx=16,
                     pady=8)
format_frame.place(relx=0.4, y=20)

format_label = Label(format_frame,
                     text="Result Format",
                     font=('Comic Sans MS', 12))
format_label.pack()

for index, format_option in enumerate(Result_Format):
    radiobutton = Radiobutton(format_frame,
                     text=format_option,
                     variable=format_var,
                     value=format_option,
                     command=update_output_format,
                     font=('Comic Sans MS', 12))
    radiobutton.pack()

HelloLabel = Label(home,
                   text="Equation Solver\n\nCreated by: Adam Haddach\n\nSelect a tab to get started.",
                   bg='#eeeeee',
                   font=('Comic Sans MS', 24),
                   relief=RAISED,
                   border=32,
                   padx=16,
                   pady=16,
                   justify=CENTER,
                   highlightbackground='#444444',
                   highlightcolor='#888888',
                   highlightthickness=4)
HelloLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

easter_egg_found = False
bonus_tab_added = 0

def found_easter_egg(event):
    easter_egg_found = True
    print("Easter Egg Activated!")
    MessageBox = Toplevel(window)
    MessageBox.geometry("400x250")
    MessageBox.title("Easter Egg")
    MessageLabel = Label(MessageBox, text="Congratulations!\nYou've found\nthe Easter Egg!", font=('Comic Sans MS', 24), padx=20, pady=20)
    MessageLabel.pack()
    CloseButton = Button(MessageBox, text="Close", command=MessageBox.destroy)
    CloseButton.pack(pady=10)
    global bonus_tab_added
    if bonus_tab_added == 0:
        def bonus_hint(event):
            MessageBox = Toplevel(window)
            MessageBox.title("Bonus Hint")
            MessageBox.geometry("300x150")
            MessageLabel = Label(MessageBox, text="B36", font=('Comic Sans MS', 24), padx=20, pady=20)
            MessageLabel.pack()
            CloseButton = Button(MessageBox, text="Close", command=MessageBox.destroy)
            CloseButton.pack(pady=10)
    Bonus = Frame(notebook)
    notebook.add(Bonus,text=" | Bonus | ")
    Bonus.config(background='#999999')
    BonusLabel = Label(Bonus,
                       text="18 1012010 13726",
                       bg='#eeeeee',
                       font=('Comic Sans MS', 24),
                       relief=RAISED,
                       border=32,
                       padx=16,
                       pady=16,
                       justify=CENTER,
                       highlightbackground='#444444',
                       highlightcolor='#888888',
                       highlightthickness=4)
    BonusLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
    window.bind("<F1>", bonus_hint)
    bonus_tab_added = 1

easter_egg_sequence = ["<Up>", "<Up>", "<Down>", "<Down>", "<Left>", "<Right>", "<Left>", "<Right>", "b", "a", "<Return>"]
easter_egg_progress = []

def track_easter_egg(event):
    key = event.keysym.lower()
    if key == "backspace":
        easter_egg_progress.clear()
        print("Sequence reset manually.")
        return
    mapped = f"<{key.capitalize()}>" if len(key) > 1 else key
    easter_egg_progress.append(mapped)

    if easter_egg_progress == easter_egg_sequence[:len(easter_egg_progress)]:
        if len(easter_egg_progress) == len(easter_egg_sequence):
            found_easter_egg(event)
            print("Easter Egg Found!")
            easter_egg_progress.clear()
    else:
        easter_egg_progress.clear()

window.bind("<Key>", track_easter_egg)

window.mainloop()
