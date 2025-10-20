import tkinter as tk

def button_clicked():
    my_label["text"] = text_input.get()

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))

#Button
button = tk.Button(text="Click Me", command=button_clicked)

#Entry
text_input = tk.Entry(width=10)

#Packing
my_label.pack()
button.pack()
text_input.pack()

window.mainloop()