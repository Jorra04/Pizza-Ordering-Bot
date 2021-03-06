from tkinter import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from tkinter.filedialog import askopenfilename, asksaveasfilename
from twilio.rest import Client
from creds import account_sid, auth_token, cell, twillio_num
import xlrd, xlsxwriter

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
    chromePath = r"chromedriver.exe"
    driver = webdriver.Chrome(chromePath)
    driver.get("https://www.dominos.ca/en/")
    client = Client(account_sid, auth_token)
    try:
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

        ############### Place order #############################################
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/aside/div[2]/a").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[24]/section/div/div[2]/div/a").click()
        sleep(5)
        Select(driver.find_element_by_name('1|Quantity')).select_by_visible_text(quantity_val.get())
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div/aside/div[3]/a").click()
        sleep(7)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[1]/div/div[3]/div[2]/div/div[2]/input").send_keys(first_name_var.get())
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[1]/div/div[3]/div[2]/div/div[3]/input").send_keys(last_name_var.get())
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[1]/div/div[3]/div[2]/div/div[4]/div/bdo/input").send_keys("Jorra04@gmail.com")
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[1]/div/div[3]/div[2]/div/div[8]/div[1]/bdo/input[1]").send_keys("("+ phone_number_var.get()[0:3]+") "+
        phone_number_var.get()[3:6] + "-"+ phone_number_var.get()[6:10])
        sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[4]/div/div[2]/div[2]/div[5]/label/input").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[4]/div/div[2]/div[2]/div[5]/div/div/div[2]/input").send_keys(credit_var.get())
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[4]/div/div[2]/div[2]/div[5]/div/div/div[4]/div[2]/input").send_keys(ccv_var.get())
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[4]/div/div[2]/div[2]/div[5]/div/div/div[5]/div[1]/input").send_keys(postal_var.get())
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[4]/div/div[2]/div[2]/div[26]/div/div[1]/div/label/input").click()
        sleep(3)
        Select(driver.find_element_by_name('Expiration_Month')).select_by_visible_text(cc_exp_month_val.get())
        sleep(2)
        Select(driver.find_element_by_name('Expiration_Year')).select_by_visible_text(cc_exp_year_val.get())
        sleep(4)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/form/div[5]/div/div[4]/button").click()
        message = 'Your order has been completed. It will arrive within 20-45 minutes from receiving this message. Thank you!'  
        message = client.messages.create(body=message,
        from_=twillio_num, to=cell)
        driver.quit()
        root.destroy()
    except:
        message = 'We incurred an issue while trying to process your request. Please restart the process.'  
        message = client.messages.create(body=message,
        from_=twillio_num, to=cell)
        driver.quit()
        root.destroy()
        

def openPastOrder():
    fileName = askopenfilename()
    workbook = xlrd.open_workbook(fileName)
    worksheet = workbook.sheet_by_name('order')
    first_name_var.set(worksheet.cell(1,0).value)
    last_name_var.set(worksheet.cell(1,1).value)
    phone_number_var.set(worksheet.cell(1,2).value)
    address_var.set(worksheet.cell(1,3).value)
    city_var.set(worksheet.cell(1,4).value)
    postal_var.set(worksheet.cell(1,5).value)
    prov.set(worksheet.cell(1,6).value)
    credit_var.set(worksheet.cell(1,7).value)
    ccv_var.set(worksheet.cell(1,8).value)
    cc_exp_month_val.set(worksheet.cell(1,9).value)
    cc_exp_year_val.set(worksheet.cell(1,10).value)
    clicked.set(worksheet.cell(1,11).value)
    quantity_val.set(worksheet.cell(1,12).value)
def writeExcel(workSheet,workBook,makeBold, col,val):
    bold = workBook.add_format({'bold':makeBold})
    workSheet.write(col,val,bold)

