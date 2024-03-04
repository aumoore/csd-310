import mysql.connector
from mysql.connector import errorcode

config = {
        "user": "root",
        "password": "bellevue",
        "host": "localhost",
        "database": "Bacchus",
        "raise_on_warnings": True
    }

db = mysql.connector.connect(**config)
print("\nDatabase user (root) connected to MySQL on host (localhost) with database (Bacchus).")


cursor = db.cursor()

try:
    
    product_query1 = "SELECT employee_id, quarterly_hours FROM employee1 ;"
    cursor.execute(product_query1)
    employee1 = cursor.fetchall()

    print("\nData from employee quarterly_hours table:")
    for quarterly_hours in employee1:
        print(quarterly_hours)

finally:
   
    cursor.close()
    db.close()

