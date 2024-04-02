import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        root.geometry("300x400")  # 크기 조정

        self.current_input = ""
        self.display_var = tk.StringVar()

        # Display
        display = tk.Entry(root, textvariable=self.display_var, justify='right', font=('Arial', 18), bd=10, bg="lightgray")
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.add_button(text, row, col)

        # Adjust row and column weights to make buttons expand
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def add_button(self, text, row, col):
        button_command = lambda: self.on_button_click(text)
        tk.Button(self.root, text=text, font=('Arial', 14), command=button_command).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.current_input = ""
        elif char == '=':
            try:
                self.current_input = str(eval(self.current_input))
            except Exception:
                self.current_input = "Error"
        else:
            self.current_input += str(char)
        self.display_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

