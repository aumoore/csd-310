
import mysql.connector
from  mysql.connector import errorcode

config = {
    "user": "root",
    "password": "bellevue",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try: 
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    #Display for studio records
    cursor.execute("SELECT studio_id, studio_name FROM studio")

    result = cursor.fetchall()

    print("-- DISPLAYING Studio RECORDS --")
    for x in result:

        print("Studio ID: {}\nStudio Name: {}\n".format(x[0], x[1])) 

    #Display for genre records
    cursor.execute("SELECT genre_id, genre_name FROM genre")

    result = cursor.fetchall()

    print("-- DISPLAYING Genre RECORDS --")
    for x in result:

        print("Genre ID: {}\nGenre Name: {}\n".format(x[0], x[1]))

    
    #Display for short film records
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")

    result = cursor.fetchall()

    print("-- DISPLAYING Short Film RECORDS --")
    for x in result:

        print("Film Name: {}\nRuntime: {}\n".format(x[0], x[1]))


    #Display directors in order
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

    result = cursor.fetchall()

    print("-- DISPLAYING Director RECORDS in Order --")
    for x in result:

        print("Film Name: {}\nDirector: {}\n".format(x[0], x[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()




