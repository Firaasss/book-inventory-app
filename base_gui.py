from tkinter import *
import db1

# functions for buttons
def view_command():
    clearText(list_box)
    for row in db1.view():
        list_box.insert(END, row)

def search_command():
    clearText(list_box)
    for row in db1.search(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get()):
        list_box.insert(END, row)

def add_command():
    clearText(list_box)
    db1.insert(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    list_box.insert(END, "Record added.")

# for when item is selected in list_box, event param is default to bind function
def get_selected_row(event):
    global selected_tuple  # global variable to reference outside of function
    if len(list_box.curselection()) > 0:  #if there are any items in listbox - can also use 'try' 'catch indexerror'
        index = list_box.curselection()[0]  # getting index for the record that was selected
        selected_tuple = list_box.get(index)  # storing the record using the index the cursor selected

        #writing selected record into new entry fields
        title.delete(0, END)
        title.insert(END, selected_tuple[1])
        author.delete(0, END)
        author.insert(END, selected_tuple[2])
        year.delete(0, END)
        year.insert(END, selected_tuple[3])
        isbn.delete(0, END)
        isbn.insert(END, selected_tuple[4])

    else:
        print("No record is selected.")

def delete_command():
    db1.delete(selected_tuple[0])
    clearText(list_box)
    for row in db1.view():
        list_box.insert(END, row)

def update_command():
    db1.update(selected_tuple[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    clearText(list_box)
    for row in db1.view():
        list_box.insert(END, row)

#creating an empty window
window = Tk()
window.title("Book Inventory App")

# Labels
title_label = Label(window, text="Title")
author_label = Label(window, text="Author")
year_label  = Label(window, text="Year")
isbn_label = Label(window, text="ISBN")

# Entry Fields
title_entry = StringVar()
title = Entry(window, bd = 3, width = 20, textvariable = title_entry)

author_entry = StringVar()
author = Entry(window, bd = 3, width = 20, textvariable = author_entry)

year_entry = StringVar()
year = Entry(window, bd = 3, width = 20, textvariable = year_entry)

isbn_entry = StringVar()
isbn = Entry(window, bd = 3, width = 20, textvariable = isbn_entry)

# Listbox
list_box = Listbox(window, width=45)
list_box.bind('<<ListboxSelect>>', get_selected_row)

# Scrollbar
scroll = Scrollbar(window)

# Buttons
view_all = Button(window, text= "View All", width = 12, command = view_command)
search_entry = Button(window, text= "Search Entry", width = 12, command = search_command)
add_entry = Button(window, text= "Add Entry", width = 12, command = add_command)
update = Button(window, text= "Update", width = 12, command = update_command)
delete = Button(window, text= "Delete", width = 12, command = delete_command)
close = Button(window, text= "Close", width = 12, command = window.destroy)

# Gridding Labels
title_label.grid(row = 0, column = 0)
author_label.grid(row = 0, column = 2)
year_label.grid(row = 1, column = 0)
isbn_label.grid(row = 1, column = 2)

# Gridding Entry Fields
title.grid(row = 0, column = 1)
author.grid(row = 0, column = 3)
year.grid(row = 1, column = 1)
isbn.grid(row = 1, column = 3)

# Gridding Listbox + Scroll
list_box.grid(row = 2, column = 0, columnspan = 2, rowspan = 6)
scroll.grid(row = 2, column = 2, rowspan = 6)
list_box.configure(yscrollcommand = scroll.set)
scroll.configure(command = list_box.yview)

# Gridding Buttons
view_all.grid(row = 2, column = 3)
search_entry.grid(row = 3, column = 3)
add_entry.grid(row = 4, column = 3)
update.grid(row = 5, column = 3)
delete.grid(row = 6, column = 3)
close.grid(row = 7, column = 3)





# function to clear input
def clearText(textBox):
    textBox.delete(0, "end")

#needed to close the program - always at end of code
window.mainloop()
