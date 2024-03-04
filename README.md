# CIS-3103-Database-Development

This is to track, store, analyze the birth month of successful athletes in different sports to see any trends in when successful athletes are born. It'll track the birth month, day(if possible), what sport the athlete is competing in, name, nationality, and probably some others I think of along the way.

## Entities
Athlete: (Strong Entity) ID: (First Name, Last Name)
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

Sport: (Strong Entity) ID: (Sport Name)
  - Sport Name R *U*
  - number of athletes R P
  - popularity R

Popularity: (Strong Entity) ID: (Sport Name)
  - Sport Name R *U*
  - percent of people competing R
  - percent of people watching R

Month: (Strong Entity) ID: (Name)
  - Name R *U*
  - number of athletes in a month R P
  - avg income per month from athletes R

Club: (Strong Entity) ID: (Name)
  - Name R *U*
  - Nation R
  - League R
  - Budget R
  - Sport Name R
  - Athletes R P

Award: (Strong Entity) ID: (Name)
  - Name R *U*
  - Sport Name R
  - Number of Times Received P

## Relationships
Month has many athletes but possibly none 
Athletes are born in one month
Athletes are in one Club
Athletes are given Awards but possibly none
Athletes play in at least one Sport
A Sport is played by many Athletes
A Sport has a level of Popularity
A Sport is played by at least one Club
A Club has many Athletes
A Club participates in one Sport

## Glossary
Athlete - someone competing in one of the following sports who is considered to be successful: Soccer, Basketball, American Football(inferior), Tennis, and Volleyball.

Sport - either Soccer, Basketball, American Football, Tennis, or Volleyball.

Popularity - the popularity of each sport in the world hopefully differentiating between those competing and those just watching.
