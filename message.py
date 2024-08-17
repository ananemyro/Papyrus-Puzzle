import random
import tkinter as tk
from tkinter import messagebox


class Message:
    def __init__(self, root, input_frame):
        self.root = root
        self.input_frame = input_frame
        self.frame = tk.Frame(root, bg='black')
        self.frame.grid(row=0, column=0, sticky='news')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.label = tk.Label(
            self.frame,
            text="",
            font=("Papyrus", 16, "bold"),
            fg="white",
            bg="black",
            pady=20
        )
        self.label.pack(expand=True, fill='both', anchor='center')
        self.rules = [["HEY!", "IT'S  THE  HUMAN!", "YOU'RE  GONNA  LOVE  THIS  PUZZLE!",
                       "EACH  COLOR  HAS A  DIFFERENT  FUNCTION!", "RED  TILES  ARE  IMPASSABLE!",
                       "YOU  CANNOT  WALK  ON  THEM!",
                       "YELLOW  TILES  ARE  ELECTRIC!", "THEY  WILL  ELECTROCUTE  YOU!",
                       "GREEN  TILES  ARE  ALARM  TILES!",
                       "IF  YOU  STEP  ON  THEM...", "YOU  WILL  HAVE  TO  FIGHT  A  MONSTER!!",
                       "ORANGE  TILES  ARE  ORANGE-SCENTED.", "THEY  WILL  MAKE  YOU  SMELL  DELICIOUS!",
                       "BLUE  TILES  ARE  WATER  TILES.", "SWIM  THROUGH  IF  YOU  LIKE,  BUT...",
                       "IF  YOU  SMELL  LIKE  ORANGES!", "THE  PIRANHAS  WILL  BITE  YOU.",
                       "ALSO,  IF  A  BLUE  TILE  IS  NEXT  TO  A,", "YELLOW  TILE,  THE  WATER  WILL  ALSO  ZAP  YOU!",
                       "PURPLE  TILES  ARE  SLIPPERY!", "YOU  WILL  SLIDE  TO  THE  NEXT  TILE!",
                       "HOWEVER,  THE  SLIPPERY SOAP...", "SMELLS  LIKE  LEMONS!!", "WHICH  PIRANHAS  DO  NOT  LIKE!",
                       "PURPLE  AND  BLUE  ARE  OK!", "FINALLY,  PINK  TILES.", "THEY  DON'T  DO  ANYTHING.",
                       "STEP  ON  THEM  ALL  YOU  LIKE.", "HOW  WAS  THAT!?  UNDERSTAND???"],
                      ["OKAY...  I  GUESS  I'LL  REPEAT  MYSELF...", "RED  TILES  ARE  IMPASSABLE.",
                       "YELLOW  TILES  ARE  ELECTRIC  AND  DANGEROUS.", "BLUE  TILES  MAKE  YOU  FIGHT  A  MONSTER.",
                       "GREEN  TILES  ARE  WATER  TILES.", "ORANGE  TILES  ARE  ORANGE  SCENTED.",
                       "IF  YOU  STEP  ON  ORANGE,  DON'T  STEP  ON  GREEN.", "BROWN  TILES  ARE...",
                       "WAIT!!!  THERE  ARE  NO  BROWN  TILES...", "PURPLE  TILES  SMELL  LIKE  LEMONS...",
                       "WHY  DON'T  THE  YELLOW  ONES  SMELL  LEMONY?",
                       "UMM...", "WAIT!!  DID  I  MIX  UP  GREEN  AND  BLUE!?", "THE  BLUE  ONES  ARE  WATER  ONES!",
                       "PINK  TILES...", "I  DON'T...  REMEMBER???", "WAIT!!!", "THOSE  ONES  DON'T  DO  ANYTHING.",
                       "OKAY!  DO  YOU  UNDERSTAND  BETTER  NOW!?"],
                      [".   .   .   .   .   .   .   .   .   .", "OK,  YOU  KNOW  WHAT???",
                       "HOW  ABOUT...  YOU  JUST...",
                       "DO  THIS  PUZZLE...  ON  YOUR  OWN...", "GOOD  LUCK."]]
        self.warnings = {"wall": ["You\'ve hit a wall.", "Dead end.", "Bonk."],
                         "red": ["It\'s like a stop\nsign, you know?", "Can\'t pass.", "Roses are..?"],
                         "orange": ["Sweet. I know just\nsomeone who likes that.", "Fanta-scented.",
                                    "An orange a day..."],
                         "yellow": ["You\'re going to get\nyourself roasted.", "Twinkle twinkle\nlittle star...",
                                    "Should I call you\nEdison?"],
                         "green": ["So you decided\nto try your luck...", "Bold move.", "I respect that."],
                         "blue": ["Splash.", "Searching for Atlantis?", "You may borrow my\ngoggles."],
                         "blue&electric": ["Water is a good\nconductor.", "Take a better look\naround.",
                                           "This game\'s about to get\nbreathtaking. Literally."],
                         "blue&tasty": ["You smell like\ndinner.", "Maybe reconsider.", "Nom!"],
                         "violet": ["What is it called...\nTriple axel?", "You smell citrusy,\nby the way.",
                                    "Violets are..?"],
                         "pink": ["You\'re safe...\nFor now.", "Keep moving.", "Don\'t just stand there."]}
        self.confirmation_counter = 0

    def show_messages(self):
        self.display_messages(self.rules[0], 1500, self.show_confirmation)

    def display_messages(self, messages, interval, next_step):
        def display_message(index):
            if index < len(messages):
                self.label.config(text=messages[index])
                self.root.after(interval, display_message, index + 1)
            else:
                next_step()

        display_message(0)

    def show_confirmation(self):
        response = messagebox.askyesno("Rules", "Understand the explanation?")
        if response:
            self.input_frame.tkraise()
        else:
            if self.confirmation_counter == 0:
                self.confirmation_counter += 1
                self.display_messages(self.rules[1], 1300, self.show_confirmation)
            else:
                self.display_messages(self.rules[2], 1500, self.input_frame.tkraise)

    def show_warning(self, text):
        self.label.config(text=text)
        self.frame.tkraise()

    def prepare_warnings(self, condition):
        warning_id = random.randint(0, 2)
        return self.warnings[str(condition)][warning_id]

    def clear_message(self):
        self.label.config(text='')
        self.root.update_idletasks()
