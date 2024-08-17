import tkinter as tk
import random
from tkinter import messagebox
from message import Message


class Grid:
    def __init__(self, root, input_frame):
        self.root = root
        self.input_frame = input_frame
        self.message = Message(root, input_frame)
        self.colors = ['red', 'yellow', 'green', 'blue', 'pink', 'orange', 'violet']
        self.player_x = 0
        self.player_y = 0
        self.rows = 0
        self.cols = 0

        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, sticky='news')

        self.canvas = tk.Canvas(self.frame, width=800, height=600, bg='black')
        self.canvas.grid(row=0, column=0, sticky='news')

        self.tiles = []
        self.player = None
        self.tasty = False
        self.message_rect = None
        self.message_text = None
        self.last_message = None

        root.bind('<KeyPress>', self.handle_key_press)
        root.bind('<KeyRelease>', self.handle_key_release)

    def handle_key_press(self, event):
        if event.keysym in ['Left', 'Up', 'Right', 'Down']:
            self.highlight_arrow(event)
            self.move_player(event)

    def handle_key_release(self, event):
        if event.keysym in ['Left', 'Up', 'Right', 'Down']:
            self.reset_arrow(event)

    def teardown_grid(self):
        self.canvas.delete("all")
        self.tiles = []
        self.player = None
        self.player_x = 0
        self.player_y = 0
        self.tasty = False
        self.message_rect = None
        self.message_text = None
        self.last_message = None

    def restart_grid(self, rows, cols):
        self.teardown_grid()
        self.generate_grid(rows, cols)

    def generate_grid(self, rows, cols):
        self.teardown_grid()
        self.player_x, self.player_y = 0, 0
        try:
            self.rows, self.cols = rows, cols
            if not (2 <= rows <= 12 and 2 <= cols <= 12):
                raise ValueError
        except ValueError:
            messagebox.showerror("Bad input", "Please enter valid numbers for rows and columns (2 to 12).")
            return

        self.draw_tiles()
        self.draw_arrow_keys()
        self.draw_player()
        self.message.clear_message()
        self.frame.tkraise()

        if self.last_message:
            self.show_message(self.last_message)

    def draw_tiles(self):
        self.canvas.delete("all")
        self.tiles = []

        tile_size = 40
        padding = 5

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                color = 'pink' if (i == 0 and j == 0) else random.choice(self.colors)
                x1 = j * (tile_size + padding)
                y1 = i * (tile_size + padding)
                x2 = x1 + tile_size
                y2 = y1 + tile_size

                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black', tags=f'{i}-{j}')
                row.append((rect, color))
            self.tiles.append(row)

        canvas_width = 800
        canvas_height = 600

        return_button = tk.Button(self.canvas, text="Return", font=("Papyrus", 14, "bold"), bg="black", fg="white",
                                  command=self.return_to_input)
        restart_button = tk.Button(self.canvas, text="Restart", font=("Papyrus", 14, "bold"), bg="black", fg="white",
                                   command=lambda: self.generate_grid(self.rows, self.cols))

        self.canvas.create_window(45, canvas_height - 30, window=return_button)
        self.canvas.create_window(135, canvas_height - 30, window=restart_button)

    def draw_arrow_keys(self):
        canvas_width = 800
        canvas_height = 600

        self.canvas.create_polygon(
            canvas_width - 160, canvas_height - 90,
            canvas_width - 120, canvas_height - 110,
            canvas_width - 120, canvas_height - 70,
            fill='gray', outline='black', tags='left_arrow'
        )

        self.canvas.create_polygon(
            canvas_width - 90, canvas_height - 160,
            canvas_width - 110, canvas_height - 120,
            canvas_width - 70, canvas_height - 120,
            fill='gray', outline='black', tags='up_arrow'
        )

        self.canvas.create_polygon(
            canvas_width - 20, canvas_height - 90,
            canvas_width - 60, canvas_height - 110,
            canvas_width - 60, canvas_height - 70,
            fill='gray', outline='black', tags='right_arrow'
        )

        self.canvas.create_polygon(
            canvas_width - 90, canvas_height - 20,
            canvas_width - 110, canvas_height - 60,
            canvas_width - 70, canvas_height - 60,
            fill='gray', outline='black', tags='down_arrow'
        )

    def highlight_arrow(self, event):
        if event.keysym == 'Left':
            self.canvas.itemconfig('left_arrow', fill='yellow')
        elif event.keysym == 'Up':
            self.canvas.itemconfig('up_arrow', fill='yellow')
        elif event.keysym == 'Right':
            self.canvas.itemconfig('right_arrow', fill='yellow')
        elif event.keysym == 'Down':
            self.canvas.itemconfig('down_arrow', fill='yellow')

    def reset_arrow(self, event):
        if event.keysym == 'Left':
            self.canvas.itemconfig('left_arrow', fill='gray')
        elif event.keysym == 'Up':
            self.canvas.itemconfig('up_arrow', fill='gray')
        elif event.keysym == 'Right':
            self.canvas.itemconfig('right_arrow', fill='gray')
        elif event.keysym == 'Down':
            self.canvas.itemconfig('down_arrow', fill='gray')

    def draw_player(self):
        if self.player:
            self.canvas.delete(self.player)
        x1 = self.player_x * 45
        y1 = self.player_y * 45
        x2 = x1 + 40
        y2 = y1 + 40
        self.player = self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="X", font=("Papyrus", 16, "bold"),
                                              fill="black")

    def return_to_input(self):
        self.teardown_grid()
        self.input_frame.tkraise()

    def move_player(self, event):
        dx, dy = 0, 0
        if event.keysym == 'Left':
            dx = -1
        elif event.keysym == 'Right':
            dx = 1
        elif event.keysym == 'Up':
            dy = -1
        elif event.keysym == 'Down':
            dy = 1

        new_x = self.player_x + dx
        new_y = self.player_y + dy

        if not (0 <= new_x and 0 <= new_y < self.rows):
            self.show_message(self.message.prepare_warnings("wall"))
            return

        if self.player_x == self.cols - 1:
            self.canvas.delete(self.player)
            self.trigger_end_sequence()

        condition = self.tiles[new_y][new_x][1]

        self.show_message(self.message.prepare_warnings(condition))

        if condition == "wall":
            return
        elif condition in ["red", "yellow"]:
            return
        elif condition == "orange" or condition == "pink":
            self.update_position(new_x, new_y)
            if condition == "orange":
                self.tasty = True
        elif condition == "green":
            if random.choice([True, False]):
                self.update_position(new_x, new_y)
            else:
                self.update_position(0, 0)
        elif condition == "blue":
            if self.is_yellow_tile_around(new_x, new_y) or self.tasty:
                self.show_message(self.message.prepare_warnings(
                    condition + ("&electric" if self.is_yellow_tile_around(new_x, new_y) else "&tasty")))
            else:
                self.update_position(new_x, new_y)
        elif condition == "violet":
            further_x = new_x
            further_y = new_y
            if 0 <= further_x < self.cols and 0 <= further_y < self.rows:
                further_condition = self.tiles[further_y][further_x][1]
                self.show_message(self.message.prepare_warnings(further_condition))
                if further_condition not in ["red", "yellow", "wall"]:
                    self.update_position(new_x, new_y)
                    self.update_position(further_x, further_y)

                    further_further_x = further_x + (further_x - new_x)
                    further_further_y = further_y + (further_y - new_y)

                    if 0 <= further_further_x < self.cols and 0 <= further_further_y < self.rows:
                        further_further_condition = self.tiles[further_further_y][further_further_x][1]

                        if further_further_condition == "violet":
                            self.update_position(further_further_x, further_further_y)



                    self.move_player(event)
            return
        else:
            self.update_position(new_x, new_y)

        self.draw_player()

    def trigger_end_sequence(self):
        self.canvas.delete("all")
        self.canvas.configure(bg='white')
        self.root.after(3000, self.show_final_message)

    def show_final_message(self):
        self.canvas.create_text(400, 300, text="I  BELIEVED  IN  YOU,  HUMAN!!!", font=("Papyrus", 16, "bold"),
                                fill="black")
        self.root.after(3000, self.root.quit)

    def update_position(self, x, y):
        self.player_x = x
        self.player_y = y

    def is_yellow_tile_around(self, x, y):
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.cols and 0 <= ny < self.rows:
                if self.tiles[ny][nx][1] == "yellow":
                    return True
        return False

    def show_message(self, text):
        self.last_message = text
        if self.message_rect:
            self.canvas.delete(self.message_rect)
        if self.message_text:
            self.canvas.delete(self.message_text)

        self.message_rect = self.canvas.create_rectangle(550, 20, 780, 120, outline="white", width=1)
        self.message_text = self.canvas.create_text((550 + 780) / 2, (20 + 120) / 2, text=text, font=("Papyrus", 14),
                                                    fill="white", anchor='center')

    def clear_message(self):
        if self.message_rect:
            self.canvas.delete(self.message_rect)
            self.message_rect = None
        if self.message_text:
            self.canvas.delete(self.message_text)
            self.message_text = None
        self.last_message = None
