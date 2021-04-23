"""
Written By: Jacob Cox

A program that stores book information:
Title, Author, Year, ISBN

Uses Tkinter and SQLite

User can:

View all records
Search for a specific record
Add a record
Update a record
Delete a Record
"""

from tkinter import *
import sqlite3
import backend

def get_selected_row(event):
    try:
        global selectedTuple #Circumnavigates event handler
        index=output.curselection()[0] #Curselection returns tuple [0] returns index
        selectedTuple=output.get(index)

    #Fills entry Box
        titleE.delete(0,END)
        titleE.insert(END, selectedTuple[1])

        authorE.delete(0,END)
        authorE.insert(END, selectedTuple[2])

        yearE.delete(0,END)
        yearE.insert(END, selectedTuple[3])

        isbnE.delete(0,END)
        isbnE.insert(END, selectedTuple[4])
    except IndexError:
        pass
    
def view_command():
    output.delete(0,END) #Clear prior to output
    rows = backend.view()
    for row in rows:
        output.insert(END, row)

def insert_command():
    backend.insertRow(titleE.get(), authorE.get(), yearE.get(), isbnE.get())
    output.delete(0,END)
    output.insert(END, (titleE.get(), authorE.get(), yearE.get(), isbnE.get()))

def search_command():
    output.delete(0,END)
    for row in backend.search(titleE.get(), authorE.get(), yearE.get(), isbnE.get()):
        output.insert(END, row)
    
def delete_command():
    backend.delete(selectedTuple[0])

def update_command():
    backend.update(selectedTuple[0], titleE.get(), authorE.get(), yearE.get(), isbnE.get())

def close_command():
    window.destroy()

window = Tk()


#Labels

titleLabelVal=StringVar()
titleLabelVal.set("Title")

authorLabelVal=StringVar()
authorLabelVal.set("Author")

yearLabelVal=StringVar()
yearLabelVal.set("Year")

isbnLabelVal=StringVar()
isbnLabelVal.set("ISBN")

titleLabel=Label(window, textvariable=titleLabelVal)
titleLabel.grid(row=0, column = 0)

authorLabel=Label(window, textvariable=authorLabelVal)
authorLabel.grid(row=0, column = 2)

yearLabel=Label(window, textvariable=yearLabelVal)
yearLabel.grid(row=1, column = 0)

isbnLabel=Label(window, textvariable=isbnLabelVal)
isbnLabel.grid(row=1, column = 2)

#Entry Boxes

title_eVal = StringVar()
titleE=Entry(window, textvariable=title_eVal)
titleE.grid(row=0, column = 1)

author_eVal = StringVar()
authorE=Entry(window, textvariable=author_eVal)
authorE.grid(row=0, column = 3)

year_eVal = StringVar()
yearE=Entry(window, textvariable=year_eVal)
yearE.grid(row=1, column = 1)

isbn_eVal = StringVar()
isbnE=Entry(window, textvariable=isbn_eVal)
isbnE.grid(row=1, column = 3)

#Buttons

viewAll=Button(window, text="View All", width=13, command=view_command) 
viewAll.grid(row=2, column=3) #Add Button

search=Button(window, text="Search Entry", width=13, command=search_command) 
search.grid(row=3, column=3) #Add Button

add=Button(window, text="Add Entry", width=13, command=insert_command) 
add.grid(row=4, column=3) #Add Button

update=Button(window, text="Update Selected", width=13, command = update_command) 
update.grid(row=5, column=3) #Add Button

delete=Button(window, text="Delete Selected", width=13, command=delete_command) 
delete.grid(row=6, column=3) #Add Button

close=Button(window, text="Close", width=13, command= close_command)
close.grid(row=7, column=3) #Add Button

#TextBox

output= Listbox(window, width = 35, height= 6)
output.grid(row=2, column=0, columnspan=2, rowspan=6)

output.bind('<<ListboxSelect>>', get_selected_row)

#ScrollBar

scrollB=Scrollbar(window)
scrollB.grid(row=2,column=2, rowspan=6)

#Configuration
output.configure(yscrollcommand=scrollB.set)
scrollB.configure(command=output.yview)


window.mainloop()


