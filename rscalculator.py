import tkinter as tk

calc_colour = "#FFFFFF"
label_colour = "#000000"
small_font = ("Arial", 16)
large_font = ("Arial", 40, "bold")
digits_font = ("Arial", 24, "bold")
default_font = ("Arial", 20)
default_colour = "#FFFFFF"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("RS Calculator")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total = ""
        self.current = ""
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame.rowconfigure(0, weight=1)
        for b in range(1, 5):
            self.buttons_frame.rowconfigure(b, weight=1)
            self.buttons_frame.columnconfigure(b, weight=1)


        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equal_button()

        self.create_digits_buttons()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=calc_colour)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total, anchor=tk.E, bg=calc_colour, fg=label_colour,
                               padx=24, font=small_font)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.total, anchor=tk.E, bg=calc_colour, fg=label_colour,
                         padx=24, font=large_font)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_digits_buttons(self):

        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=default_colour, fg=label_colour,
                               font=digits_font, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        k = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=default_colour, fg=label_colour, font=default_font,
                               borderwidth=0, command=lambda x=operator: self.add_operator(x))
            button.grid(row=k, column=4, sticky=tk.NSEW)
            k += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=default_colour, fg=label_colour, font=default_font,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=default_colour, fg=label_colour, font=default_font,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def update_total(self):
        self.total_label.config(text=self.total)

    def update_label(self):
        self.label.config(text=self.current)

    def add_to_expression(self, value):
        self.current += str(value)
        self.update_label()

    def add_operator(self, operator):
        self.current += operator
        self.total += self.current
        self.current = ""
        self.update_total()
        self.update_label()

    def clear(self):
        self.current = ""
        self.total = ""
        self.update_total()
        self.update_label()

    def evaluate(self):
        self.total += self.current
        self.update_total()

        self.current = str(eval(self.total))

        self.total = ""
        self.update_label()


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

