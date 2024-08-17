import tkinter as tk


class InputFrame:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root, bg="black")
        self.frame.grid(row=0, column=0, sticky='news')

        input_inner_frame = tk.Frame(self.frame, bg="black")
        input_inner_frame.place(relx=0.5, rely=0.5, anchor='center')

        rows_label = tk.Label(input_inner_frame, text="Enter the number of rows:", font=("Papyrus", 14), fg="white",
                              bg="black")
        rows_label.pack(anchor=tk.W)
        self.rows_entry = tk.Entry(input_inner_frame, width=5)
        self.rows_entry.pack(anchor=tk.W)

        cols_label = tk.Label(input_inner_frame, text="Enter the number of columns:", font=("Papyrus", 14), fg="white",
                              bg="black")
        cols_label.pack(anchor=tk.W)
        self.cols_entry = tk.Entry(input_inner_frame, width=5)
        self.cols_entry.pack(anchor=tk.W)

        self.button = tk.Button(input_inner_frame, text="Generate Grid", font=("Papyrus", 14), fg="white",
                                         bg="black")
        self.button.pack(anchor=tk.W, pady=10)

    def set_grid(self, grid):
        self.button.config(command=lambda: grid.generate_grid(int(self.rows_entry.get()), int(self.cols_entry.get())))
