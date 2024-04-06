import mysql.connector
from mysql.connector import errorcode

import csv

dataList = []

with open('archive (2)/fm2023.csv', encoding="utf8") as f:
    readObj = csv.reader(f)
    for row in readObj:
        dataList.append(row)

# print(dataList[1])


try: 
    reservationConnection = mysql.connector.connect(
        user='root',
        password='sqlSERVER19!',
        host='127.0.0.1',
        database='athleterecords')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("invalid connection")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database not found")
    else:
        print("cannot connect to database: ", err)

else:
    dataCursor = reservationConnection.cursor()

    for i in range(1,5):
        dataQuery = ("INSERT INTO Athlete "
                    "(ID, FirstName, LastName, BirthDate) "
                    "VALUES (%d, %s, %s, %s);"
                    )
        print(dataList[i][0], dataList[i][2], dataList[i][2], dataList[i][3])
        dataCursor.execute(dataQuery, (dataList[i][0], dataList[i][2], dataList[i][2], dataList[i][3]))
        # dataCursor.execute(dataQuery, (1, "testName", "testName", "testDate"))

    reservationConnection.commit()
    reservationConnection.close()