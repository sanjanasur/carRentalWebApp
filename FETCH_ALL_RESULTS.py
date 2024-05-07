
import mysql.connector as mysql


mydb = mysql.connect(
        host="acadmysqldb001p.uta.edu",
        user="sxs9074",
        password="cPpyDGF@OMF2",
        database="sxs9074")

cursor = mydb.cursor()


print("Customers:")
cursor.execute("SELECT * FROM Customer")
customers = cursor.fetchall()
for customer in customers:
    print(customer)

print("Cars:")
cursor.execute("SELECT * FROM Car")
cars = cursor.fetchall()
for car in cars:
    print(car)

print("Owner:")
cursor.execute("SELECT * FROM Owner")
owners = cursor.fetchall()
for owner in owners:
    print(owner)

print("Rents:")
cursor.execute("SELECT * FROM Rents")
rents = cursor.fetchall()
for rent in rents:
    print(rent)

cursor.close()
mydb.close()