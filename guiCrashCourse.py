# Must import tkinter
import tkinter as tk

# This Constructs tkinter
root = tk.Tk()

# Setting Frame Size
root.geometry("500x300")

# Setting the Title Of Frame
root.title("Music Video Player")

# Label (Text)
label = tk.Label(root, text="Hello World!", font=('Arial', 14), anchor="e", justify="left")
label.pack()

# Textbox
textbox = tk.Text(root, font=('Arial', 16), height=3)
textbox.pack()

# Entry
my_entry = tk.Entry(root)
my_entry.pack()

# Button
button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

# Button Usage in a Button Frame
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill='x')

# Test Placement on A Button
anotherbtn = tk.Button(root, text="Test")
anotherbtn.place(x=50, y=125, height=50, width=50)

# Creates GUI Frame
root.mainloop()
