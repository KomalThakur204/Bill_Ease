import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()  # Get screen width
screen_height = root.winfo_screenheight()  # Get screen height

print(f"Screen Width: {screen_width}, Screen Height: {screen_height}")

root.mainloop()