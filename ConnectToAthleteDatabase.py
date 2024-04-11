import mysql.connector
from mysql.connector import errorcode

import csv
import sys
import json

dataList = []
monthData = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June":0, "July": 0, "August": 0, "September":0,
             "October": 0, "November": 0, "December": 0}

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
        # dataCursor.execute(dataQuery, (dataList[i][0], firstName, lastName, birthDate))
    reservationConnection.commit()

    getBirthdateQuery = ("SELECT MONTH(Birthdate) "
                       "FROM Athlete")
    dataCursor.execute(getBirthdateQuery)
    for row in dataCursor.fetchall():
        if(row[0] == 1): monthData["January"] += 1
        if(row[0] == 2): monthData["February"] += 1
        if(row[0] == 3): monthData["March"] += 1
        if(row[0] == 4): monthData["April"] += 1
        if(row[0] == 5): monthData["May"] += 1
        if(row[0] == 6): monthData["June"] += 1
        if(row[0] == 7): monthData["July"] += 1
        if(row[0] == 8): monthData["August"] += 1
        if(row[0] == 9): monthData["September"] += 1
        if(row[0] == 1): monthData["October"] += 1
        if(row[0] == 1): monthData["November"] += 1
        if(row[0] == 1): monthData["December"] += 1

        print(monthData)

    print("")
    for month in monthData:
        string = "" + month + ": " + (10 - len(month))*" "
        for i in range(monthData[month]):
            string += "|"
        print(string)

    print("")
    reservationConnection.close()