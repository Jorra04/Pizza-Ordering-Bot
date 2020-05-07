from tkinter import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from tkinter.filedialog import askopenfilename
import pandas
import xlrd

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
    sleep(10)
    driver.find_element_by_id("Street").send_keys(address_entry.get())
    sleep(4)
    driver.find_element_by_id("City").send_keys(city_entry.get())
    sleep(4)
    driver.find_element_by_id("Postal_Code").send_keys(postal_entry.get())
    sleep(4)
    Select(driver.find_element_by_name('Region')).select_by_visible_text(prov.get())
    sleep(4)
    driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
    sleep(7)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[7]/a/div[2]/h2").click()
    sleep(20)
    if style == 1: #cheese
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[16]/div/a[1]").click()
    elif style == 2:#pep
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[11]/div/a[1]").click()
        # /html/body/div[2]/div[2]/div/div/section/div/div[16]/div/a[1]
    elif style == 3: #Meat
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[9]/div/a[1]").click()
        
    elif style == 4: #canadian
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[5]/div/a[1]").click()
    elif style == 5: #hawaiian
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[8]/div/a[1]").click()
def openPastOrder():
    # filename = askopenfilename()
    data_sheet = pandas.read_excel('Order.xlsx')
    first_name_var.set("Jorrasss")
    
def saveCurrOrder():
    pass
def endProgram():
    pass
root = Tk()
root.title("Order a pizza")
root.geometry("700x500")
first_name = Label(root, text="First Name")
first_name_var = StringVar()
first_name_entry = Entry(root,textvariable=first_name_var) #first name
last_name = Label(root,text="Last Name")
last_name_entry = Entry(root) #last name
phone_number = Label(root, text="Phone #")
phone_number_entry = Entry(root)
address = Label(root,text="Address")
address_entry = Entry(root)

city = Label(root,text="City")
city_entry = Entry(root)
postal = Label(root,text="Postal Code")
postal_entry = Entry(root)
prov = StringVar()
prov.set("ON")
province = OptionMenu(root,prov, "AL","BC","MB","NB","NL"
,"NS","NT","NU","ON","PE","QC","SK","YT")

credit = Label(root, text="Credit Card Number")
credit_entry = Entry(root)
ccv = Label(root,text="CCV")
ccv_entry = Entry(root)




######################################### creating menu ##########################################
myMenu = Menu(root)
root.config(menu=myMenu)

file_menu = Menu(myMenu)
myMenu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open...", command=openPastOrder)
file_menu.add_command(label="Save...", command=saveCurrOrder)
file_menu.add_separator()
file_menu.add_command(label="Quit...",command=endProgram)
################################ done ###################################################

clicked = StringVar()
clicked.set("Cheese")
drop = OptionMenu(root,clicked, "Cheese", "Pepperoni", "Meat Lovers", "Canadian", "Hawaiian")

accept = Button(root,text="Click Me!", command=run)
first_name.grid(row=0, column=0 ,padx=10, pady=10)
last_name.grid(row=0, column=4)
first_name_entry.grid(row=0,column=1)
last_name_entry.grid(row=0,column=5)

phone_number.grid(row=2, column=0)
phone_number_entry.grid(row=2,column=1)

address.grid(row=2, column=4)
address_entry.grid(row=2,column=5)



city.grid(row = 4, column=0)
city_entry.grid(row=4,column=1)

postal.grid(row = 4, column=4)
postal_entry.grid(row=4,column=5)


province.grid(row = 4, column=7)


credit.grid(row = 6, column=0)
credit_entry.grid(row=6,column=1)

ccv.grid(row=6, column=4)
ccv_entry.grid(row=6, column=5)
drop.grid(row = 8, column= 1)
accept.grid(row=8,column=5)


root.mainloop()