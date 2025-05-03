import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    root=tk.Tk()
    root.geometry('950x1055+{}+{}'.format(
        int(root.winfo_screenwidth()/4), 
        int(root.winfo_screenheight()/4)
    ))
    root.title('Area of a Rectangle')
    
    frm_main = Frame(root)
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    make_widget(frm_main)
    root.mainloop()

def make_widget(frame):
    height_label = Label(frame, text='Height: ')
    height_label.pack(pady=10)
    height_entry = IntEntry(frame, width=4, lower_bound=12, upper_bound=90)
    height_entry.pack(pady=10)
    width_label = Label(frame, text='Width: ')
    width_label.pack(pady=10)
    width_entry = IntEntry(frame, width=4, lower_bound=8, upper_bound=90)
    width_entry.pack(pady=10)

    user_area = height_entry.get() * width_entry.get()
    area_label = Label(frame, text=f'Area: {user_area}')
    area_label.pack(pady=10)

if __name__ == "__main__":
    main()