
from tkinter import *

<<<<<<< HEAD
import json

debug = True
trace = True

class Tk_Application(Tk):

    def __init__(self, title, width, height, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.title(title)

        # Center app in screen
        self.window_width = width
        self.window_height = height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x_coordinate = int((self.screen_width/2) - (self.window_height/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_width/2))

        self.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")


class Cypher_Application (Tk_Application):

    def __init__(self, title, width, height, *args, **kwargs):

        super().__init__(self, *args, **kwargs)

        # Text Boxes Labels, Entries, and Buttons
        self.message = LabelFrame(self, text="Message")
        self.message.pack(fill="both", expand="yes", padx=20, pady=(20, 0))

        self.input_label = Label(self.message, text="Input:")
        self.input_label.grid(row=0, column=0, padx=10, pady=(20,0), sticky=W)
        self.input_box = Text(self.message, width=100, height=15)
        self.input_box.grid(row=1, column=0, padx=10, pady=(10,20))

        self.output_label = Label(self.message, text="Output:")
        self.output_label.grid(row=2, column=0, padx=10, pady=(10,0), sticky=W)
        self.output_box = Text(self.message, width=100, height=15)
        self.output_box.grid(row=3, column=0, padx=10, pady=(10,0))

        # Options Labels, Entries, and Buttons

        self.options = LabelFrame(self, text="Options")
        self.options.pack(fill="x", expand="no", padx=20, pady=20, ipadx=20, ipady=10)

        self.offset_keyword = Label(self.options, text="Offset/Keyword")
        self.offset_keyword.grid(row=0, column=0, padx=20, pady=(15,0), sticky=E)

        self.offset_keyword_entry = Entry(self.options, width=10)
        self.offset_keyword_entry.grid(row=0, column=1, pady=(15,0), sticky=W)

        self.cypher_option = StringVar()

        self.caesar_button = Radiobutton(self.options, text="Caesar", variable=self.cypher_option, value="caesar")
        self.caesar_button.grid(row=0, column=2, padx=(18,10), pady=(20,0), sticky=N)

        self.vigenere_button = Radiobutton(self.options, text="Vigenere", variable=self.cypher_option, value="vigenere")
        self.vigenere_button.grid(row=0, column=3, padx=(0,10), pady=(20,0), sticky=N)

        self.encode_decode_option = StringVar()

        self.encode_button = Radiobutton(self.options, text="Encode", variable=self.encode_decode_option, value="encode")
        self.encode_button.grid(row=1, column=2, padx=(10,0))

        self.decode_button = Radiobutton(self.options, text="Decode", variable=self.encode_decode_option, value="decode")
        self.decode_button.grid(row=1, column=3, padx=(0,10))

        self.cypher_button = Button(self.options, text="Cypher Message!", command=lambda: self.cypher_options(self.cypher_option.get()))
        self.cypher_button.grid(row=0, column=4, padx=(10,0), pady=(20,0), ipady=10)

        self.clear_field_button = Button(self.options, text="Clear Fields", command=self.clear_fields)
        self.clear_field_button.grid(row=0, column=6, padx=10, pady=(20,0), ipady=10, sticky=W)

        self.cypher_option.set("caesar")
        self.encode_decode_option.set("encode")
        self.offset_keyword_entry.insert (0, "1")

        self.bind("<Configure>", self.save_window_position)


    def save_window_position(self, event):

        self.config["position_x"] = str(self.winfo_x())
        self.config["position_y"] = str(self.winfo_y())

        print (self.config)

        with open('app.config', 'w') as json_file:
            json.dump(self.config, json_file)


    def center_window (self, width, height):

        print ("center_window")

        screen_width = self.winfo_screenwidth ()
        screen_height = self.winfo_screenheight ()

        position_x = (screen_width - width)//2
        position_y = (screen_height - height)//2

        self.geometry (f"{width}x{height}+{position_x}+{position_y}")


    def clear_fields(self):

        self.input_box.delete(1.0, "end")
        self.output_box.delete(1.0, "end")

        # self.offset_keyword_entry.delete(0, END)

        # self.caesar_button.deselect()
        # self.vigenere_button.deselect()

        # self.encode_button.deselect()
        # self.decode_button.deselect()


    def cypher_options(self, options):

        if debug or trace: print(f"cypher_options: {options}")

        if options == "caesar":

            input_message = self.input_box.get("1.0", END)
            offset = self.offset_keyword_entry.get()
            coding_direction = self.encode_decode_option.get()

            if trace: print(f"input_message: '{input_message}', offset: '{offset}', coding_direction: '{coding_direction}'")

            if coding_direction == "":
                self.update_results ("ERROR: must selection coding method")
                return

            # check if offset is all digits before continuing or 

            try:
                offset = int(offset)

            except:
                if trace: print ("ERROR: string offset has nonnumeric characters")

                self.update_results ("ERROR: string offset has nonnumeric characters")
                return

            self.update_results (caesar_cypher(input_message, offset, coding_direction))


        if options == "vigenere":

            if trace: print("calling vigenere_option()")
        
            self.update_results (vigenere_cypher(self.input_box.get("1.0", END), self.offset_keyword_entry.get(), self.encode_decode_option.get()))


    def update_results (self, results):

        self.output_box.delete(1.0, "end")
        self.output_box.insert(1.0, results)


def caesar_cypher(message, offset, method):

    if debug or trace: print(f"initialized caesar_cypher() with message - '{message}' and offset - {offset}")
    
    message = message.lower()

    new_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
=======
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
>>>>>>> refs/remotes/michelle/main

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

<<<<<<< HEAD
        if trace: print(f"iterating through '{letter}' in message")
=======
        # Quit program button
        self.close_button = Button(self, text="Close Application", command=self.destroy)
        self.close_button.grid(row=4, column=0, columnspan=5, pady=10, ipadx=298, ipady=4)
>>>>>>> refs/remotes/michelle/main

        # Error labels
        self.keyword_error_label = Label(self, text=">>> ERROR: Keyword must only contain alphabets")
        self.keyword_error_label.grid(row=3, column=0, padx=20, sticky=W)
        self.keyword_error_label.grid_remove()

<<<<<<< HEAD
            if trace: print(f"old_index = {old_index}")

            if method == "encode":
                new_index = old_index + (offset % 26)
=======
        self.offset_error_label = Label(self, text=">>> ERROR: Offset value must be an integer")
        self.offset_error_label.grid(row=3, column=0, padx=20, sticky=W)
        self.offset_error_label.grid_remove()

>>>>>>> refs/remotes/michelle/main

    def reset_fields(self):
        self.input_box.delete(1.0, "end")
        self.output_box.delete(1.0, "end")

<<<<<<< HEAD
            if method == "decode":
                new_index = old_index - (offset % 26)
=======
        self.offset_entry.delete(0, END)
        self.offset_entry.insert(0, "0")
>>>>>>> refs/remotes/michelle/main

        self.keyword_entry.delete(0, END)
        self.keyword.set("friends")

<<<<<<< HEAD
            if trace: print(f"new_index = {new_index}")
=======
        self.disable_keyword()
>>>>>>> refs/remotes/michelle/main

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

<<<<<<< HEAD
            if trace: print(f"new_message = {new_message}")
=======
>>>>>>> refs/remotes/michelle/main

        else:
            if trace: print("calling vigenere_cypher()")

<<<<<<< HEAD
    if debug or trace: print(f"new_message = '{new_message}'")

    return new_message


def vigenere_cypher(message, keyword, method):
=======
            message = self.input_box.get("1.0", END).strip()
            action = self.encode_decode.get()
            keyword = self.keyword_entry.get()

            if not keyword.isalpha():
                self.keyword_error_label.grid(row=3, column=0, padx=20, sticky=W)
                return

            results = vigenere_cypher(message, keyword, action)

        self.display_results(results)
        self.remove_error()
>>>>>>> refs/remotes/michelle/main

    if debug or trace: print(f"initialized vigenere_cypher() with message - '{message}' and keyword - '{keyword}' and method '{method}'")

<<<<<<< HEAD
    message = message.lower()
=======
    def display_results(self, results):
        self.output_box.delete(1.0, "end")
        self.output_box.insert(1.0, results)
>>>>>>> refs/remotes/michelle/main


def caesar_cypher(message, offset, action):
    if debug: print(f"caesar_cypher() with offset - {offset}")

    message = message.strip()

<<<<<<< HEAD
        if trace: print(message[i])
            
        if not message[i].isalpha():
            new_message += message[i]
            continue
        
        if trace: print(f"key_index='{key_index}'")
        
        if method == "encode":

            if trace: print(f"encode_decode_option.get() = '{method}'")
=======
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
>>>>>>> refs/remotes/michelle/main

            if new_index > 25:
                new_index -= 26

<<<<<<< HEAD
        if method == "decode":
            new_index = letters.index(message[i]) - letters.index(keyword[key_index])

=======
>>>>>>> refs/remotes/michelle/main
            if new_index < 0:
                new_index += 26

            if trace: print(f"new_index = {new_index}")

            if letter.isupper():
                new_message.append(upper_letters[new_index])

<<<<<<< HEAD
        if key_index >= len(keyword):
            key_index = key_index % len(keyword)

        if trace: print(f"new_message = {new_message}")

        
    if debug or trace: print(new_message)

    return new_message


if __name__ == "__main__":

    application = Cypher_Application(title="Cypher GUI", width=775, height=810)

    try:
        with open('app.config', 'r') as f:
            application.config = json.load(f)
            geometry = f"{application.config['width']}x{application.config['height']}+{application.config['position_x']}+{application.config['position_y']}"
            
            application.geometry (geometry)

    except:
        application.center_window (775, 810)

        application.config = {
            "position_x": "10",
            "position_y": "10",
            "width":"775",
            "height":"810",
            "keyword":"friends",
            "offset":"1"
        }


    application.mainloop()

    with open('app.config', 'w') as json_file:
        json.dump(application.config, json_file)
=======
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

    

>>>>>>> refs/remotes/michelle/main
