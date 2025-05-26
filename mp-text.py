import tkinter as tk
import tkinter.filedialog as fd

file_name = None

def new_file():
    # Sets the file name to untitled and deletes all existing text
    global file_name
    file_name = "Untitled"
    tk.Text.delete(0.0, tk.END)

def save_file():
    # Saves existing text to current file name
    global file_name
    text = tk.Text.get(0.0, tk.END)
    file = open(file_name, "w")
    file.write(text)
    file.close()

def save_as():
    # Saves existing text to user-chosen file name
    file = fd.asksaveasfile(mode="w", defaultextension=".txt")
    text = tk.Text.get(0.0, tk.END)
    file.write(text)
    file.close()

def open_file():
    # Reads user-chosen file, deletes existing text, adds text from chosen file
    file = fd.askopenfile(mode="r")
    text = file.read()
    tk.Text.delete(0.0, tk.END)
    tk.Text.insert(0.0, text)

# Creates MP Text Editor Window
root = tk.Tk()
root.title("MP Text Editor")

# Sets window size to half of screen size and centers the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width // 2
window_height = screen_height // 2
root.geometry(f"{window_width}x{window_height}+{window_width//2}+{window_height//2}")

# Create a menubar
menubar = tk.Menu(root)

# Creates a file menu in the menubar
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator
file_menu.add_command(label="Exit", command=root.quit)

# Adds a text editor widget, setting default font to Courier and default font size to 12
text_editor = tk.Text(root, font=("Courier", "12"))

# Creates scroll bar
scroll_bar = tk.Scrollbar(text_editor)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
text_editor.grid(sticky="nesw")

# Adds scroll bar to text editor widget
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.config(yscrollcommand=scroll_bar.set)

# Adds menubar to window
root.config(menu=menubar)
root.mainloop()