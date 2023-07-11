DROP DATABASE IF EXISTS foundation_assessment_ii;
CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

-- A] movie_info Table
DROP TABLE IF EXISTS movie_info;
CREATE TABLE movie_info (
  Movie_ID INT PRIMARY KEY,
  Movie_Name VARCHAR(100),
  Movie_Length TIME,
  Age_Rating VARCHAR(10)
);

-- B] screens Table
CREATE TABLE IF NOT EXISTS screens (
  Screen_ID INT PRIMARY KEY,
  Four_K BOOLEAN
);

-- C] showings Table
CREATE TABLE IF NOT EXISTS showings (
  Showing_ID INT PRIMARY KEY,
  Movie_ID INT,
  Screen_ID INT,
  Start_Time TIME,
  Available_Seats INT,
  FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
  FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

-- Inserting data into movie_info table
INSERT INTO movie_info (Movie_ID, Movie_Name, Movie_Length, Age_Rating)
VALUES
  (1, 'The Movie', '01:35:00', '12A');

-- Inserting data into screens table
INSERT INTO screens (Screen_ID, Four_K)
VALUES
  (1, false);

-- Inserting data into showings table
INSERT INTO showings (Showing_ID, Movie_ID, Screen_ID, Start_Time, Available_Seats)
VALUES
  (1, 1, 1, '12:00:00', 23);
