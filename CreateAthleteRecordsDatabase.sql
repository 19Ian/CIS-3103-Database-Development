drop database AthleteRecords;
create database AthleteRecords;
use AthleteRecords;

create table Month (
	Name varchar(10) CHECK (Name IN ("January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December")) NOT NULL UNIQUE default("Unknown") ,
    NumberOfAthletes int NOT NULL default(0),
    AverageIncomeOfAthletes float NOT NULL default(0.0)
);

create table Popularity(
	SportName varchar(20) NOT NULL UNIQUE default("Soccer"),
    PercentPeopleWatch float NOT NULL default(0.0),
    PercentPeopleCompete float NOT NULL default(0.0)
);

create table Award (
	Name varchar(20) NOT NULL UNIQUE default("Unknown"),
    SportName varchar(20) NOT NULL default("Soccer"),
	TimesReceived int default(0),
    AthleteID int NOT NULL UNIQUE
);

create table Sport(
	Name varchar(20) NOT NULL UNIQUE default("Soccer"),
    NumberOfAthletes int NOT NULL default(0),
    FOREIGN KEY (Name) references Popularity(SportName)
);

create table Athlete (
	ID int NOT NULL UNIQUE,
	FirstName varchar(20) NOT NULL default("Unknown"),
    LastName varchar(20) NOT NULL default("Unknown"),
    Birthdate Date NOT NULL default (current_date),
	Nationality varchar(5) NOT NULL default("N/A"),
	Salary int NOT NULL default (00000),
--     Club varchar(20) NOT NULL UNIQUE,
	Foot varchar(6) CHECK (Foot IN ('Right', 'Left', 'Either')),
    Height int NOT NULL default (0),
    Weight int NOT NULL default (0),
    Age int NOT NULL default (0)
--     CareerLength int NOT NULL,
--     PRIMARY KEY (ID),
--     FOREIGN KEY (ID) references Award(AthleteID),
--     FOREIGN KEY (Sport) references Sport(Name)
);

create table Club (
	ClubName varchar(20) NOT NULL UNIQUE,
    Nation varchar(20) NOT NULL default("Unknown"),
    League varchar(20) NOT NULL default("Unknown"),
    Budget float NOT NULL default(0.0),
    SportName varchar(15) NOT NULL default("Soccer"),
    FOREIGN KEY (ClubName) references Athlete(Club)
);

