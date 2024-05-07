
import tkinter as tk
import mysql.connector as mysql

mydb = mysql.connect(
        host="xxx",
        user="xxx",
        password="xxx",
        database="xxx")

cursor = mydb.cursor()


def add_data_for_car():
        VehicleType = VType_entry.get()
        VehicleModel = VModel_entry.get()
        Year = Year_entry.get()
        Category = category_entry.get()
        DailyRate = get_regular_rate(VehicleType, Category)
        WeeklyRate = DailyRate * 7
        EmpSplRate = DailyRate * 0.8
        OwnerId=ownerID_entry.get()

        insert_query_car = "INSERT INTO Car (VehicleModel, Year, VehicleType, Category, DailyRate, WeeklyRate, EmpSplRate, OwnerId) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        my_data_for_car = (VehicleModel, Year, VehicleType, Category, DailyRate, WeeklyRate, EmpSplRate, OwnerId)


        cursor.execute(insert_query_car, my_data_for_car)
        mydb.commit()
        print("Data added successfully for car!")


def get_regular_rate(vtype, category):
        if vtype == "Compact":
                if category == "Luxury":
                        return 50 * 1.2
                else:
                        return 50
        elif vtype == "Medium":
                if category == "Luxury":
                        return 70 * 1.2
                else:
                        return 70
        elif vtype == "Large":
                if category == "Luxury":
                        return 90 * 1.2
                else:
                        return 90
        elif vtype == "SUV":
                if category == "Luxury":
                        return 110 * 1.2
                else:
                        return 110
        elif vtype == "Truck":
                if category == "Luxury":
                        return 130 * 1.2
                else:
                        return 130
        elif vtype == "Van":
                if category == "Luxury":
                        return 150 * 1.2
                else:
                        return 150
        else:
                return 0



rental_window = tk.Tk()
rental_window.title("Add Car Data")


VType_label = tk.Label(rental_window, text="Enter Vehicle Type:")
VType_entry = tk.Entry(rental_window)
VType_label.pack()
VType_entry.pack()

Year_label = tk.Label(rental_window, text="Enter Year:")
Year_entry = tk.Entry(rental_window)
Year_label.pack()
Year_entry.pack()

VModel_label = tk.Label(rental_window, text="Enter Vehicle Model:")
VModel_entry = tk.Entry(rental_window)
VModel_label.pack()
VModel_entry.pack()

category_label = tk.Label(rental_window, text="Enter Category of Car:")
category_entry = tk.Entry(rental_window)
category_label.pack()
category_entry.pack()

ownerID_label = tk.Label(rental_window, text="Enter Owner ID:")
ownerID_entry = tk.Entry(rental_window)
ownerID_label.pack()
ownerID_entry.pack()


add_record = tk.Button(rental_window, text='Add Record', width=10, command=add_data_for_car)
add_record.pack()

rental_window.mainloop()
