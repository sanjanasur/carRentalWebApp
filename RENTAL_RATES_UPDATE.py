import tkinter as tk
import mysql.connector as mysql
from tkinter import messagebox

mydb = mysql.connect(
        host="xxx",
        user="xxx",
        password="xxx",
        database="xxx")

cursor = mydb.cursor()


def add_data_for_car():
    OwnerId = OwnerId_entry.get()
    VehicleType = VehicleType_entry.get()
    Category = Category_entry.get()
    DailyRate = float(DailyRate_entry.get())
    WeeklyRate = float(WeeklRate_entry.get())
    EmpSplRate = 0.8 * DailyRate

    try:
        cursor.execute("UPDATE Car SET DailyRate = %s, WeeklyRate = %s, EmpSplRate = %s WHERE OwnerId = %s AND VehicleType = %s",
                       (DailyRate, WeeklyRate, EmpSplRate, OwnerId, VehicleType))
        mydb.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
    except mysql.Error as e:
        messagebox.showerror("Error", f"Error updating data: {e}")


rental_window = tk.Tk()
rental_window.title("Add Rental Data")


OwnerId_label = tk.Label(rental_window, text="Owner ID:")
OwnerId_label.pack()
OwnerId_entry = tk.Entry(rental_window)
OwnerId_entry.pack()

VehicleType_label = tk.Label(rental_window, text="Vehicle Type:")
VehicleType_label.pack()
VehicleType_entry = tk.Entry(rental_window)
VehicleType_entry.pack()

Category_label = tk.Label(rental_window, text="Category:")
Category_label.pack()
Category_entry = tk.Entry(rental_window)
Category_entry.pack()

DailyRate_label = tk.Label(rental_window, text="Daily Rate:")
DailyRate_label.pack()
DailyRate_entry = tk.Entry(rental_window)
DailyRate_entry.pack()

WeeklyRate_label = tk.Label(rental_window, text="Weekly Rate:")
WeeklyRate_label.pack()
WeeklRate_entry = tk.Entry(rental_window)
WeeklRate_entry.pack()


add_record = tk.Button(rental_window, text='Add Rental Data', width=15, command=add_data_for_car)
add_record.pack()

rental_window.mainloop()
