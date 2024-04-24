drop database AthleteRecords;
create database AthleteRecords;
use AthleteRecords;


create table AthleteSalary (
    AthleteID int NOT NULL UNIQUE PRIMARY KEY,
    Salary int NOT NULL default (00000),
    Club varchar(30) NOT NULL default("N/A")
);

create table AthleteBiometrics (
    AthleteID int NOT NULL UNIQUE PRIMARY KEY,
    Birthdate Date NOT NULL default (current_date),
    Foot varchar(6) CHECK (Foot IN ('Right', 'Left', 'Either')),
    Height int NOT NULL default (0) CHECK(Height > 0 AND Height < 200),
    Weight int NOT NULL default (0) CHECK(Weight > 0 AND Weight < 100),
    Age int NOT NULL default (0) CHECK(Age > 0 AND Age < 100)
);

create table Athlete (
    ID int NOT NULL UNIQUE PRIMARY KEY,
    FirstName varchar(20) NOT NULL default("Unknown"),
    LastName varchar(60) NOT NULL default("Unknown"),
    Nationality varchar(5) NOT NULL default("N/A"),
    FOREIGN KEY (ID) references AthleteBiometrics(AthleteID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ID) references AthleteSalary(AthleteID) ON UPDATE CASCADE ON DELETE CASCADE
);
