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
    # Define the SQL query to select delivery dates and actual delivery dates
    product_query = "SELECT * FROM delivery;"
    
    # Execute the SQL query
    cursor.execute(product_query)
    
    # Fetch all rows from the result set
    products = cursor.fetchall()

    print("\n--DISPLAYING Delivery Information REPORT--\n")
    for product in products:
        print("Supplier Name: {}\nExpected Delivery Percent: {}\nJanuary Delivery: {}\nFebruary Delivery: {}\nMarch Delivery: {}\nApril Delivery: {}\nMay Delivery: {}\nJune Delivery: {}\nJuly Delivery: {}\nAugust Deliver: {}\nSeptember Deliver: {}\nOctober Delivery: {}\nNovember Deliver: {}\nDecember Delivery: {}\n".format(product[0], product[1], product[2], product[3], product[4], product[5], product[6], product[7], product[8], product[9], product[10], product[11], product[12], product[13]))

finally:
    # Close the cursor and database connection
    cursor.close()
    db.close()