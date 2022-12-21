# Team3_Project2
Glen Dagger and Chris Schultz - Project 2

# Team3_Project2

Project Overview
This project looks at breweries and beers while comparing population, per captia income and median age. 

Resources
Data source: Kaggle and US census API
Software: Python, Jupyter Notebook, pgAdmin
    Modules: Pandas, Census Libray, SQL Alchemy.

Results

Extract: 

This project extracted information from Kaggle and US Census API and formatted using the follow:
    Downloading the CVS files from Kaggle
    Read them into Jupyter notebook using panadas
    Census API Calls.
    ![Alt text](Team3_Project2/screenshots/beers_df_before.png)
    ![Alt text](Team3_Project2/screenshots/breweries_df_before.png)
    ![Alt text](Team3_Project2/screenshots/census_df_before.png)

Transform: 

This project transform the data in Python. The following data cleaning was requried for this project

Beers: Filter down columns
    ![Alt text](Team3_Project2/screenshots/beers_cleaned_df.png)
    Removed 2 colums including ounces and ibu 

Breweries: Filter down columns and strip white space from names on state name and reset index to be brewery ID
    ![Alt text](Team3_Project2/screenshots/breweries_cleaned_df.png)
    Renamed Unamed column to brewery_ID

Census: Made calls to Amercia Community Survey (ACS) Data via API to pull relevant census information, Drop the state code column and cast the population column as integer. Additonally, used the dictonary to convert state names to abbreviations. 
    ![Alt text](Team3_Project2/screenshots/census_df_after.png)
    Renamed the headers including state, population, med_household_income, per_capita_income, and median age. 

Load: This project loaded 
    SQL Alchemy connect to the postgres database. Used SQL to create the tables schemia using SQL and pgAmin. Exported the the data frames from Jupyyer notebook to PgAmin. 