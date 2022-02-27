from tkinter import *
from tkinter import ttk
from tkinter import messagebox


debug = True
trace = True

class App(Tk):
    def __init__(self, title, width, height):
        super().__init__()

        self.title(title)

        # Center app in screen
        self.window_width = width
        self.window_height = height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x_coordinate = int((self.screen_width/2) - (self.window_height/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_width/2))

        # Open app in previos position
        try:
            with open("app.config", "r") as config:
                self.geometry(config.readline())
        
        except:
            self.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")

        self.bind("<Configure>", self.save_position)

    def save_position(self, event):
        with open("app.config", "w") as config:
            config.write(self.geometry())


class CypherApplication(App):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

        # Messages: Labels, Entries, and Buttons
        self.message = LabelFrame(self, text="Messages")
        self.message.grid(row=0, column=0, padx=20, pady=(20,10))

        self.input_label = Label(self.message, text="Input Message -")
        self.input_label.grid(row=0, column=0, padx=10, pady=(20,0), sticky=W)

        self.input_box = Text(self.message, width=100, height=15)
        self.input_box.grid(row=1, column=0, padx=10, pady=(10,20))

        self.output_label = Label(self.message, text="Output Messsage -")
        self.output_label.grid(row=2, column=0, padx=10, pady=(10,0), sticky=W)

        self.output_box = Text(self.message, width=100, height=15)
        self.output_box.grid(row=3, column=0, padx=10, pady=(10,20))

        # Options: Labels, Entries, and Buttons
        self.options = LabelFrame(self, text="Options")
        self.options.grid(row=1, column=0, padx=20, pady=(0,10), ipadx=4)

        self.button_options = StringVar()

        self.caesar_button = Radiobutton(self.options, text="Caesar", variable=self.button_options, value="caesar", command=self.disable_keyword)
        self.caesar_button.grid(row=0, column=0, padx=(18,10), pady=(10,0), sticky=N)
        self.caesar_button.select()

        self.vigenere_button = Radiobutton(self.options, text="Vigenere", variable=self.button_options, value="vigenere", command=self.disable_offset)
        self.vigenere_button.grid(row=1, column=0, padx=(25,10), pady=(0,10), sticky=N)

        self.offset = IntVar()

        self.offset_label = Label(self.options, text="Offset:")
        self.offset_label.grid(row=0, column=1, padx=20, sticky=E)

        self.offset_entry = Entry(self.options, width=10, textvariable=self.offset)
        self.offset_entry.grid(row=0, column=2, sticky=W)

        self.keyword = StringVar()

        self.keyword_label = Label(self.options, text="Keyword:")
        self.keyword_label.grid(row=1, column=1, padx=20, pady=(0,10), sticky=E)

        self.keyword_entry = Entry(self.options, width=10, textvariable=self.keyword, state=DISABLED)
        self.keyword_entry.grid(row=1, column=2, pady=(0,10), sticky=W)
        self.keyword.set("friends")

        self.encode_decode = StringVar()

        self.encode_button = Radiobutton(self.options, text="Encode", variable=self.encode_decode, value="encode")
        self.encode_button.grid(row=0, column=3, padx=(25,20), pady=(10,0))
        self.encode_button.select()

        self.decode_button = Radiobutton(self.options, text="Decode", variable=self.encode_decode, value="decode")
        self.decode_button.grid(row=1, column=3, padx=(25,20), pady=(0,10))

        self.cypher_button = Button(self.options, text="Cypher Message !", height=2, command=lambda: self.cypher_message(self.button_options.get()))
        self.cypher_button.grid(row=0, column=4, rowspan=2, padx=15)

        self.reset_button = Button(self.options, text="Reset", height=2, command=self.reset_fields)
        self.reset_button.grid(row=0, column=5, rowspan=2, padx=15, sticky=W)

        # Quit program button
        self.close_button = Button(self, text="Close Application", command=self.destroy)
        self.close_button.grid(row=4, column=0, columnspan=5, pady=10, ipadx=298, ipady=4)

        # Error labels
        self.keyword_error_label = Label(self, text=">>> ERROR: Keyword must only contain alphabets")
        self.keyword_error_label.grid(row=3, column=0, padx=20, sticky=W)
        self.keyword_error_label.grid_remove()

        self.offset_error_label = Label(self, text=">>> ERROR: Offset value must be an integer")
        self.offset_error_label.grid(row=3, column=0, padx=20, sticky=W)
        self.offset_error_label.grid_remove()


    def reset_fields(self):
        self.input_box.delete(1.0, "end")
        self.output_box.delete(1.0, "end")

        self.offset_entry.delete(0, END)
        self.offset_entry.insert(0, "0")

        self.keyword_entry.delete(0, END)
        self.keyword.set("friends")

        self.disable_keyword()

        self.caesar_button.select()
        self.vigenere_button.deselect()

        self.encode_button.select()
        self.decode_button.deselect()

        self.remove_error()


    def disable_keyword(self):
        self.offset_entry.config(state=NORMAL)
        self.keyword_entry.config(state=DISABLED)


    def disable_offset(self):
        self.keyword_entry.config(state=NORMAL)
        self.offset_entry.config(state=DISABLED)

    
    def remove_error(self):
        self.keyword_error_label.grid_remove()
        self.offset_error_label.grid_remove()


    def cypher_message(self, options):
        if debug: print("cypher_message()")

        if options == "caesar":
            if trace: print("calling caesar_cypher()")

            message = self.input_box.get("1.0", END).strip()
            action = self.encode_decode.get()

            try:
                offset = int(self.offset_entry.get())

            except:
                self.offset_error_label.grid(row=3, column=0, padx=20, sticky=W)
                return

            if trace: print("message - '{message}', offset = {offset}, action = '{action}'")

            results = caesar_cypher(message, offset, action)


        else:
            if trace: print("calling vigenere_cypher()")

            message = self.input_box.get("1.0", END).strip()
            action = self.encode_decode.get()
            keyword = self.keyword_entry.get()

            if not keyword.isalpha():
                self.keyword_error_label.grid(row=3, column=0, padx=20, sticky=W)
                return

            results = vigenere_cypher(message, keyword, action)

        self.display_results(results)
        self.remove_error()


    def display_results(self, results):
        self.output_box.delete(1.0, "end")
        self.output_box.insert(1.0, results)


