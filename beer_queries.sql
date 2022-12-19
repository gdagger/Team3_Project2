DROP TABLE IF EXISTS beers, census_data, breweries;

CREATE TABLE census_data (
	state VARCHAR(5) PRIMARY KEY,
	population INT,
	med_household_income FLOAT,
	per_capita_income FLOAT,
	median_age FLOAT
);

CREATE TABLE breweries (
	brewery_id INT PRIMARY KEY,
	name VARCHAR(50),
	city VARCHAR(50),
	state VARCHAR(5) REFERENCES census_data(state)
);

CREATE TABLE beers (
	id INT PRIMARY KEY,
	name VARCHAR(100),
	style VARCHAR(50),
	brewery_id INT REFERENCES breweries(brewery_id),
	abv FLOAT
)