import tkinter as tk
import mysql.connector as mysql
from datetime import datetime, timedelta, date
from tkinter import messagebox


mydb = mysql.connect(
        host="xxx",
        user="xxx",
        password="xxx",
        database="xxx")

cursor = mydb.cursor()

def add_data_for_car():
    CustomerID = CustomerID_entry.get()
    VehicleType = VehicleType_var.get()
    Category = category_entry.get()
    RentalType = RentalType_var.get()
    StartDate = datetime.strptime(StartDate_entry.get(), "%Y-%m-%d")


    if RentalType == "Personal":
        NoOfDays = NoOfDays_entry.get()
        NoOfDays = int(NoOfDays) if NoOfDays else 0
        ReturnDate = StartDate + timedelta(days=NoOfDays)
        NoOfWeeks = 0
    else:
        NoOfWeeks = NoOfWeeks_entry.get()
        NoOfWeeks = int(NoOfWeeks) if NoOfWeeks else 0
        ReturnDate = StartDate + timedelta(weeks=NoOfWeeks)
        NoOfDays = 0

    StartDate = datetime.combine(StartDate, datetime.min.time())
    ReturnDate = datetime.combine(ReturnDate, datetime.min.time())


    cursor.execute("SELECT VehicleID FROM CAR WHERE VehicleType = %s AND Category = %s",
                   (VehicleType, Category,))
    car_data = [car[0] for car in cursor.fetchall()]
    for car_id in car_data:
        cursor.execute("SELECT StartDate, ReturnDate FROM rents WHERE CarID = %s", (car_id,))
        rent_data = cursor.fetchall()
        if rent_data:
            for rent_start_date, rent_return_date in rent_data:
                rent_start_date = datetime.combine(rent_start_date, datetime.min.time())
                rent_return_date = datetime.combine(rent_return_date, datetime.min.time())
                if (rent_start_date <= StartDate <= rent_return_date) or (
                        rent_start_date <= ReturnDate <= rent_return_date):

                    tk.messagebox.showerror("Error", "Car is not available for the selected dates.")
                    return


    CarID = car_data[0] if car_data else None


    Status = "Active" if StartDate == datetime.now().date() else "Scheduled"
    insert_query_rent = "INSERT INTO RENTS (CarID, CustomerID, RentalType, NoOfDays, NoOfWeeks, StartDate, ReturnDate,AmountDue, Status) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s,  %s, %s)"

    my_data_for_car = (CarID, CustomerID, RentalType, NoOfDays, NoOfWeeks, StartDate.strftime("%Y-%m-%d"), ReturnDate.strftime("%Y-%m-%d"),0, Status)

    cursor.execute(insert_query_rent, my_data_for_car)
    mydb.commit()

    print("Data added successfully for car!")


def rental_type_selected():
    if RentalType_var.get() == "Personal":
        NoOfDays_label.pack()
        NoOfDays_entry.pack()
        NoOfWeeks_label.pack_forget()
        NoOfWeeks_entry.pack_forget()
    else:
        NoOfDays_label.pack_forget()
        NoOfDays_entry.pack_forget()
        NoOfWeeks_label.pack()
        NoOfWeeks_entry.pack()


rental_window = tk.Tk()
rental_window.title("Add Rental Data")


CustomerID_label = tk.Label(rental_window, text="Enter Customer ID:")
CustomerID_entry = tk.Entry(rental_window)
CustomerID_label.pack()
CustomerID_entry.pack()

VehicleType_label = tk.Label(rental_window, text="Select Vehicle Type:")
VehicleType_var = tk.StringVar()
VehicleType_var.set("Compact")
vehicle_types = [("Compact"), ("Medium"), ("Large"), ("SUV"), ("Truck"), ("Van")]
for vehicle_type in vehicle_types:
    radio = tk.Radiobutton(rental_window, text=vehicle_type, variable=VehicleType_var, value=vehicle_type)
    radio.pack(anchor='w')
VehicleType_label.pack()

category_label = tk.Label(rental_window, text="Enter Category of Car:")
category_entry = tk.Entry(rental_window)
category_label.pack()
category_entry.pack()

RentalType_label = tk.Label(rental_window, text="Select Rental Type:")
RentalType_var = tk.StringVar()
RentalType_var.set("Personal")
rental_types = [("Rental"), ("Bank"), ("Personal")]
for rental_type in rental_types:
    radio = tk.Radiobutton(rental_window, text=rental_type, variable=RentalType_var, value=rental_type, command=rental_type_selected)
    radio.pack(anchor='w')
RentalType_label.pack()

NoOfWeeks_label = tk.Label(rental_window, text="Enter Number of Weeks:")
NoOfWeeks_entry = tk.Entry(rental_window)
NoOfWeeks_label.pack()
NoOfWeeks_entry.pack()

NoOfDays_label = tk.Label(rental_window, text="Enter Number of Days:")
NoOfDays_entry = tk.Entry(rental_window)
NoOfDays_label.pack()
NoOfDays_entry.pack()

StartDate_label = tk.Label(rental_window, text="Enter Start Date (YYYY-MM-DD):")
StartDate_entry = tk.Entry(rental_window)
StartDate_label.pack()
StartDate_entry.pack()


add_record = tk.Button(rental_window, text='Add Rental Data', width=15, command=add_data_for_car)
add_record.pack()


rental_window.mainloop()
