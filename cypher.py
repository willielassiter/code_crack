from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cypher")
root.geometry("800x810")

options = LabelFrame(root, text="Options")
options.pack(fill="x", expand="no", padx=20, pady=20, ipadx=20, ipady=20)

caesar = StringVar()
caesar_option = Radiobutton(options, text="Caesar", variable=caesar, value=0)
caesar_option.grid(row=0, column=0)


vigenere = StringVar()
vigenere_option = Radiobutton(options, text="Vigenere", variable=vigenere, value=1)
vigenere_option.grid(row=0, column=1)

offset_keyword = Label(options, text="Offset/Keyword")
offset_keyword.grid(row=0, column=2)

offset_keyword_entry = Entry(options)
offset_keyword_entry.grid(row=0, column=3)

message = LabelFrame(root, text="Message")
message.pack(fill="both", expand="yes", padx=20, pady=(0, 10))

message_label = Label(message, text="Enter Your Message")
message_label.grid(row=0, column=0, pady=(20,0), sticky=W)
message_box = Text(message, width=100, height=15)
message_box.grid(row=1, column=0, pady=(0,20))

result_label = Label(message, text="Result")
result_label.grid(row=2, column=0, sticky=W)
message_result = Text(message, width=100, height=15)
message_result.grid(row=3, column=0)

root.mainloop()