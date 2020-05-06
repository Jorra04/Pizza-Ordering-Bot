from tkinter import *
from selenium import webdriver
from time import sleep

def run():
    if clicked.get() == "Cheese":
        # print("cheese mate")
        order(1)
    elif clicked.get() == "Pepperoni":
        # print("Pep mate")
        order(2)

    elif clicked.get() == "Meat Lovers":
        # print("Meat Lovers mate")
        order(3)

    elif clicked.get() == "Canadian":
        # print("Canadian mate")
        order(4)
    elif clicked.get() == "Hawaiian":
        # print("Hawaiian mate")
        order(5)

def order(style):
    chromePath = r"C:\Users\jorra\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromePath)
    driver.get("https://www.dominos.ca/en/")
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/main/section[1]/div/div[2]/a[1]").click()
    sleep(2)
    driver.find_element_by_xpath("//input[[@name=\"Street\"]").send_keys(address_entry.get())
def openPastOrder():
    pass
def saveCurrOrder():
    pass
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
city = Label(root,text="City")
city_entry = Entry(root)
province = Label(root,text="Province")
province_entry = Entry(root)

######################################### creating menu ##########################################
myMenu = Menu(root)
root.config(menu=myMenu)

file_menu = Menu(myMenu)
myMenu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open...", command=openPastOrder)
file_menu.add_command(label="Save...", command=saveCurrOrder)
file_menu.add_separator()
file_menu.add_command(label="Quit...",command=root.quit)
################################ done ###################################################

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



city.grid(row = 4, column=0,padx=10, pady=10)
city_entry.grid(row=4,column=1)

province.grid(row = 4, column=4,padx=10, pady=10)
province_entry.grid(row = 4, column=5)

credit.grid(row = 6, column=0,padx=10, pady=10)
credit_entry.grid(row=6,column=1)

ccv.grid(row=6, column=4,padx=10, pady=10)
ccv_entry.grid(row=6, column=5)
drop.grid(row = 8, column= 1)
accept.grid(row=8,column=5)


root.mainloop()