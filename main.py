import tkinter as tk

def button_clicked():
    my_label["text"] = text_input.get()

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

#Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(padx=50, pady=50)

#Button
button = tk.Button(text="Click Me", command=button_clicked)
new_button = tk.Button(text="New Button", command=button_clicked)

#Entry
text_input = tk.Entry(width=10)

#Packing
my_label.grid(row=0, column=0)
button.grid(row=1, column=1)
new_button.grid(row=0, column=2)
text_input.grid(row=2, column=3)

window.mainloop()