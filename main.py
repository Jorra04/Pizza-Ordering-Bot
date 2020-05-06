from tkinter import *

def run():
    text = first_name_entry.get()
    print(text)
root = Tk()
root.title("Order a pizza")
root.geometry("700x500")
first_name = Label(root, text="First Name")
first_name_entry = Entry(root) #first name
last_name = Label(root,text="Last Name")
last_name_entry = Entry(root) #last name
phone_number = Label(root, text="Phone #")
phone_number_entry = Entry(root)
address = Label(root,text="Address")
address_entry = Entry(root)
credit = Label(root, text="Credit Card Number")
credit_entry = Entry(root)
ccv = Label(root,text="CCV")
ccv_entry = Entry(root)

clicked = StringVar()
clicked.set("Pepperoni")
drop = OptionMenu(root,clicked, "Cheese", "Pepperoni", "Meat Lovers", "Canadian", "Hawaiian")

accept = Button(root,text="Click Me!", command=run)
first_name.grid(row=0, column=0 ,padx=10, pady=10)
last_name.grid(row=0, column=4)
first_name_entry.grid(row=0,column=1)
last_name_entry.grid(row=0,column=5)

phone_number.grid(row=2, column=0,padx=10, pady=10)
phone_number_entry.grid(row=2,column=1)

address.grid(row=2, column=4,padx=10, pady=10)
address_entry.grid(row=2,column=5)

credit.grid(row = 4, column=0,padx=10, pady=10)
credit_entry.grid(row=4,column=1)

ccv.grid(row=4, column=4,padx=10, pady=10)
ccv_entry.grid(row=4, column=5)
drop.grid(row = 6, column= 1)
accept.grid(row=6,column=5)






root.mainloop()

    




