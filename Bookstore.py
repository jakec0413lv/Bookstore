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


def createTable():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def insertRow():
    title=title_eVal.get()
    author=author_eVal.get()
    year=year_eVal.get()
    isbn=isbn_eVal.get()
    #Connect to database
    con = sqlite3.connect("books.db") 
    #Create cursor object
    cur = con.cursor()
    #Write an SQL Query
    cur.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (title, author, year, isbn)) #Parameter Insertion
    #Commit to database
    con.commit() 
    #Close connection
    con.close()

def view():
    con = sqlite3.connect("books.db") 
    cur = con.cursor()
    cur.execute("SELECT * FROM books") 
    rows=cur.fetchall()
    con.close()
    i = 1
    for row in rows:
        output.insert(i, row)

"""
def search():
    title=title_eVal.get()
    author=author_eVal.get()
    year=year_eVal.get()
    isbn=isbn_eVal.get()

    con = sqlite3.connect("books.db") 
    #Create cursor object
    cur = con.cursor()
    #Write an SQL Query
    cur.execute("SELECT * FROM books WHERE title= ? OR author= ? OR year= ? OR isbn= ", (title, author, year, isbn))
    rows=cur.fetchall()
    con.close()
    i = 1
    for row in rows:
        output.insert(i, row)
"""

window = Tk()

createTable()

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

viewAll=Button(window, text="View All", width=13, command=view)
viewAll.grid(row=2, column=3) #Add Button

search=Button(window, text="Search Entry", width=13)
search.grid(row=3, column=3) #Add Button

add=Button(window, text="Add Entry", width=13, command=insertRow)
add.grid(row=4, column=3) #Add Button

update=Button(window, text="Update Selected", width=13)
update.grid(row=5, column=3) #Add Button

delete=Button(window, text="Delete Selected", width=13)
delete.grid(row=6, column=3) #Add Button

close=Button(window, text="Close", width=13)
close.grid(row=7, column=3) #Add Button


#TextBox

output= Listbox(window, width = 35, height= 6)
output.grid(row=2, column=0, columnspan=2, rowspan=6)

#ScrollBar

scrollB=Scrollbar(window)
scrollB.grid(row=2,column=2, rowspan=6)

#Configuration
output.configure(yscrollcommand=scrollB.set)
scrollB.configure(command=output.yview)


window.mainloop()


