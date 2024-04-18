SELECT * FROM athleterecords.athlete;

SELECT FirstName, LastName, Birthdate, Salary AS Salary_Pounds
FROM Athlete
ORDER BY Birthdate;

SELECT FirstName, LastName, MONTH(Birthdate), Salary AS Salary_Pounds
FROM Athlete;

SELECT MONTH(Birthdate), AVG(Salary) AS AVG_Salary_Pounds
FROM Athlete
GROUP BY MONTH(Birthdate)
ORDER BY MONTH(Birthdate);

SELECT FirstName, LastName, Height AS Height_CM, Weight AS Weight_KG
FROM Athlete
ORDER BY LastName DESC;

SELECT AVG(Height) AS Avg_Height_CM, AVG(Weight) AS Avg_Weight_KG
FROM Athlete;

SELECT FirstName, LastName, Salary AS Salary_Pounds, Nationality, Birthdate
FROM Athlete
ORDER BY Salary
