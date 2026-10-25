import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=10, pady=10, ipady=10)


def click(value):
    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    else:
        display.insert(tk.END, value)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True, fill="both")

    for item in row:
        button = tk.Button(
            frame,
            text=item,
            font=("Arial", 16),
            command=lambda x=item: click(x)
        )
        button.pack(side="left", expand=True, fill="both", padx=3, pady=3)

root.mainloop()