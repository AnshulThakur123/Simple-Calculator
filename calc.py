from tkinter import Tk, Entry, StringVar, Button

class Expression:
    expression = ""

    @classmethod
    def set(cls, expression):
        cls.expression = expression
        return cls.expression

    @classmethod
    def get(cls):
        return cls.expression

def on_button_press(equation, value):
    Expression.set(Expression.get() + str(value))
    equation.set(Expression.get())

def on_equal_button_press(equation):
    try:
        total = str(eval(Expression.get()))
        equation.set(total)
    except:
        equation.set(" error ")
    finally:
        Expression.set("")

def on_clear_button_press(equation):
    Expression.set("")
    equation.set("")

def create_window(tkinter):
    tkinter.configure(background="light grey")
    tkinter.title("Calculator Made By Anshul")
    tkinter.geometry("460x430")
    return tkinter

def add_buttons(tkinter, equation):
    add_button(tkinter, ' 1 ', lambda: on_button_press(equation, '1'), 2, 0)
    add_button(tkinter, ' 2 ', lambda: on_button_press(equation, '2'), 2, 1)
    add_button(tkinter, ' 3 ', lambda: on_button_press(equation, '3'), 2, 2)
    add_button(tkinter, ' 4 ', lambda: on_button_press(equation, '4'), 3, 0)
    add_button(tkinter, ' 5 ', lambda: on_button_press(equation, '5'), 3, 1)
    add_button(tkinter, ' 6 ', lambda: on_button_press(equation, '6'), 3, 2)
    add_button(tkinter, ' 7 ', lambda: on_button_press(equation, '7'), 4, 0)
    add_button(tkinter, ' 8 ', lambda: on_button_press(equation, '8'), 4, 1)
    add_button(tkinter, ' 9 ', lambda: on_button_press(equation, '9'), 4, 2)
    add_button(tkinter, ' 0 ', lambda: on_button_press(equation, '0'), 5, 0)
    add_button(tkinter, ' + ', lambda: on_button_press(equation, '+'), 2, 3)
    add_button(tkinter, ' - ', lambda: on_button_press(equation, '-'), 3, 3)
    add_button(tkinter, ' * ', lambda: on_button_press(equation, '*'), 4, 3)
    add_button(tkinter, ' / ', lambda: on_button_press(equation, '/'), 5, 3)
    add_button(tkinter, ' = ', lambda: on_equal_button_press(equation), 5, 2)
    add_button(tkinter, ' Clear ', lambda: on_clear_button_press(equation), 5, 1)

def add_button(tkinter, text, command, row, column):
    button = Button(
        tkinter,
        text=text,
        fg='black',
        bg='light goldenrod',
        command=command,
        height=5,
        width=15
    )
    button.grid(row=row, column=column)

def add_textbox(tkinter):
    equation = StringVar()
    expression_field = Entry(tkinter, textvariable=equation)
    expression_field.grid(columnspan=4, pady=(8, 50), ipadx=70)
    return equation

def render_window(tkinter):
    tkinter.mainloop()

def run():
    tkinter = Tk()
    tkinter = create_window(tkinter)
    equation = add_textbox(tkinter)
    add_buttons(tkinter, equation)
    render_window(tkinter)

if __name__ == "__main__":
    run()