def caesar_cypher(message, offset, action):
    if debug: print(f"caesar_cypher() with offset - {offset}")

    message = message.strip()

    if debug: print(f"message = '{message}'")

    if action == "decode":
        offset = -(offset)

    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    new_message = []

    for letter in message:

        if trace: print(f"iterating through '{letter}' in message")

        if not letter.isalpha():
            new_message.append(letter)

        else:
            if letter in lower_letters:
                old_index = ord(letter) - ord("a")

            else:
                old_index = ord(letter) - ord("A")

            if trace: print(f"old_index = {old_index}")
            
            new_index = old_index + (offset % 26)

            if new_index > 25:
                new_index -= 26

            if new_index < 0:
                new_index += 26

            if trace: print(f"new_index = {new_index}")

            if letter.isupper():
                new_message.append(upper_letters[new_index])

            else:
                new_message.append(lower_letters[new_index])

    new_message = "".join(new_message)

    if debug: print(f"new_message = '{new_message}'")

    return new_message


def vigenere_cypher(message, keyword, action):
    if debug: print(f"vigenere_cypher() with keyword -'{keyword}'")

    message = message.strip()
    keyword = keyword.lower()

    if debug: print(f"message - '{message}', keyword - '{keyword}', action - '{action}'")

    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    keyword_index = 0

    new_message = []
    offsets = []
    
    for letter in keyword:
        if action == "encode":
            offsets.append(ord(letter) - ord("a"))
        
        else:
            offsets.append(-(ord(letter) - ord("a")))

    for letter in message:

        if trace: print(f"iterating through '{letter}' in message")
            
        if not letter.isalpha():
            new_message.append(letter)
            continue

        if letter in lower_letters:
            old_index = ord(letter) - ord("a")

        else:
            old_index = ord(letter) - ord("A")

        if trace: print(f"old_index = '{old_index}', offsets[keyword_index] = '{offsets[keyword_index]}', new_message - '{new_message}'")

        new_index = old_index + (offsets[keyword_index] % 26)

        if new_index > 25:
            new_index -= 26

        if new_index < 0:
            new_index += 26

        if trace: print(f"new_index - '{new_index}'")

        if letter.isupper():
            new_message.append(upper_letters[new_index])

        else:
            new_message.append(lower_letters[new_index])

        keyword_index += 1

        if keyword_index >= len(keyword):
            keyword_index = keyword_index % len(keyword)

    new_message = "".join(new_message)
        
    if debug: print(f"new_message - '{new_message}'")
        
    return new_message
        

if __name__ == "__main__":
    app = CypherApplication(title="Cypher GUI", width=775, height=810)
    app.mainloop()

