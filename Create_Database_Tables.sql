drop database AthleteRecords;
create database AthleteRecords;
use AthleteRecords;

create table Month (
	Name varchar(10) NOT NULL UNIQUE,
    NumberOfAthletes int NOT NULL,
    AverageIncomeOfAthletes float NOT NULL
);

create table Popularity(
	SportName varchar(20) NOT NULL UNIQUE,
    PercentPeopleWatch float NOT NULL,
    PercentPeopleCompete float NOT NULL
);

create table Award (
	Name varchar(20) NOT NULL UNIQUE,
    SportName varchar(20) NOT NULL,
	TimesReceived int,
    AthleteID int NOT NULL UNIQUE
);

create table Sport(
	Name varchar(20) NOT NULL UNIQUE,
    NumberOfAthletes int NOT NULL,
    FOREIGN KEY (Name) references Popularity(SportName)
);

create table Athlete (
	ID int NOT NULL UNIQUE,
	FirstName varchar(20) NOT NULL,
    LastName varchar(20) NOT NULL,
    Birthdate Date NOT NULL,
    Sport varchar(20) NOT NULL,
    Nationality varchar(20) NOT NULL,
    Salary int NOT NULL,
    Club varchar(20) NOT NULL UNIQUE,
    Foot varchar(5) CHECK (Foot IN ('Right', 'Left')),
    Hand varchar(5) CHECK (Hand IN ('Right', 'Left')),
    CareerLength int NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID) references Award(AthleteID),
    FOREIGN KEY (Sport) references Sport(Name)
);

create table Club (
	ClubName varchar(20) NOT NULL UNIQUE,
    Nation varchar(20) NOT NULL,
    League varchar(20) NOT NULL,
    Budget float NOT NULL,
    SportName varchar(15) NOT NULL,
    FOREIGN KEY (ClubName) references Athlete(Club)
);

