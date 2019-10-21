import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='m',
                                         user='root',
                                         password='student')

    sql_select_Query = "select * from m1"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of student is: ", cursor.rowcount)

    print("\nPrinting record")
    for row in records:
        
        print(row[0],row[1])

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
