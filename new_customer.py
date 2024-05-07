
import tkinter as tk
import mysql.connector as mysql


mydb = mysql.connect(
        host="xxx",
        user="xxx",
        password="xxx",
        database="xxx")

cursor = mydb.cursor()



def show_fields():
    customer_type = customer_type_var.get()


    IName_label.pack_forget()
    IName_entry.pack_forget()
    LName_label.pack_forget()
    LName_entry.pack_forget()
    BusinessName_label.pack_forget()
    BusinessName_entry.pack_forget()
    EmployeeName_label.pack_forget()
    EmployeeName_entry.pack_forget()
    Phone_label.pack_forget()
    Phone_entry.pack_forget()


    if customer_type == "Personal":
        IName_label.pack()
        IName_entry.pack()
        LName_label.pack()
        LName_entry.pack()
        Phone_label.pack()
        Phone_entry.pack()
        BusinessName_entry.delete(0, tk.END)
        EmployeeName_entry.delete(0, tk.END)
        Phone_entry.delete(0, tk.END)
    elif customer_type == "Business":
        BusinessName_label.pack()
        BusinessName_entry.pack()
        Phone_label.pack()
        Phone_entry.pack()
        IName_entry.delete(0, tk.END)
        LName_entry.delete(0, tk.END)
        EmployeeName_entry.delete(0, tk.END)
        Phone_entry.delete(0, tk.END)
    elif customer_type == "RentalEmployee":
        EmployeeName_label.pack()
        EmployeeName_entry.pack()
        Phone_label.pack()
        Phone_entry.pack()
        IName_entry.delete(0, tk.END)
        LName_entry.delete(0, tk.END)
        BusinessName_entry.delete(0, tk.END)
        Phone_entry.delete(0, tk.END)

def add_data():
    phone = Phone_entry.get()
    customer_type = customer_type_var.get()
    Iname = IName_entry.get()
    Lname = LName_entry.get()
    BusinessName = BusinessName_entry.get()
    Ename = EmployeeName_entry.get()

    insert_query = "INSERT INTO Customer (phone, customer_type, Iname, Lname, BusinessName, Ename) \
                    VALUES (%s, %s, %s, %s, %s, %s)"
    my_data = (phone, customer_type, Iname, Lname, BusinessName, Ename)

    cursor.execute(insert_query, my_data)
    mydb.commit()
    print("Data added successfully!")



rental_window = tk.Tk()


customer_type_var = tk.StringVar()


personal_radio = tk.Radiobutton(rental_window, text="Personal", variable=customer_type_var, value="Personal",
                                command=show_fields)
personal_radio.pack()

business_radio = tk.Radiobutton(rental_window, text="Business", variable=customer_type_var, value="Business",
                                command=show_fields)
business_radio.pack()

rental_employee_radio = tk.Radiobutton(rental_window, text="Rental Employee", variable=customer_type_var,
                                       value="RentalEmployee", command=show_fields)
rental_employee_radio.pack()


IName_label = tk.Label(rental_window, text="Enter Initial:")
IName_entry = tk.Entry(rental_window)

LName_label = tk.Label(rental_window, text="Enter Last Name:")
LName_entry = tk.Entry(rental_window)

BusinessName_label = tk.Label(rental_window, text="Enter Business Name:")
BusinessName_entry = tk.Entry(rental_window)

EmployeeName_label = tk.Label(rental_window, text="Enter Employee Name:")
EmployeeName_entry = tk.Entry(rental_window)

Phone_label = tk.Label(rental_window, text="Enter Phone Number:")
Phone_entry = tk.Entry(rental_window)

add = tk.Button(rental_window, text='Add Record', width=10, command=add_data)


IName_label.pack()
IName_entry.pack()
LName_label.pack()
LName_entry.pack()
Phone_label.pack()
Phone_entry.pack()
add.pack()

rental_window.mainloop()

