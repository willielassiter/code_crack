from tkinter import *

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

    for letter in message:

        if trace: print(f"iterating through '{letter}' in message")

        if letter in alphabet:
            old_index = alphabet.index(letter)

            if trace: print(f"old_index = {old_index}")

            if method == "encode":
                new_index = old_index + (offset % 26)

                if new_index > 25:
                    new_index -= 26

            if method == "decode":
                new_index = old_index - (offset % 26)

                if new_index < 0:
                    new_index += 26

            if trace: print(f"new_index = {new_index}")

            new_message += alphabet[new_index]

            if trace: print(f"new_message = {new_message}")

        else:
            new_message += letter

    if debug or trace: print(f"new_message = '{new_message}'")

    return new_message


def vigenere_cypher(message, keyword, method):

    if debug or trace: print(f"initialized vigenere_cypher() with message - '{message}' and keyword - '{keyword}' and method '{method}'")

    message = message.lower()

    letters = "abcdefghijklmnopqrstuvwxyz"
    key_index = 0

    new_message = ""

    for i in range(len(message)):

        if trace: print(message[i])
            
        if not message[i].isalpha():
            new_message += message[i]
            continue
        
        if trace: print(f"key_index='{key_index}'")
        
        if method == "encode":

            if trace: print(f"encode_decode_option.get() = '{method}'")

            new_index = letters.index(message[i]) + letters.index(keyword[key_index])
        
            if new_index > 25:
                new_index -= 26

        if method == "decode":
            new_index = letters.index(message[i]) - letters.index(keyword[key_index])

            if new_index < 0:
                new_index += 26

        new_message += letters[new_index]

        key_index += 1

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
