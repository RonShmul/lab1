from tkinter import *
from backend import *

window = Tk()
frame = Frame(window)
create_table()
create_ratings_table()

# list box and scroll
listbox = Listbox(frame)
scrollbar = Scrollbar(frame, orient="vertical")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
frame.grid(row=3, column=0, rowspan=5, columnspan=4)
listbox.grid(row=0, column=0)
scrollbar.grid(row=0, column=2)
#labels
title_l = Label(window, text='Title')
id_l = Label(window, text='Id')
genre_l = Label(window, text='genre')
title_l.grid(row=0, column=0)
id_l.grid(row=0, column=2)
genre_l.grid(row=0, column=4)

#values of labels
title_v = StringVar()
id_v = StringVar()
genre_v = StringVar()

# entries
title_e = Entry(window, textvariable=title_v)
id_e = Entry(window, textvariable=id_v)
genre_e = Entry(window, textvariable=genre_v)
title_e.grid(row=0, column=1)
id_e.grid(row=0, column=3)
genre_e.grid(row=0, column=5)

# functions for backend:
def view_all_front():
    listbox.delete(0, END)
    rows = view_all()
    for row in rows:
        listbox.insert(END, ' '.join(row))

def search_front(): #todo- fix: can search from each field
    listbox.delete(0, END)
    rows = search(id_e.get(), title_e.get(), genre_e.get())
    for row in rows:
        listbox.insert(END, ' '.join(row))

def add_front():
    listbox.delete(0, END)
    insert_movie(id_v.get(), title_v.get(), genre_v.get())

def update_front(): #todo- fix: can update each field? including id?
    listbox.delete(0, END)
    update(id_v.get(), title_v.get(), genre_v.get())

def delete_front(): # todo- i dont know how yet
    movie = listbox.curselection()
    listbox.delete(0, END)
    rows = check(movie)
    for row in rows:
        listbox.insert(END, ' '.join(row))

#buttons
view_all_b = Button(window, text='View all', command=lambda : view_all_front())
search_b = Button(window, text='Search entry',command=lambda : search_front())
add_b = Button(window, text='Add entry', command=lambda : add_front())
update_b = Button(window, text='Update selected', command=lambda : update_front())
delete_b = Button(window, text='Delete selected', command=lambda : delete_front())
close_b = Button(window, text='Close', command=lambda : window.destroy())
view_all_b.grid(row=2,column=5)
search_b.grid(row=3,column=5)
add_b.grid(row=4,column=5)
update_b.grid(row=5,column=5)
delete_b.grid(row=6,column=5)
close_b.grid(row=7,column=5)

window.mainloop()
