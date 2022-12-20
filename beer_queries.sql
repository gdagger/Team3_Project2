DROP TABLE IF EXISTS beers, breweries, county_census, state_census;

CREATE TABLE state_census (
	state VARCHAR(5),
	population INT,
	med_household_income FLOAT,
	per_capita_income FLOAT,
	median_age FLOAT,
	PRIMARY KEY (state)
);

CREATE TABLE county_census (
	county VARCHAR(50),
	state VARCHAR(5),
	population INT,
	med_household_income FLOAT,
	per_capita_income FLOAT,
	median_age FLOAT,
	PRIMARY KEY(county,state),
	FOREIGN KEY (state) REFERENCES state_census(state)
);

CREATE TABLE breweries (
	brewery_id SERIAL,
	name VARCHAR(50),
	city VARCHAR(50),
	county VARCHAR(50),
	state VARCHAR(5),
	PRIMARY KEY (brewery_id),
	FOREIGN KEY (county, state) REFERENCES county_census (county, state)
	FOREIGN KEY (state) REFERENCES state_census (state)
);

CREATE TABLE beers (
	id INT,
	name VARCHAR(100),
	style VARCHAR(50),
	brewery_id INT,
	abv FLOAT,
	PRIMARY KEY (id),
	FOREIGN KEY (brewery_id) REFERENCES breweries(brewery_id)
);