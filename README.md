# CIS-3103-Database-Development

This is to track, store, analyze the birth month of successful athletes in different sports to see any trends in when successful athletes are born. It'll track the birth month, day(if possible), what sport the athlete is competing in, name, nationality, and probably some others I think of along the way.

To run: "python ConnectToAthleteDatabase.py config.json"x

## Entities
Athlete: (Strong Entity because it has a Primary Key and is not reliant on a foreign key) ID: (First Name, Last Name)
  - First Name R
  - Last Name R
  - Birthdate R
  - Sport R
  - Nationality R
  - Age R
  - Salary R
  - Awards P
  - Club
  - Foot
  - Hand
  - Career Length R

Sport: (Strong Entity because it has a Primary Key and is not reliant on a foreign key) ID: (Sport Name)
  - Sport Name R *U*
  - number of athletes R P
  - popularity R

Popularity: (Strong Entity because it has a Primary Key and is not reliant on a foreign key) ID: (Sport Name)
  - Sport Name R *U*
  - percent of people competing R
  - percent of people watching R

Month: (Strong Entity because it has a Primary Key and is not reliant on a foreign key) ID: (Name)
  - Name R *U*
  - number of athletes in a month R P
  - avg income per month from athletes R

Club: (Strong Entity because it has a Primary Key and is not reliant on a foreign key) ID: (Name)
  - Name R *U*
  - Nation R
  - League R
  - Budget R
  - Sport Name R
  - Athletes R P

Award: (Strong Entity because it has a Primary Key and is not reliant on a foreign key) ID: (Name)
  - Name R *U*
  - Sport Name R
  - Number of Times Received P

## Relationships
- Month has many athletes but possibly none 
- Athletes are born in one month
- Athletes are in one Club
- Athletes are given Awards but possibly none
- Athletes play in at least one Sport
- A Sport is played by many Athletes
- A Sport has a level of Popularity
- A Sport is played by at least one Club
- A Club has many Athletes
- A Club participates in one Sport

## Queries
  SELECT FirstName, LastName, Birthdate, Salary AS Salary_Pounds
  FROM Athlete
  ORDER BY Birthdate DESC

  SELECT FirstName, LastName, Height AS Height_CM, Weight AS Weight_KG
  FROM Athlete
  ORDER BY LastName DESC;

  SELECT FirstName, LastName, Salary AS Salary_Pounds, Nationality, Birthdate
  FROM Athlete
  ORDER BY Salary
  
  SELECT AVG(Height) AS Avg_Height_CM, AVG(Weight) AS Avg_Weight_KG
  FROM Athlete;

## Glossary
Athlete - someone competing in one of the following sports who is considered to be successful: Soccer, Basketball, American Football(inferior), Tennis, and Volleyball.

Sport - either Soccer, Basketball, American Football, Tennis, or Volleyball.

Popularity - the popularity of each sport in the world hopefully differentiating between those competing and those just watching.

## Data Links
https://medium.com/@giacorada/the-fascinating-birth-trend-among-professional-soccer-players-b2a48d015e7d
https://girlssoccernetwork.com/soccer-success-do-birth-months-matter/
https://www.kaggle.com/datasets/furkanuluta/football-manager-22-complete-player-dataset?resource=download
https://www.kaggle.com/datasets/ultimus/football-wages-prediction

## Table
    Player-Name | Salary | Birthdate | Prefered Foot | Position

X = birthMonth
Y = Salary
Point-shape = Prefered Foot
Color = Position
Point-label = Player-Name

## ER Diagram
![Database ER diagram (crow's foot) (1)](https://github.com/19Ian/CIS-3103-Database-Development/assets/79172931/276d1a3b-a05a-40e3-a806-20ea41625877)
