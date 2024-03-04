import mysql.connector
from mysql.connector import errorcode

config = {
        'user': "root",
        'password': "bellevue",
        'host': 'localhost',
        'database': 'Bacchus',
        'raise_on_warnings': True
    }

db = mysql.connector.connect(**config)
print("\nDatabase user (root) connected to MySQL on host (localhost) with database (Bacchus).")


cursor = db.cursor()

try:
   
#product sales report    
    product_query = "SELECT product_sales, distributor_id, product_name FROM distribution;"
    cursor.execute(product_query)
    product = cursor.fetchall()

    print("\n--DISPLAYING Annual Product Sales REPORT--\n")
    for product_sales in product:
        print("Product Sales (in units): {}\nProduct ID: {}\nProduct Name: {}\n".format(product_sales[0], product_sales[1], product_sales[2]))


#total hours of last 4 quarters for each employee
    print("\n--DISPLAYING Last Four Quarters Total Hours REPORT--\n")

    total_hours1 = "SELECT SUM(quarters*quarterly_hours) AS total_hours FROM employee1 WHERE employee_id = 1;"
    cursor.execute(total_hours1)
    stan = cursor.fetchall()

    for employee_id in stan:
        print("Stan Bacchus: {}".format(stan[0]))


    total_hours2 = "SELECT SUM(quarters*quarterly_hours) AS total_hours FROM employee1 WHERE employee_id = 2;"
    cursor.execute(total_hours2)
    davis = cursor.fetchall()

    for employee_id in davis:
        print("Davis Bacchus: {}".format(davis[0]))

    total_hours3 = "SELECT SUM(quarters*quarterly_hours) AS total_hours FROM employee1 WHERE employee_id = 3;"
    cursor.execute(total_hours3)
    janet = cursor.fetchall()

    for employee_id in janet:
        print("Janet Collins: {}".format(janet[0]))

    total_hours4 = "SELECT SUM(quarters*quarterly_hours) AS total_hours FROM employee1 WHERE employee_id = 4;"
    cursor.execute(total_hours4)
    roz = cursor.fetchall()

    for employee_id in roz:
        print("Roz Murphy: {}".format(roz[0]))


    total_hours5 = "SELECT SUM(quarters*quarterly_hours) AS total_hours FROM employee1 WHERE employee_id = 5;"
    cursor.execute(total_hours5)
    bob = cursor.fetchall()

    for employee_id in bob:
        print("Bob Ulrich: {}".format(bob[0]))


    total_hours6 = "SELECT SUM(quarters*quarterly_hours) AS total_hours FROM employee1 WHERE employee_id = 6;"
    cursor.execute(total_hours6)
    henry = cursor.fetchall()

    for employee_id in henry:
        print("Henry Doyle: {}".format(henry[0]))


    total_hours7 = "SELECT SUM(quarters*quarterly_hours) AS total_hours FROM employee1 WHERE employee_id = 7;"
    cursor.execute(total_hours7)
    maria = cursor.fetchall()

    for employee_id in maria:
        print("Maria Costanza: {}\n".format(maria[0]))

finally:
   
    cursor.close()
    db.close()
