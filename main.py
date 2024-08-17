import tkinter as tk
from message import Message
from input import InputFrame
from grid import Grid


def main():
    root = tk.Tk()
    root.title("Papyrus Puzzle")
    root.geometry("800x600")
    root.resizable(False, False)

    input_frame_instance = InputFrame(root)
    input_frame = input_frame_instance.frame
    message = Message(root, input_frame)
    grid = Grid(root, input_frame)

    input_frame_instance.set_grid(grid)
    message.frame.tkraise()

    root.after(0, message.show_messages)
    root.mainloop()


if __name__ == "__main__":
    main()
