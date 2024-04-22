SELECT * 
FROM Athlete
INNER JOIN AthleteBiometrics ON ID = AthleteID
INNER JOIN AthleteSalary ON AthleteSalary.AthleteID = AthleteBiometrics.AthleteID;

SELECT FirstName, LastName, Birthdate, Salary AS Salary_Pounds
FROM Athlete
INNER JOIN AthleteBiometrics ON ID = AthleteID
INNER JOIN AthleteSalary ON AthleteSalary.AthleteID = AthleteBiometrics.AthleteID
ORDER BY Birthdate;

SELECT FirstName, LastName, MONTH(Birthdate), Salary AS Salary_Pounds
FROM Athlete
INNER JOIN AthleteBiometrics ON ID = AthleteID
INNER JOIN AthleteSalary ON AthleteSalary.AthleteID = AthleteBiometrics.AthleteID;

SELECT MONTH(Birthdate), AVG(Salary) AS AVG_Salary_Pounds
FROM AthleteBiometrics
INNER JOIN AthleteSalary ON AthleteSalary.AthleteID = AthleteBiometrics.AthleteID
GROUP BY MONTH(Birthdate)
ORDER BY MONTH(Birthdate);

SELECT DISTINCT FirstName, LastName, Height AS Height_CM, Weight AS Weight_KG
FROM Athlete
INNER JOIN AthleteBiometrics ON ID = AthleteID;

SELECT AVG(Height) AS Avg_Height_CM, AVG(Weight) AS Avg_Weight_KG
FROM AthleteBiometrics;

SELECT FirstName, LastName, Salary AS Salary_Pounds, Nationality, Birthdate
FROM Athlete
INNER JOIN AthleteSalary ON ID = AthleteID
INNER JOIN AthleteBiometrics ON AthleteSalary.AthleteID = AthleteBiometrics.AthleteID
WHERE Salary > 0
ORDER BY Salary
