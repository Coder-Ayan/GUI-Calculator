from tkinter import *

calculator = Tk()
calculator.geometry("330x500")
calculator.minsize("330", "500")
calculator.maxsize("330", "500")
calculator.resizable(0, 0)
calculator.title("GUI Calculator - Coder Ayan")
calculator.wm_iconbitmap("Calculator.ico")


def input_screen():
    global text_problem
    text_problem = StringVar()
    text_problem.set('')
    global input_problem
    input_problem = Entry(calculator, textvariable=text_problem,
                          font="lucida 25 bold", justify=RIGHT)
    input_problem.pack(side="top", ipady=26)

    global bracket_num
    bracket_num = 0


def commands(event):

    global bracket_num

    key = event.widget.cget("text")

    if key == '=':

        problem = input_problem.get()

        problem = problem.replace('÷', '/')
        problem = problem.replace('×', '*')
        problem = problem.replace('^', '**')

        if problem == '':
            total = 0
        else:
            try:
                total = str(eval(problem))
            except:
                total = "Error"

        input_problem.delete(0, END)
        text_problem.set(text_problem.get() + total)

    elif key == '⌫':
        if text_problem.get().endswith('(') or text_problem.get().endswith(')'):
            bracket_num -= 1
            
        if text_problem.get() == 'Error':
            input_problem.delete(0, END)

        the_problem = input_problem.get()
        input_problem.delete(0, END)
        present_problem = the_problem[0:len(the_problem)-1]
        text_problem.set(text_problem.get() + present_problem)

    elif key == 'C':
        input_problem.delete(0, END)

    elif key == '()':
        # global bracket_num
        bracket_num += 1

        if (bracket_num % 2) == 0:
            text_problem.set(text_problem.get() + ')')
        else:
            text_problem.set(text_problem.get() + '(')

    else:
        text_problem.set(text_problem.get() + key)

    input_problem.update()


