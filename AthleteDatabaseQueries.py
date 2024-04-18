import mysql.connector
from mysql.connector import errorcode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

import csv
import sys
import json

monthData = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June":0, "July": 0, "August": 0, "September":0,
             "October": 0, "November": 0, "December": 0}

# print(dataList[1])

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

#### SETUP MONTH DATA
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
    if(row[0] == 10): monthData["October"] += 1
    if(row[0] == 11): monthData["November"] += 1
    if(row[0] == 12): monthData["December"] += 1


month = list(monthData.keys())
values = list(monthData.values())


#### ATHLETES BORN IN MONTHS BAR CHART ####
def Born_In_Months():

    fig = plt.figure(figsize = (13, 5))

    # creating the bar plot
    plt.bar(month, values, color ='maroon', 
            width = 0.3)

    plt.xlabel("Month of the Year")
    plt.ylabel("No. of athletes born")
    plt.title("Athletes Born In Months")
    plt.show()

#### GET BIRTHMONTH, SALARY BAR GRAPH ####
def Birthmonth_Salary_Bar():
    getBirthdateSalaryQuery = ("SELECT MONTH(Birthdate), AVG(Salary) AS AVG_Salary_Pounds "
                                "FROM Athlete "
                                "GROUP BY MONTH(Birthdate) "
                                "ORDER BY MONTH(Birthdate);")
    dataCursor.execute(getBirthdateSalaryQuery)

    firstNames = []
    lastNames = []
    months = []
    salaries = []
    
    for row in dataCursor.fetchall():
        months.append(row[0])
        salaries.append(row[1])

    fig = plt.figure(figsize = (13, 5))

    # creating the bar plot
    plt.bar(month, salaries, color ='maroon', 
            width = 0.3)

    plt.xlabel("Month of the Year")
    plt.ylabel("AVG Salary of Athletes")
    plt.title("Salary's of Athletes Born in Months")
    plt.show()
    # plt.savefig('plot3.png')


#### GET NAME, WEIGHT, HEIGHT ####
    # TODO:too many points to plot
def Name_Weight_Height(firstRow, lastRow):
    getHeightWeightQuery = ("SELECT FirstName, LastName, Height AS Height_CM, Weight AS Weight_KG "
                                "FROM Athlete "
                                "ORDER BY LastName DESC;")
    dataCursor.execute(getHeightWeightQuery)

    firstNames = []
    lastNames = []
    heights = []
    weights = []

    data = dataCursor.fetchall()

    for i in range(firstRow,lastRow):
        firstNames.append(data[i][0])
        lastNames.append(data[i][1])
        heights.append(data[i][2])
        weights.append(data[i][3])
    
    # for row in dataCursor.fetchall():
    #     firstNames.append(row[0])
    #     lastNames.append(row[1])
    #     heights.append(row[2])
    #     weights.append(row[3])

    fig = plt.figure(figsize = (14, 10))
    plt.scatter(heights, weights)
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Height and Weight")

    for i, txt in enumerate(lastNames):
        plt.annotate(txt, (heights[i], weights[i]), fontsize=5)

    plt.show()


#### PLOTS ####
# Born_In_Months()
# Birthmonth_Salary_Bar()
Name_Weight_Height(50000, 51000)


reservationConnection.close()