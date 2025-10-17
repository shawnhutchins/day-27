import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

#Button
def button_clicked():
    my_label["text"] = text_input.get()

button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

text_input = tk.Entry(width=10)
text_input.pack()

window.mainloop()