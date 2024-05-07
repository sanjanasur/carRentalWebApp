import tkinter as tk
import mysql.connector as mysql


mydb = mysql.connect(
        host="xxx",
        user="xxx",
        password="xxx",
        database="xxx")

cursor = mydb.cursor()


def add_data_for_car():
    CustomerID = CustomerID_entry.get()
    CarID = CarID_entry.get()
    RentalType = RentalType_entry.get()

    cursor.execute("SELECT Status FROM rents WHERE CarID = %s AND CustomerID = %s", (CarID, CustomerID,))
    Status = cursor.fetchone()

    if Status and Status[0] == "Active":
        cursor.execute("SELECT DailyRate, WeeklyRate, EmpSplRate FROM CAR WHERE VehicleID = %s", (CarID,))
        car_data = cursor.fetchone()
        DailyRate, WeeklyRate, EmpSplRate = car_data


        cursor.execute("SELECT NoOfDays, NoOfWeeks FROM RENTS WHERE CarID = %s", (CarID,))
        rent_data = cursor.fetchone()
        NoOfDays, NoOfWeeks = rent_data


        if RentalType == "Personal":
            AmountDue = NoOfDays * DailyRate
        elif RentalType == "Bank":
            AmountDue = NoOfWeeks * WeeklyRate
        else:
            AmountDue = NoOfDays * EmpSplRate


        update_query_rent = "UPDATE RENTS SET AmountDue = %s, Status = 'Returned' WHERE CustomerID = %s AND CarID = %s"
        cursor.execute(update_query_rent, (AmountDue, CustomerID, CarID))
        mydb.commit()

        print("Amount due updated successfully!")
    else:
        print("Car status is not active. Cannot calculate amount due.")


rental_window = tk.Tk()
rental_window.title("Add Rental Data")


CustomerID_label = tk.Label(rental_window, text="Enter Customer ID:")
CustomerID_entry = tk.Entry(rental_window)
CustomerID_label.pack()
CustomerID_entry.pack()

CarID_label = tk.Label(rental_window, text="Enter Car ID:")
CarID_entry = tk.Entry(rental_window)
CarID_label.pack()
CarID_entry.pack()

RentalType_label = tk.Label(rental_window, text="Enter Rental Type (Personal/Business/Rental):")
RentalType_entry = tk.Entry(rental_window)
RentalType_label.pack()
RentalType_entry.pack()


add_record = tk.Button(rental_window, text='Add Rental Data', width=15, command=add_data_for_car)
add_record.pack()


rental_window.mainloop()
