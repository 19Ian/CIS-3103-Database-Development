import mysql.connector
from mysql.connector import errorcode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.colors as mcolors

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
                       "FROM AthleteBiometrics")
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
                                "FROM AthleteBiometrics INNER JOIN AthleteSalary "
                                "ON AthleteBiometrics.AthleteID = AthleteSalary.AthleteID "
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
    # TODO:too many points to plot, DISTINCT
def Name_Weight_Height():
    getHeightWeightQuery = ("SELECT MONTH(Birthdate), AVG(Height) AS Height_CM, AVG(Weight) AS Weight_KG "
                                "FROM AthleteBiometrics "
                                "GROUP BY MONTH(Birthdate)"
                                "ORDER BY MONTH(Birthdate)")
    dataCursor.execute(getHeightWeightQuery)

    monthData2 = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June":0, "July": 0, "August": 0, "September":0,
             "October": 0, "November": 0, "December": 0}
    heights = []
    weights = []

    for row in dataCursor.fetchall():
        if(row[0] == 1): monthData2["January"] += 1
        if(row[0] == 2): monthData2["February"] += 1
        if(row[0] == 3): monthData2["March"] += 1
        if(row[0] == 4): monthData2["April"] += 1
        if(row[0] == 5): monthData2["May"] += 1
        if(row[0] == 6): monthData2["June"] += 1
        if(row[0] == 7): monthData2["July"] += 1
        if(row[0] == 8): monthData2["August"] += 1
        if(row[0] == 9): monthData2["September"] += 1
        if(row[0] == 10): monthData2["October"] += 1
        if(row[0] == 11): monthData2["November"] += 1
        if(row[0] == 12): monthData2["December"] += 1

        heights.append(row[1])
        weights.append(row[2]) 

    barWidth = 0.25
    br1 = np.arange(12) 
    br2 = [x + barWidth for x in br1]

    # PLOT BOTH
    plt.subplot(1,2,2)
    plt.bar(br1, weights, color =mcolors.to_rgb("cornflowerblue"), width = barWidth, 
            edgecolor ='grey', label ='Weights') 
    plt.bar(br2, heights, color =mcolors.to_rgb("mediumblue"), width = barWidth, 
            edgecolor ='grey', label ='Heights') 

    # Adding Xticks 
    plt.xlabel('Month', fontweight ='bold', fontsize = 15) 
    plt.ylabel('Heights(CM)/Weights(KG)', fontweight ='bold', fontsize = 15) 
    plt.xticks([r + barWidth for r in range(12)], 
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.legend()

    # PLOT WEIGHTS
    plt.subplot(2,2,1)
    plt.bar(br1, weights, color =mcolors.to_rgb("mediumpurple"), width = barWidth, 
            edgecolor ='grey', label ='Weights')

    # Adding Xticks 
    plt.xlabel('Month', fontweight ='bold', fontsize = 15) 
    plt.ylabel('Weights(KG)', fontweight ='bold', fontsize = 15) 
    plt.xticks([r for r in range(12)], 
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # PLOT HEIGHTS
    plt.subplot(2,2,3)
    plt.bar(br1, heights, color =mcolors.to_rgb("violet"), width = barWidth, 
            edgecolor ='grey', label ='Heights')

    # Adding Xticks 
    plt.xlabel('Month', fontweight ='bold', fontsize = 15) 
    plt.ylabel('Heights(CM)', fontweight ='bold', fontsize = 15)

    plt.xticks([r for r in range(12)], 
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    plt.show()

#### GET NUM_ATHLETES IN NATIONALITIES ####
def Num_Athletes_Nationalities_Bar():
    getNumAthletesQuery = ("SELECT Nationality AS Country, COUNT(*) AS Count "
                                "FROM Athlete "
                                "GROUP BY Nationality "
                                "ORDER BY Nationality; ")
    dataCursor.execute(getNumAthletesQuery)

    countries = []
    counts = []
    
    for row in dataCursor.fetchall():
        if row[1] > 500:
            countries.append(row[0])
            counts.append(row[1])

    fig = plt.figure(figsize = (13, 5))

    # creating the bar plot
    plt.bar(countries, counts, color ='gray', 
            width = 0.1)
    plt.tick_params(axis='x', which='major', labelsize=5)

    plt.xlabel("Country")
    plt.ylabel("Num Athletes")
    plt.title("Number of Athletes Born in Each Country")
    plt.show()


#### PLOTS ####
# Born_In_Months()
# Birthmonth_Salary_Bar()
Name_Weight_Height()
# Num_Athletes_Nationalities_Bar()


reservationConnection.close()