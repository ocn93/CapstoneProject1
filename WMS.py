import pandas as pd
from datetime import date

#Project Warehouse Management System
#Beginning Data
begbal = {
    "Product 1" : {
        "Product Type" : "Dining Chair",
        "Quantity" : 50
    },
        "Product 2" : {
        "Product Type" : "Dining Table",
        "Quantity" : 20
    },
        "Product 3" : {
        "Product Type" : "Bed 160",
        "Quantity" : 20
    },
        "Product 4" : {
        "Product Type" : "Bed 180",
        "Quantity" : 30
    },        
}
goodreceipt = {
    "Product 1" : {
        "Product Type" : "Dining Chair",
        "Quantity" : 10,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },
        "Product 2" : {
        "Product Type" : "Dining Table",
        "Quantity" : 20,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },
        "Product 3" : {
        "Product Type" : "Bed 160",
        "Quantity" : 40,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },
        "Product 4" : {
        "Product Type" : "Bed 180",
        "Quantity" : 50,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },        
}
salesorder = {
    "Product 1" : {
        "Product Type" : "Dining Chair",
        "Quantity" : 10,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },
        "Product 2" : {
        "Product Type" : "Dining Table",
        "Quantity" : 10,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },
        "Product 3" : {
        "Product Type" : "Bed 160",
        "Quantity" : 5,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },
        "Product 4" : {
        "Product Type" : "Bed 180",
        "Quantity" : 10,
        "Date" : date(2023,12,1).strftime("%m/%d/%Y")
    },       
}

#Login Modul
username = input("Username = ")
password = input("Password = ")
while username != "ocan" or password != "1234":
    print("Please Re-enter your Username and Password")
    username = input("Username = ")
    password = input("Password = ")
    continue
print("Login Successful\n")

#Menu for WMS
def menu() :
    print("Warehouse Management System","\n" 
          "1. Stock Qty Report", "\n" 
          "2. Good Receipt", "\n" 
          "3. Sales Order", "\n"
          "4. Stock Adjustment")
menu()
inputmenu = int(input("Please type the number of report you want to select = "))

if inputmenu == 1 :
    i = 1
    while i <= len(goodreceipt) :
        namaproduct = "Product "+str(i)
        begbal[namaproduct]["Quantity"] = begbal[namaproduct]["Quantity"] + goodreceipt[namaproduct]["Quantity"] - salesorder[namaproduct]["Quantity"]
        i +1
        break
    
    print("Inventory Report")
    inventoryreport = pd.DataFrame.from_dict(begbal)
    print(inventoryreport)

#Menu for Good Receipt    
if inputmenu == 2 :
    def goodreceiptmenu() :
        print("Good Receipt","\n"
            "1. Create Receipt Order", "\n" 
            "2. Good Receipt Report", "\n") 
    goodreceiptmenu()
    inputmenugr = int(input("Please type the number of action you want to select = "))
    if inputmenugr == 1 :
        productname = input("Product Name = ")
        if productname in goodreceipt :
            print("\nExisting Product\n")
            print("Product Type :",begbal[productname]["Product Type"])
            print("Quantity :",begbal[productname]["Quantity"],"\n")
            inputreceipt = input("Is this the product you wish to update? If Yes, type Yes = ")
            while inputreceipt == "Yes" :
                inputquantityreceipt = int(input("Input Quantity Receipt = "))
                inputdatereceipt = input("Date Receipt (DD/MM/YYYY) = ")
                begbal[productname]["Quantity"] = inputquantityreceipt + goodreceipt[productname]["Quantity"] + begbal[productname]["Quantity"] - salesorder[productname]["Quantity"]
                goodreceipt[productname]["Quantity"] = inputquantityreceipt + goodreceipt[productname]["Quantity"]
                goodreceipt[productname]["Date"] = inputdatereceipt
                print("Data Sucessfully Updated")
                print(begbal[productname])
                break
        else : 
            print("New Product")
            print("Please Input Product's Information Below \n")
            productname2 = productname
            print("Product Name = ",productname2)
            producttype = input("Product Type = ")
            quantityrcpt = int(input("Quantity = "))
            datereceipt = input("Date Receipt (DD/MM/YYYY) = ")
            goodreceipt[productname] = {"Product Type" :  producttype, "Quantity" : quantityrcpt,"Date" : datereceipt}
            begbal[productname] = {"Product Type" :  producttype, "Quantity" : quantityrcpt}
            print("Data has Sucessfully Added")
            
    else :
        print("Good Receipt Report")
        grreport = pd.DataFrame.from_dict(goodreceipt)
        print(grreport)

#Menu for Sales Order  
if inputmenu == 3 :
    def salesordermenu() :
        print("Sales Order","\n"
            "1. Create Sales Order", "\n" 
            "2. Sales Order Report", "\n") 
    salesordermenu()
    inputmenuso = int(input("Please type the number of action you want to select = "))
    if inputmenuso == 1 :
        productname = input("Product Name = ")
        if productname in salesorder :
            print("\nExisting Product\n")
            print("Product Type :",begbal[productname]["Product Type"])
            print("Quantity :",begbal[productname]["Quantity"],"\n")
            inputorder = input("Is this the product the customer wish to order? If Yes, type Yes = ")
            while inputorder == "Yes" :
                inputquantityorder = int(input("Input Quantity Order = "))
                inputdateorder = input("Date Order (DD/MM/YYYY) = ")
                begbal[productname]["Quantity"] = goodreceipt[productname]["Quantity"] + begbal[productname]["Quantity"] - salesorder[productname]["Quantity"] - inputquantityorder
                salesorder[productname]["Quantity"] = inputquantityorder + salesorder[productname]["Quantity"]
                salesorder[productname]["Date"] = inputdateorder
                print(begbal[productname])
                break
        else : 
            print("Product You Wish to Order is not there in the System. Please, Contact and Confirm with the Customer")
            
    else :
        print("Sales Order Report")
        soreport = pd.DataFrame.from_dict(salesorder)
        print(soreport)
#Menu for Stock Adjustemnt
if inputmenu == 4 :
    def stockadjustmentmenu() :
        print("Stock Adjustment","\n"
            "1. Inactive Product", "\n" 
            "2. Stock Adjustment", "\n") 
    stockadjustmentmenu()
    inputmenusa = int(input("Please type the number of action you want to select = "))
    if inputmenusa == 1 :
        productname = input("Product Name = ")
        if productname in begbal :
            print("\nExisting Product\n")
            print("Quantity :",begbal[productname]["Quantity"],"\n")
            inputinactive = input("Is this the product the customer wish to inactive? If Yes, type Yes = ")
            while inputinactive == "Yes" :
                del begbal[productname]
                print("Product Successfully Adjusted")
                inventoryreport = pd.DataFrame.from_dict(begbal)
                print(inventoryreport)
                break
            else : print("Thank You")
    else : 
        productname = input("Product Name = ")
        if productname in begbal :
            print("\nExisting Product\n")
            print("Product Type :",begbal[productname]["Product Type"])
            print("Quantity :",begbal[productname]["Quantity"],"\n")
            inputorder = input("Is this the product you wish to adjust? If Yes, type Yes = ")
            inputquantitadjustment = int(input("Input Quantity Adjust = "))
            begbal[productname]["Quantity"] = inputquantitadjustment
            print("Product Successfully Adjusted")
            inventoryreport = pd.DataFrame.from_dict(begbal)
            print(inventoryreport)
        else : print("Please Reconfirm the Product. Thank You")
 


