DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS players;

CREATE TABLE teams (
  teamId INTEGER PRIMARY KEY AUTOINCREMENT,
  teamName TEXT UNIQUE NOT NULL,
  homeCity TEXT NOT NULL,
  sponsors TEXT 
);

CREATE TABLE players (
  playerId INTEGER PRIMARY KEY AUTOINCREMENT,
  firstName TEXT NOT NULL,
  secondName TEXT NOT NULL,
  patronName TEXT NOT NULL,
  birthDate DATE NOT NULL,
  teamName TEXT NOT NULL,
  FOREIGN KEY (playerId) REFERENCES teams (teamId)
);
