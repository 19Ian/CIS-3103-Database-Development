import mysql.connector
from mysql.connector import errorcode

import csv
import sys
import json

dataList = []

with open('archive (2)/fm2023.csv', encoding="utf8") as f:
    readObj = csv.reader(f)
    for row in readObj:
        dataList.append(row)

# print(dataList[1])

if __name__ == "__main__":  
    ## Get the configuration file 
    configFileLocation = sys.argv[1]  
    print("Configuration file location: {0}".format(configFileLocation))   
    configFile = open(configFileLocation)
    configFileJSON = json.load(configFile)
    # print("user: " + configFileJSON["user"])
    # print("password: " + configFileJSON["password"])
    # print("host: " + configFileJSON["host"])
    # print("database: " + configFileJSON["database"])


def setupConnection(user, password, host, database):
    reservationConnection = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database)
    return reservationConnection

try: 
    reservationConnection = setupConnection(configFileJSON["user"], configFileJSON["password"], configFileJSON["host"], configFileJSON["database"])

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("invalid connection")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database not found")
    else:
        print("cannot connect to database: ", err)

else:
    dataCursor = reservationConnection.cursor()

    for i in range(1,100):
        dataQuery = ("INSERT INTO Athlete "
                    "(ID, FirstName, LastName, Birthdate) "
                    "VALUES (%s, %s, %s, %s);"
                    )
        #Setup Date
        date = dataList[i][3].split()[0]
        day = date.split("/")[0]
        if len(day) == 1:
            day = "0" + day
        month = date.split("/")[1]
        if len(month) == 1:
            month = "0" + month
        year = date.split("/")[2]
        birthDate = year + "-" + month + "-" + day

        #Setup Name
        firstName = dataList[i][2].split()[0]
        if len(dataList[i][2].split()) == 2:
            lastName = dataList[i][2].split()[1]
        else:
            lastName = ""
        dataCursor.execute(dataQuery, (dataList[i][0], firstName, lastName, birthDate))
    reservationConnection.commit()
    reservationConnection.close()