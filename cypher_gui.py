from tkinter import *
from tkinter import ttk


debug = True

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Cypher")
        self.geometry("775x810")

        # Text Boxes Labels, Entries, and Buttons
        self.message = LabelFrame(self, text="Message")
        self.message.pack(fill="both", expand="yes", padx=20, pady=(20, 0))

        self.input_label = Label(self.message, text="Input Message -")
        self.input_label.grid(row=0, column=0, padx=10, pady=(20,0), sticky=W)

        self.input_box = Text(self.message, width=100, height=15)
        self.input_box.grid(row=1, column=0, padx=10, pady=(10,20))

        self.output_label = Label(self.message, text="Output Messsage -")
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

        self.button_options = StringVar()

        self.caesar_button = Radiobutton(self.options, text="Caesar", variable=self.button_options, value="caesar")
        self.caesar_button.grid(row=0, column=2, padx=(18,10), pady=(20,0), sticky=N)

        self.vigenere_button = Radiobutton(self.options, text="Vigenere", variable=self.button_options, value="vigenere")
        self.vigenere_button.grid(row=0, column=3, padx=(0,10), pady=(20,0), sticky=N)

        self.encode_decode = StringVar()

        self.encode_button = Radiobutton(self.options, text="Encode", variable=self.encode_decode, value="encode")
        self.encode_button.grid(row=1, column=2, padx=(10,0))

        self.decode_button = Radiobutton(self.options, text="Decode", variable=self.encode_decode, value="decode")
        self.decode_button.grid(row=1, column=3, padx=(0,10))

        self.cypher_button = Button(self.options, text="Cypher Message !", command=lambda: self.cypher_options(self.button_options.get()))
        self.cypher_button.grid(row=0, column=4, padx=(10,0), pady=(20,0), ipady=10)

        self.clear_button = Button(self.options, text="Clear Fields", command=self.clear_fields)
        self.clear_button.grid(row=0, column=6, padx=10, pady=(20,0), ipady=10, sticky=W)


    def cypher_options(self, options):

        if options == "caesar":
            if debug: print("calling caesar_option()")

            if self.encode_decode.get() == "encode":
                app.caesar_cypher(self.input_box.get("1.0", END).lower(), self.offset_keyword_entry.get(), self.encode_decode.get())

            if self.encode_decode.get() == "decode":
                app.caesar_cypher(self.input_box.get("1.0", END).lower(), self.offset_keyword_entry.get(), self.encode_decode.get())


        if options == "vigenere":
            if debug: print("calling vigenere_option()")
        
            if self.encode_decode.get() == "encode":
                app.vigenere_cypher(self.input_box.get("1.0", END).lower(), self.offset_keyword_entry.get(), self.encode_decode.get())

            if self.encode_decode.get() == "decode":
                app.vigenere_cypher(self.input_box.get("1.0", END).lower(), self.offset_keyword_entry.get(), self.encode_decode.get())

        
    def clear_fields(self):
        self.input_box.delete(1.0, "end")
        self.output_box.delete(1.0, "end")

        self.offset_keyword_entry.delete(0, END)

        self.caesar_button.deselect()
        self.vigenere_button.deselect()

        self.encode_button.deselect()
        self.decode_button.deselect()


    def display_results(self, results):
        self.output_box.delete(1.0, "end")
        self.output_box.insert(1.0, results)


    def caesar_cypher(self, message, offset, action):
        if debug: print(f"initialized caesar_cypher() with message - '{message}' and offset - {offset}")
        
        new_message = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for letter in message:

            if debug: print(f"iterating through '{letter}' in message")

            if letter in alphabet:
                old_index = alphabet.index(letter)

                if debug: print(f"old_index = {old_index}")

                if action == "encode":
                    new_index = old_index + int(offset)

                    if new_index > 25:
                        new_index -= 26

                if action == "decode":
                    new_index = old_index - int(offset)

                    if new_index < 0:
                        new_index += 26

                if debug: print(f"new_index = {new_index}")

                new_message += alphabet[new_index]

                if debug: print(f"new_message = {new_message}")

            else:
                new_message += letter

                if debug: print(f"new_message = '{new_message}'")

        # Display in texbox
        # if action == "encode": 
        #     self.encoded_box.delete(1.0, "end")
        #     self.encoded_box.insert(1.0, new_message)

        # if action == "decode":
        #     self.decoded_box.delete(1.0, "end")
        #     self.decoded_box.insert(1.0, new_message)

        app.display_results(new_message)

        return new_message


    def vigenere_cypher(self, message, keyword, action):
        if debug: print(f"initialized vigenere_cypher() with message - '{message}' and keyword - '{keyword}'")

        letters = "abcdefghijklmnopqrstuvwxyz"
        key_index = 0

        new_message = ""

        for i in range(len(message)):

            if debug: print(message[i])
                
            if not message[i].isalpha():
                new_message += message[i]
                continue
            
            if debug: print(f"key_index='{key_index}'")
            
            if action == "encode":

                if debug: print(f"encode_decode.get() = '{action}'")

                new_index = letters.index(message[i]) + letters.index(keyword[key_index])
            
                if new_index > 25:
                    new_index -= 26

            if action == "decode":
                new_index = letters.index(message[i]) - letters.index(keyword[key_index])

                if new_index < 0:
                    new_index += 26

            new_message += letters[new_index]

            key_index += 1

            if key_index >= len(keyword):
                key_index = key_index % len(keyword)
            
            if debug: print(new_message)

        # Display in texbox 
        # if action == "decode":
        #     self.decoded_box.delete(1.0, "end")
        #     self.decoded_box.insert(1.0, new_message)
            
        # if action == "encode":
        #     self.encoded_box.delete(1.0, "end")
        #     self.encoded_box.insert(1.0, new_message)

        app.display_results(new_message)
            
        return new_message
        

if __name__ == "__main__":
    app = App()
    app.mainloop()