import mysql.connector
from mysql.connector import errorcode
import numpy as np
import matplotlib.pyplot as plt 

import csv
import sys
import json

dataList = []
monthData = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June":0, "July": 0, "August": 0, "September":0,
             "October": 0, "November": 0, "December": 0}

with open('fm2023.csv', encoding="utf8") as f:
    readObj = csv.reader(f)
    for row in readObj:
        dataList.append(row)


if __name__ == "__main__":  
    ## Get the configuration file 
    configFileLocation = sys.argv[1]  
    print("Configuration file location: {0}".format(configFileLocation))   
    configFile = open(configFileLocation)
    configFileJSON = json.load(configFile)


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
    #### INSERT DATA INTO ATHLETE TABLE ####
    for i in range(1,189333):
        
        insertIntoAthlete = ("INSERT IGNORE INTO Athlete "
            "(ID, FirstName, LastName, Nationality) "
            "VALUES (%s, %s, %s, %s);"
            )
        
        insertIntoAthleteBiometrics = ("INSERT IGNORE INTO AthleteBiometrics "
            "(AthleteID, Birthdate, Foot, Height, Weight, Age) "
            "VALUES (%s, %s, %s, %s, %s, %s);"
            )
        
        insertIntoAthleteSalary = ("INSERT IGNORE INTO AthleteSalary "
            "(AthleteID, Salary, Club) "
            "VALUES (%s, %s, %s);"
            )
        

        #Setup ID
        athleteID = dataList[i][0]

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

        #Setup Salary
        salary = dataList[i][16].split()[0][1:]
        if(salary == '' or salary == '/A'):
            salary = "00000"
        else:
            salary = salary.replace(',','')

        #Setup Foot
        foot = dataList[i][8].split()[0]

        #Setup Height Weight Age
        height = dataList[i][12].split()[0]
        weight = dataList[i][13].split()[0]
        age = dataList[i][14]

        #Setup Nationality
        nationality = dataList[i][4]

        #Setup Club
        club = dataList[i][6]
        
        dataCursor.execute(insertIntoAthleteBiometrics, (athleteID, birthDate, foot, int(height), int(weight), int(age)))
        dataCursor.execute(insertIntoAthleteSalary, (athleteID, int(salary), club))
        dataCursor.execute(insertIntoAthlete, (athleteID, firstName, lastName, nationality))

    reservationConnection.commit()
    reservationConnection.close()