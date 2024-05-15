import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="252525",
        database="labormap"
    )

    # Set isolation level
    mydb.start_transaction(isolation_level='SERIALIZABLE')

    mycursor = mydb.cursor()

    mycursor.execute("INSERT INTO book (id, title, stock) VALUES (200, 'Shirley', 10)")

    mydb.commit()

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
