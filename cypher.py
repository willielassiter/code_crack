from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cypher")
root.geometry("775x810")

debug = True

def cypher_options(options):

    if options == "caesar":
        if debug: print("calling caesar_option()")

        caesar_cypher(decoded_box.get("1.0", END).lower(), offset_keyword_entry.get())

    if options == "vigenere":
        if debug: print("calling vigenere_option()")
    
        vigenere_cypher(encoded_box.get("1.0", END).lower(), offset_keyword_entry.get())


def caesar_cypher(message, offset):
    if debug: print(f"initialized caesar_cypher() with message - '{message}' and offset - {offset}")
    
    new_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in message:

        if debug: print(f"iterating through '{letter}' in message")

        if letter in alphabet:
            old_index = alphabet.index(letter)

            if debug: print(f"old_index = {old_index}")

            new_index = old_index + int(offset)

            if new_index > 25:
                new_index = new_index - 26

            if debug: print(f"new_index = {new_index}")

            new_message += alphabet[new_index]

            if debug: print(f"new_message = {new_message}")

        else:
            new_message += letter

            if debug: print(f"new_message = '{new_message}'")

    # Display in texbox 
    encoded_box.delete(1.0, "end")
    encoded_box.insert(1.0, new_message)

    return new_message


def vigenere_cypher(message, keyword):
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

        new_index = letters.index(message[i]) - letters.index(keyword[key_index])

        if new_index < 0:
            new_index += 26

        new_message += letters[new_index]

        key_index += 1

        if key_index >= len(keyword):
            key_index = key_index % len(keyword)
        
        if debug: print(new_message)

    # Display in texbox 
    decoded_box.delete(1.0, "end")
    decoded_box.insert(1.0, new_message)

    return new_message


def clear_fields():
    decoded_box.delete(1.0, "end")
    encoded_box.delete(1.0, "end")
    offset_keyword_entry.delete(0, END)
    caesar_button.deselect()
    vigenere_button.deselect()


# Text Boxes Labels, Entries, and Buttons
message = LabelFrame(root, text="Message")
message.pack(fill="both", expand="yes", padx=20, pady=(20, 0))

decoded_label = Label(message, text="Decoded Message -")
decoded_label.grid(row=0, column=0, padx=10, pady=(20,0), sticky=W)
decoded_box = Text(message, width=100, height=15)
decoded_box.grid(row=1, column=0, padx=10, pady=(10,20))

encoded_label = Label(message, text="Encoded Messsage -")
encoded_label.grid(row=2, column=0, padx=10, sticky=W)
encoded_box = Text(message, width=100, height=15)
encoded_box.grid(row=3, column=0, padx=10, pady=(10,0))


# Options Labels, Entries, and Buttons
options = LabelFrame(root, text="Options")
options.pack(fill="x", expand="no", padx=20, pady=20, ipadx=20, ipady=10)

offset_keyword = Label(options, text="Offset/Keyword")
offset_keyword.grid(row=0, column=0, padx=20, pady=(15,0), sticky=E)

offset_keyword_entry = Entry(options, width=10)
offset_keyword_entry.grid(row=0, column=1, pady=(15,0), sticky=W)

button_options = StringVar()
caesar_button = Radiobutton(options, text="Caesar", variable=button_options, value="caesar", command=lambda: cypher_options("caesar"))
caesar_button.grid(row=0, column=2, padx=(18,25), pady=(15,0))

button_options = StringVar()
vigenere_button = Radiobutton(options, text="Vigenere", variable=button_options, value="vigenere", command=lambda: cypher_options("vigenere"))
vigenere_button.grid(row=0, column=3, pady=(15,0))

cypher_button = Button(options, text="Cypher Message!")
cypher_button.grid(row=0, column=4, padx=(30,0), pady=(15,0), ipady=10)

clear_fields = Button(options, text="Clear", command=clear_fields)
clear_fields.grid(row=0, column=5, padx=30, pady=(15,0), ipady=10, sticky=W)

# Database
show_database = Button(root, text="Show Database")
show_database.pack(fill="both", expand="yes", padx=20, pady=(0, 20))


root.mainloop()