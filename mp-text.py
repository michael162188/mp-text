import tkinter as tk

def main():
    # Creates the MP Text window
    main_window = tk.Tk()
    main_window.title("MP Text")
    
    # Creates the Text Editor Widget
    text_edit = tk.Text(main_window, font = "Courier 12")
    text_edit.grid(row = 1, column =0 )

    main_window.mainloop()

main()