# Python GUI App with Tkinter  

![Cypher GUI App final product](/gui_image.png "Cypher GUI App final product") 

<p align="center">
  <img src="https://github.com/willielassiter/code_crack/gui_image.png?raw=true" alt="Sublime's custom image"/>
</p>

This article will explain how I built a Python graphical user interface (GUI) application, and provide a general overview of Tkinter - Python’s standard GUI package. The purpose of my application is to encrypt/decrypt messages using either the Caesar or Vigenere cypher method. Please note that I structured my code using object-oriented programming (OOP). This was done mainly to increase readability and maintainability, but moreover, OOP allows me or other programmers to easily import and reuse my code in the future.    

Enough said, let’s dive into the code!   
    

### Step 1: Import the main tkinter module and its submodule, ttk         

```python

from tkinter import *
from tkinter import ttk

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
```    

The first task is simply to create a window to contain all the GUI elements. This section is in its own class because it is not integral to the main purpose of the application, and can be reused in future Tkinter projects. I elected to center the window on the screen once the application runs. Additionally, I provided users the ability to set the position of the window, such that if the user reopens the program, it will appear at the coordinates where the user previously positioned it. This is achieved by creating a function that generates a file and records the position of the window. When the application runs, the program will open the file and set the position to the coordinates in said file.   


### Step 2: Create GUI elements, also known as, widgets         

```python

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

```


Every GUI element in Tkinter is considered a widget, including labels, entry fields, text boxes, and buttons. In Tkinter, constructing any widget is always a two-step process. After I created all the necessary widgets, I then added them to the window using the grid method which allows for more customization. The workflow for this application goes from top to bottom then left to right, so that determined the order in which the widgets were positioned.         
       

```python

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

```      

The next step involved adding functionality to the buttons. Users are able to select the method and direction in which to cypher their message. To avoid confusion, I disabled an entry field depending on which cypher method was selected.  In other words, if the “Caesar” button was selected, then the keyword entry would be disabled (and vice-a-versa). This was done because the keyword entry only accepts alphabet characters and the offset entry only accepts integers.   
       
```python

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

```         


To handle user input errors, I created error message labels which will always be hidden unless the user enters “incorrect” data. I also included default settings and values in the application, to expedite the process and enhance the user experience. Whenever the “reset” button is clicked, the program will revert to the default button selections with blank message boxes and hidden error labels.   
         

```python

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

```       

### Step 3: Create Caesar and Vigenere cypher functions   
      
A bulk of the code is dedicated to defining the Caesar and Vigenere functions. For the sake of brevity, I will not go into the minute details of these functions in this article. A comprehensive description of these functions will be included in the subsequent article. Please note that both of these cypher functions are excluded from the CypherApplication class, to provide individual testing and easy accessibility to the code.   


### Step 4: Create function to handle cypher methods   
      
```python

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

```         


The principle function in my code conducts the exception handles, manages the options selections, and displays the results. The exception handling is accomplished in this main function because it is best practice to catch (and resolve) errors sooner than later, before proceeding further along the program. Lastly, I elected to create a separate function to display the results simply to provide the program more modularity and easier debugging.   
       
### Step 5: Create instance of CypherApplication class    
      
```python

if __name__ == "__main__":
    app = CypherApplication(title="Cypher GUI", width=775, height=810)
    app.mainloop()

```         


At the end of every Tkinter application, a mainloop() method must be created in order to keep the program running, until the user closes the window. This method listens for events, executes the script, and updates the GUI accordingly. Finally, I created an instance of the class, and passed in a title and window dimensions. Please note that I added an if statement at the end of my code. This “gate” is used to prevent the program from executing and merely be imported, if I or other programmers import this module.    
      

And that is all I have for you, folks! If you are interested in the inner workings of my Caesar or Vigenere functions, check out Part 2 of this article. The entirety of my GUI app program is available on GitHub. Thanks for reading and as always, Happy Coding!    