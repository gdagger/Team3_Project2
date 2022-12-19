# Import dependencies
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def main():
    # Read breweries csv file as breweries_df
    breweries_df = pd.read_csv('./CleanedCSVs/breweries_table.csv')

    # Create list of unique cities and their states by grouping cities/states
    city_df = breweries_df.groupby(['city', 'state'], as_index=False).count()[['city','state']]

    # Set Chrome options to perform headless web-scraping
    options = Options()
    options.add_argument("--headless")

    # Set url for county finder
    url = "https://www.stats.indiana.edu/uspr/b/place_query.html"

    # Open Chrome driver and go to url
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    # Set county list as empty list
    county_list = []

    ##### START LOOP
    # Loop through all indices of city_df
    for i in range(len(city_df)):

        # Record percent of loop completed for status update
        percent_completed = ((i+1)/len(city_df))*100
        
        # Record first window handle
        window_before = driver.window_handles[0]

        # Store selected city from current row in city_df
        selected_city = city_df.iloc[i,0]

        # Store selected state from current row in city_df
        selected_state = city_df.iloc[i,1]

        # Print current loop count
        print(f'record {i}/{len(city_df)}')

        # Print percent of loop completion
        print(f'{round(percent_completed,2)}% complete')

        # Print current city and state
        print(f'Currently scraping {selected_city}, {selected_state}...')

        # # Navigate to original page
        driver.get(url)

        # Select dropdown menu using Select object
        dropdown_select = Select(driver.find_element_by_id('tu'))

        # Select currently selected state from dropdown
        dropdown_select.select_by_visible_text(selected_state)

        # Select input field
        input_select = driver.find_element_by_name('place_name')

        # Clear input field
        input_select.clear()

        # Enter city name
        input_select.send_keys(selected_city)
        time.sleep(0.5)

        # Locate submit button
        submit_button = driver.find_element_by_name('Submit')

        # Click submit button and pause
        submit_button.click() 
        time.sleep(0.5)

        # Record new window handle
        window_after = driver.window_handles[1]

        # Switch driver to new window handle
        driver.switch_to.window(window_after)

        # Create list of 'td' elements
        tds = driver.find_elements_by_tag_name('td')

        # Error handling for IndexError when no county found
        try:
            selected_county = tds[2].text.split(', ')[0]

            # Add county to countylist
            county_list.append(selected_county)

            print(f'Success! This city is in {selected_county}.')
        
        except IndexError:
            # Add empty value to list
            county_list.append('')

            print("No county was found.")
        print("--------------------------------")
    ##### END LOOP

    driver.quit()

    # Add list of counties to data_df as new column
    city_df['county'] = county_list

    # Export city_df as csv
    city_df.to_csv('county_df.csv')

    return city_df


if __name__ == 'main':
    main()