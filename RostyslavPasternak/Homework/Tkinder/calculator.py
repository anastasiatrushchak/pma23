import tkinter as tk

# you can use the keyboard as well as the buttons

class CalculatorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Калькулятор")
        self.window.geometry("610x500")

        self.current_input = ""
        self.last_operator = None
        self.result = 0

        self.create_widgets()
    def change_text(self, num):
        self.current_input += str(num)
        self.entry.delete(0, "end")
        self.entry.insert(0, self.current_input)

    def calculate(self):
        if self.last_operator:
            if self.last_operator == "+":
                self.result += float(self.current_input)
            elif self.last_operator == "-":
                self.result -= float(self.current_input)
            elif self.last_operator == "*":
                self.result *= float(self.current_input)
            elif self.last_operator == "/":
                self.result /= float(self.current_input)
            self.entry.delete(0, "end")
            if self.result.is_integer():
                self.result = (int(self.result))
            self.entry.insert(0, self.result)
            self.current_input = self.result
            self.last_operator = None

    def set_operator(self, operator):

        if self.current_input:
            if self.last_operator:
                self.calculate()
            else:
                self.result = float(self.current_input)
            self.last_operator = operator
            self.current_input = ""
            self.entry.delete(0, "end")
            if self.result.is_integer():
                self.result = (int(self.result))
            self.entry.insert(0, self.result)
    def delete(self):
        self.result = 0
        self.current_input = ""
        self.last_operator = None
        self.entry.delete(0, "end")

    def create_widgets(self):
        self.entry = tk.Entry(self.window, width=50)
        custom_font = ("Helvetica", 20)
        self.entry.configure(font=custom_font)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.entry.bind("<Key>", self.validate_input)

        button_layout = [
            [1, 2, 3, "+"],
            [4, 5, 6, "-"],
            [7, 8, 9, "*"],
            [0, ".", "=", "/"],
            ["del"]
        ]

        for i, row in enumerate(button_layout):
            for j, button_text in enumerate(row):
                row = i + 1
                col = j
                if button_text == "=":
                    button = tk.Button(self.window, text=str(button_text), command=self.calculate)
                elif button_text in ["+", "-", "*", "/"]:
                    button = tk.Button(self.window, text=str(button_text),
                                       command=lambda button_text=button_text: self.set_operator(button_text))
                elif button_text == "del":
                    button = tk.Button(self.window, text=str(button_text), command=self.delete)
                else:
                    button = tk.Button(self.window, text=str(button_text), fg="orange",
                                       command=lambda button_text=button_text: self.change_text(button_text))
                button.config(width=10, height=4)
                button.grid(row=row, column=col)


    def validate_input(self, event):
        input_char = event.char
        print(input_char)
        if input_char.isdigit():
            self.change_text(input_char)
        elif input_char in ["+", "-", "*", "/"]:
            self.entry.delete(0, 'end')
            self.set_operator(input_char)
        elif input_char in ["=", ""]:
            self.calculate()
        return 'break'



if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()

