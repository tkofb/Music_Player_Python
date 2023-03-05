import tkinter as tk
from tkinter import messagebox


# Just how classes work in Python
class MyGUI:

    # A sort of defautlt constructor in Python
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")

        # Creation of menus and how they work
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        # Setting them up in a cascading style
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        # Sets the menu to the new menubar
        self.root.config(menu=self.menubar)

        # Makes it so that the GUI always shows up at the top
        self.root.attributes("-topmost", True)

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        # How checkbuttons are set up and how check state can be used
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Static Method Showing", font=('Arial', 18), command=self.static_idea)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    # Example of static methods in Python through declaration
    @staticmethod
    def static_idea():
        print("Hello World!")

    # Everything past here are just random methods used in the project
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def clear(self):
        self.textbox.delete('1.0', tk.END)

    def shortcut(self, event):
        if event.keysym == "Return" and event.state == 4:
            print(messagebox.showinfo("Message", self.textbox.get('1.0', tk.END)))

    def on_closing(self):
        if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
            self.root.destroy()


MyGUI()
