from tkinter import *
import sqlite3
root = Tk()
root.title('I`m a title!')
root.geometry("400x400") 

#Create a database or connect to one!
conn = sqlite3.connect('address_book.db') 

#tworzymy kursos
cursor = conn.cursor()

#create table- to sie robi tylko raz
#cursor.execute('''CREATE TABLE addresses (
#    first_name text,
#    last_name text,
#    address text,
#    city text,
#    state text,
#    zipcode integer
#    )''')



#create text boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)
l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)
address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)
city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20)
state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)
zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)

#create text box labels
f_name_label = Label(root, text = 'First name')
f_name_label.grid(column = 0, row = 0)
l_name_label = Label(root, text = 'Last name')
l_name_label.grid(column = 0, row = 1)
address_label = Label(root, text = 'Address')
address_label.grid(column = 0, row = 2)
city_label = Label(root, text = 'City')
city_label.grid(column = 0, row = 3)
state_label = Label(root, text = 'State')
state_label.grid(column = 0, row = 4)
zipcode_label = Label(root, text = 'Zipcode')
zipcode_label.grid(column = 0, row = 5)

def submit():
    #Create a database or connect to one!
    conn = sqlite3.connect('address_book.db') # if it doesnt exist, then it creates one
    #tworzymy kursos
    cursor = conn.cursor()
    
    #insert into table
    cursor.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'state': state.get(),
                      'zipcode': zipcode.get()
                    }) 
     
    #commit changes
    conn.commit()
    #close connection
    conn.close()
    
    
    
    
    #clear the boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    #Create a database or connect to one!
    conn = sqlite3.connect('address_book.db') 
    #tworzymy kursos
    cursor = conn.cursor()
    
    
    #Query the database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall() #or fetchone() or fetchmany()
    
    
    
    
    #commit changes
    conn.commit()
    #close connection
    conn.close()
    
    
#create submit buttons
submit_btn = Button(root, text = 'Add record to Database', command = submit)
submit_btn.grid(row = 6, column = 0, pady = 10, padx = 10, ipadx = 60, columnspan = 2)

#create query button
query_btn = Button(root, text = "Show records!", command = query).grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)


#commit changes
conn.commit()
#close connection
conn.close()


root.mainloop()