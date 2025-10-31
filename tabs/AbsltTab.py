from tkinter import * # type: ignore
from tkinter import ttk
from tkinter import messagebox
import math
import cmath
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fractions import Fraction
from utils import get_format

def create_absolute_tab(notebook, window):
    tab_abslteqnslvr = Frame(notebook)
    notebook.add(tab_abslteqnslvr,text=" | Absolute Value | ")
    tab_abslteqnslvr.config(background='#999999')

    entry_accuracy = None

    name = Label(tab_abslteqnslvr,
                 text="Absolute Value Equation Solver",
                 font=('Comic Sans MS',36),
                 background='#ffffff',
                 relief=RAISED,
                 border=8,
                 padx=8,
                 pady=8)
    name.pack(side=TOP,pady=16)

    def add_placeholder(entry_widget, placeholder):
        def on_focus_in(event):
            if entry_widget.get() == placeholder:
                entry_widget.delete(0, "end")
                entry_widget.config(fg="black")
        def on_focus_out(event):
            if entry_widget.get() == "":
                entry_widget.insert(0, placeholder)
                entry_widget.config(fg="gray")
        entry_widget.insert(0, placeholder)
        entry_widget.config(fg="gray")
        entry_widget.bind("<FocusIn>", on_focus_in)
        entry_widget.bind("<FocusOut>", on_focus_out)

    accuracy_frame = Frame(tab_abslteqnslvr, bg="#999999", relief=RAISED, border=16, padx=16, pady=8)
    accuracy_frame.pack(pady=5)
    accuracy_indication = Label(accuracy_frame,text="Significant Figures:",font=('Comic Sans MS',12),fg="#333333",relief=RAISED,border=4,width=16)
    accuracy_indication.pack(side=LEFT,padx=4)
    entry_accuracy = Entry(accuracy_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_accuracy.pack(padx=4)
    add_placeholder(entry_accuracy, "decimals...")

    coeff_frame = Frame(tab_abslteqnslvr, bg="#999999", relief=RAISED, border=16, padx=16, pady=8)
    coeff_frame.pack(pady=10)

    expected_eqn_frame = Frame(coeff_frame, bg="#ffffff", relief=RAISED, border=8, padx=8, pady=4)
    expected_eqn_frame.pack(side=TOP, pady=4)
    def expected_eqn():
        fig, ax = plt.subplots(figsize=(2, 0.5), dpi=100)
        ax.axis('off')
        ax.text(0.5, 0.5, r"$y = a|bx - h| + k$", fontsize=12, ha='center', va='center')
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        return fig
    canvas = FigureCanvasTkAgg(expected_eqn(), master=expected_eqn_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    entry_a = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_a.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_a, "Enter a...")

    entry_b = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_b.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_b, "Enter b...")

    entry_h = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_h.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_h, "Enter h...")

    entry_k = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_k.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_k, "Enter k...")

    entry_y = Entry(coeff_frame, font=('Comic Sans MS', 12), relief=RAISED, border=4, width=12)
    entry_y.pack(side=LEFT, padx=4, pady=1)
    add_placeholder(entry_y, "Enter y...")

    def SolveAbsltEquation():
        try:
            a_raw = entry_a.get()
            b_raw = entry_b.get()
            h_raw = entry_h.get()
            k_raw = entry_k.get()
            y_raw = entry_y.get()
            a = float(-1 if a_raw.strip() == "-" else a_raw if a_raw != "Enter a..." else 1)
            b = float(-1 if b_raw.strip() == "-" else b_raw if b_raw != "Enter b..." else 1)
            h = float(h_raw if h_raw != "Enter h..." else 0)
            k = float(k_raw if k_raw != "Enter k..." else 0)
            y = float(y_raw if y_raw != "Enter y..." else 0)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return
        accuracy = None
        try:
            if entry_accuracy is not None:
                raw = entry_accuracy.get()
                if raw not in ('', "decimals..."):
                    parsed = int(raw)
                    if parsed >= 0:
                        accuracy = parsed
        except ValueError:
            accuracy = None
        try:
            if a == 0:
                messagebox.showerror("Error", "This is not an absolute value equation.")
                return
            if b == 0:
                if abs(h)*a+k != y:
                    msg = "There are no solutions."
                else:
                    msg = "ℝ (This equation has infinite solutions.)"
                messagebox.showinfo("Result", msg)
                display_result(msg)
                return
            printa = '' if a == 1 else '-' if a == -1 else a
            printb = '' if b == 1 else '-' if b == -1 else b
            printh = '' if h == 0 else f"- {abs(h)}" if h > 0 else f"+ {abs(h)}"
            printk = '' if k == 0 else f"+ {abs(k)}" if k > 0 else f"- {abs(k)}"
            printy = y
            confirmfnc = messagebox.askyesno('Confirm', f"Function is {printy} = {printa}|{printb}x {printh}| {printk}?")
            if not confirmfnc:
                return
            fx = (y - k) / a
            if fx < 0:
                msg = "There are no solutions."
                messagebox.showinfo("Result", msg)
                display_result(msg)
                return
            fx1 = (fx - h) / b
            fx2 = (-fx - h) / b
            fx0 = None
            if fx1 == fx2:
                fx0 = fx1
                if fx0 == 0:
                    fx0 = 0
            if get_format() == 'Decimals':
                if accuracy is not None:
                    if round(fx1, accuracy) == round(fx2, accuracy):
                        msg = f"One solution: x = {fx0:.{accuracy}f}"
                    else:
                        msg = f"Solutions:\nx₁ = {fx1:.{accuracy}f}, x₂ = {fx2:.{accuracy}f}"
                else:
                    if fx1 == fx2:
                        msg = f"One solution: x = {fx1}"
                    else:
                        msg = f"Solutions:\nx₁ = {fx1}, x₂ = {fx2}"
                messagebox.showinfo("Solutions", msg)
                display_result(msg)
            elif get_format() == 'Fractions':
                if fx1 == fx2:
                    frac = Fraction(fx1).limit_denominator()
                    msg = f"One solution: x = {frac}"
                else:
                    frac1 = Fraction(fx1).limit_denominator()
                    frac2 = Fraction(fx2).limit_denominator()
                    msg = f"Solutions:\nx₁ = {frac1}, x₂ = {frac2}"
                messagebox.showinfo("Solutions", msg)
                display_result(msg)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")


    solve_button = Button(tab_abslteqnslvr,
                          text="Solve Equation",
                          command=SolveAbsltEquation,
                          border=8,
                          relief=RAISED,
                          padx=4,
                          pady=4)
    solve_button.pack(pady=16)

    def clear_results():
        results_box.delete("1.0", END)

    def copy_results():
        text = results_box.get("1.0", END).strip()
        if text:
            window.clipboard_clear()
            window.clipboard_append(text)
            window.update()

    buttons_frame = Frame(tab_abslteqnslvr, bg="#999999")
    buttons_frame.pack(pady=5)

    clear_button = Button(buttons_frame,
                          text="Clear Results",
                          command=clear_results,
                          border=8,
                          relief=RAISED,
                          padx=4,
                          pady=4)
    clear_button.pack(side=LEFT, padx=5)

    copy_button = Button(buttons_frame,
                         text="Copy Results",
                         command=copy_results,
                         border=8,
                         relief=RAISED,
                         padx=4,
                         pady=4)
    copy_button.pack(side=LEFT, padx=5)

    results_frame = Frame(tab_abslteqnslvr, bg="#999999", relief=RAISED, border=8, padx=8, pady=8)
    results_frame.pack(pady=10, fill=X)

    results_box = Text(results_frame,
                       font=('Comic Sans MS', 12),
                       height=8, width=60,
                       wrap=WORD,
                       relief=RAISED, border=4)
    results_box.pack(side=LEFT, fill=BOTH, expand=True)

    def display_result(text):
        results_box.insert(END, text + "\n")
        results_box.see(END)

    return tab_abslteqnslvr