def saveCurrOrder():
    fileName = asksaveasfilename(defaultextension='.xlsx')
    try:
        workBook = xlsxwriter.Workbook(fileName)
        workSheet = workBook.add_worksheet(name='order')
        writeExcel(workSheet,workBook, True, 'A1','First Name')
        writeExcel(workSheet,workBook, False, 'A2',first_name_var.get())

        writeExcel(workSheet,workBook, True, 'B1','Last Name')
        writeExcel(workSheet,workBook, False, 'B2',last_name_var.get())

        writeExcel(workSheet,workBook, True, 'C1','Phone #')
        writeExcel(workSheet,workBook, False, 'C2',phone_number_var.get())

        writeExcel(workSheet,workBook, True, 'D1','Address')
        writeExcel(workSheet,workBook, False, 'D2',address_var.get())

        writeExcel(workSheet,workBook, True, 'E1','City')
        writeExcel(workSheet,workBook, False, 'E2',city_var.get())

        writeExcel(workSheet,workBook, True, 'F1','Postal Code')
        writeExcel(workSheet,workBook, False, 'F2',postal_var.get())

        writeExcel(workSheet,workBook, True, 'G1','Province')
        writeExcel(workSheet,workBook, False, 'G2',prov.get())

        writeExcel(workSheet,workBook, True, 'H1','Credit Card #')
        writeExcel(workSheet,workBook, False, 'H2',credit_var.get())

        writeExcel(workSheet,workBook, True, 'I1','CCV')
        writeExcel(workSheet,workBook, False, 'I2',ccv_var.get())

        writeExcel(workSheet,workBook, True, 'J1','Expiry Month')
        writeExcel(workSheet,workBook, False, 'J2',cc_exp_month_val.get())

        writeExcel(workSheet,workBook, True, 'K1','Expiry Year')
        writeExcel(workSheet,workBook, False, 'K2',cc_exp_year_val.get())

        writeExcel(workSheet,workBook, True, 'L1','Pizza')
        writeExcel(workSheet,workBook, False, 'L2',clicked.get())

        writeExcel(workSheet,workBook, True, 'M1','Quantity')
        writeExcel(workSheet,workBook, False, 'M2',quantity_val.get())

        workBook.close()
    except:
        return

def endProgram():
    pass
root = Tk()
root.title("Order a pizza")
root.geometry("550x250")
root.resizable(False, False)
first_name = Label(root, text="First Name")
first_name_var = StringVar()
first_name_entry = Entry(root,textvariable=first_name_var) #first name

last_name_var= StringVar()
last_name = Label(root,text="Last Name")
last_name_entry = Entry(root,textvariable=last_name_var) #last name


phone_number_var= StringVar()
phone_number = Label(root, text="Phone #")
phone_number_entry = Entry(root,textvariable=phone_number_var)


address = Label(root,text="Address")
address_var= StringVar()
address_entry = Entry(root,textvariable=address_var)

city = Label(root,text="City")
city_var= StringVar()
city_entry = Entry(root,textvariable=city_var)

postal = Label(root,text="Postal Code")
postal_var= StringVar()
postal_entry = Entry(root,textvariable=postal_var)

prov = StringVar()
prov.set("ON")
province = OptionMenu(root,prov, "AL","BC","MB","NB","NL"
,"NS","NT","NU","ON","PE","QC","SK","YT")

credit = Label(root, text="Credit Card Number")
credit_var= StringVar()
credit_entry = Entry(root,textvariable=credit_var)


ccv = Label(root,text="CCV")
ccv_var = StringVar()
ccv_entry = Entry(root,textvariable=ccv_var)

cc_exp_month = Label(root,text="Exp")
cc_exp_month_val = StringVar()
cc_exp_month_entry = Entry(root,textvariable=cc_exp_month_val)

cc_exp_year = Label(root,text="Exp")
cc_exp_year_val = StringVar()
cc_exp_year_entry = Entry(root,textvariable=cc_exp_year_val)


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

quantity_val = StringVar()
quantity_val.set(1)
quantity = OptionMenu(root,quantity_val, "1","2","3","4","5","6","7","8")


accept = Button(root,text="Place Order!", command=run)
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

cc_exp_month.grid(row = 8, column=0)
cc_exp_month_entry.grid(row = 8, column=1)

cc_exp_year.grid(row = 8, column=4)
cc_exp_year_entry.grid(row = 8, column=5)

drop.grid(row = 10, column= 1)
quantity.grid(row = 10, column = 3)
accept.grid(row=10,column=5)

root.mainloop()