def buttons():

    def on_button(_button_):
        _button_.widget["background"] = "gray"

    def leave_button(_button_):
        _button_.widget["background"] = "black"

    # Line 1 of buttons(.,0,(),=)
    frame_of_buttons_of_line_1 = Frame(calculator)
    frame_of_buttons_of_line_1.pack(side=BOTTOM, anchor="sw")
    # Button .
    button_point = Button(frame_of_buttons_of_line_1, text=".", font="arial 25 bold",
                          bg="black", fg="white", padx=25, pady=10, borderwidth=0)
    button_point.pack(side=LEFT)

    button_point.bind("<Button-1>", commands)
    button_point.bind("<Enter>", on_button)
    button_point.bind("<Leave>", leave_button)
    # Button 0
    button_0 = Button(frame_of_buttons_of_line_1, text="0", font="arial 25 bold",
                      bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_0.pack(side=LEFT)

    button_0.bind("<Button-1>", commands)
    button_0.bind("<Enter>", on_button)
    button_0.bind("<Leave>", leave_button)
    # Button ()
    button_bracket = Button(frame_of_buttons_of_line_1, text="()", font="arial 25 bold",
                            bg="black", fg="white", padx=19, pady=10, borderwidth=0)
    button_bracket.pack(side=LEFT)

    button_bracket.bind("<Button-1>", commands)
    button_bracket.bind("<Enter>", on_button)
    button_bracket.bind("<Leave>", leave_button)
    # Button =
    button_equal = Button(frame_of_buttons_of_line_1, text="=", font="arial 25 bold",
                          bg="black", fg="white", padx=25, pady=10, borderwidth=0)
    button_equal.pack(side=LEFT)

    button_equal.bind("<Button-1>", commands)
    button_equal.bind("<Enter>", on_button)
    button_equal.bind("<Leave>", leave_button)

    # Line 2 of buttons(1,2,3,=)
    frame_of_buttons_of_line_2 = Frame(calculator)
    frame_of_buttons_of_line_2.pack(side=BOTTOM, anchor="sw")
    # Button 1
    button_1 = Button(frame_of_buttons_of_line_2, text="1", font="arial 25 bold",
                      bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_1.pack(side=LEFT)

    button_1.bind("<Button-1>", commands)
    button_1.bind("<Enter>", on_button)
    button_1.bind("<Leave>", leave_button)
    # Button 2
    button_2 = Button(frame_of_buttons_of_line_2, text="2", font="arial 25 bold",
                      bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_2.pack(side=LEFT)

    button_2.bind("<Button-1>", commands)
    button_2.bind("<Enter>", on_button)
    button_2.bind("<Leave>", leave_button)
    # Button 3
    button_3 = Button(frame_of_buttons_of_line_2, text="3", font="arial 25 bold",
                      bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_3.pack(side=LEFT)

    button_3.bind("<Button-1>", commands)
    button_3.bind("<Enter>", on_button)
    button_3.bind("<Leave>", leave_button)
    # Button +
    button_plus = Button(frame_of_buttons_of_line_2, text="+", font="arial 25 bold",
                         bg="black", fg="white", padx=25, pady=10, borderwidth=0)
    button_plus.pack(side=LEFT)

    button_plus.bind("<Button-1>", commands)
    button_plus.bind("<Enter>", on_button)
    button_plus.bind("<Leave>", leave_button)

    # Line 3 of buttons(4,5,6,-)
    frame_of_buttons_of_line_3 = Frame(calculator)
    frame_of_buttons_of_line_3.pack(side=BOTTOM, anchor="sw")
    # Button 4
    button_4 = Button(frame_of_buttons_of_line_3, text="4", font="arial 25 bold",
                      bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_4.pack(side=LEFT)

    button_4.bind("<Button-1>", commands)
    button_4.bind("<Enter>", on_button)
    button_4.bind("<Leave>", leave_button)
    # Button 5
    button_5 = Button(frame_of_buttons_of_line_3, text="5", font="arial 25 bold",
                      bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_5.pack(side=LEFT)

    button_5.bind("<Button-1>", commands)
    button_5.bind("<Enter>", on_button)
    button_5.bind("<Leave>", leave_button)
    # Button 6
    button_6 = Button(frame_of_buttons_of_line_3, text="6", font="arial 25 bold",
                      bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_6.pack(side=LEFT)

    button_6.bind("<Button-1>", commands)
    button_6.bind("<Enter>", on_button)
    button_6.bind("<Leave>", leave_button)
    # Button -
    button_minus = Button(frame_of_buttons_of_line_3, text="-", font="arial 25 bold",
                          bg="black", fg="white", padx=29, pady=10, borderwidth=0)
    button_minus.pack(side=LEFT)

    button_minus.bind("<Button-1>", commands)
    button_minus.bind("<Enter>", on_button)
    button_minus.bind("<Leave>", leave_button)

    # Line 4 of buttons(7,8,9,×)
    frame_of_buttons_of_line_4 = Frame(calculator)
    frame_of_buttons_of_line_4.pack(side=BOTTOM, anchor="sw")
    # Button 7
    button_7 = Button(frame_of_buttons_of_line_4, text="7", font="arial 25 bold",
                      bg="black", fg="white", padx=16+5, pady=10, borderwidth=0)
    button_7.pack(side=LEFT)

    button_7.bind("<Button-1>", commands)
    button_7.bind("<Enter>", on_button)
    button_7.bind("<Leave>", leave_button)
    # Button 8
    button_8 = Button(frame_of_buttons_of_line_4, text="8", font="arial 25 bold",
                      bg="black", fg="white", padx=16+5, pady=10, borderwidth=0)
    button_8.pack(side=LEFT)

    button_8.bind("<Button-1>", commands)
    button_8.bind("<Enter>", on_button)
    button_8.bind("<Leave>", leave_button)
    # Button 9
    button_9 = Button(frame_of_buttons_of_line_4, text="9", font="arial 25 bold",
                      bg="black", fg="white", padx=16+5, pady=10, borderwidth=0)
    button_9.pack(side=LEFT)

    button_9.bind("<Button-1>", commands)
    button_9.bind("<Enter>", on_button)
    button_9.bind("<Leave>", leave_button)
    # Button ×
    button_multiply = Button(frame_of_buttons_of_line_4, text="×", font="arial 25 bold",
                             bg="black", fg="white", padx=20+5, pady=10, borderwidth=0)
    button_multiply.pack(side=LEFT)

    button_multiply.bind("<Button-1>", commands)
    button_multiply.bind("<Enter>", on_button)
    button_multiply.bind("<Leave>", leave_button)

    # Line 5 of buttons(^,C,⌫,÷)
    frame_of_buttons_of_line_5 = Frame(calculator)
    frame_of_buttons_of_line_5.pack(side=BOTTOM, anchor="sw")
    # Button ^
    button_power = Button(frame_of_buttons_of_line_5, text="^", font="arial 25 bold",
                          bg="black", fg="white", padx=21, pady=10, borderwidth=0)
    button_power.pack(side=LEFT)

    button_power.bind("<Button-1>", commands)
    button_power.bind("<Enter>", on_button)
    button_power.bind("<Leave>", leave_button)
    # Button C
    button_clear = Button(frame_of_buttons_of_line_5, text="C", font="arial 25 bold",
                          bg="black", fg="white", padx=18, pady=10, borderwidth=0)
    button_clear.pack(side=LEFT)

    button_clear.bind("<Button-1>", commands)
    button_clear.bind("<Enter>", on_button)
    button_clear.bind("<Leave>", leave_button)
    # Button ⌫
    button_backspace = Button(frame_of_buttons_of_line_5, text="⌫", font="arial 19 bold",
                              bg="black", fg="white", padx=17, pady=17, borderwidth=0)
    button_backspace.pack(side=LEFT)

    button_backspace.bind("<Button-1>", commands)
    button_backspace.bind("<Enter>", on_button)
    button_backspace.bind("<Leave>", leave_button)
    # Button ÷
    button_divide = Button(frame_of_buttons_of_line_5, text="÷", font="arial 25 bold",
                           bg="black", fg="white", padx=18, pady=10, borderwidth=0)
    button_divide.pack(side=LEFT)

    button_divide.bind("<Button-1>", commands)
    button_divide.bind("<Enter>", on_button)
    button_divide.bind("<Leave>", leave_button)


input_screen()
buttons()

calculator.mainloop()
