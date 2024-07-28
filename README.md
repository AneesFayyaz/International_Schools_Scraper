**International Schools Scraper**

This repository contains a Python script for scraping information about international schools from a specific website. The script uses Selenium for web automation and BeautifulSoup for HTML parsing. It extracts the names and URLs of schools, categorizing them by country and continent, and saves the data into a CSV file.

**Prerequisites**

Before running the script, ensure you have the following installed:

  Python 3.x
  Selenium
  BeautifulSoup
  chromedriver_autoinstaller
  pandas

**Script**

This script scrapes the names and URLs of international schools from the specified website.

**Functionality:**

  Opens the website's page listing international schools.
  Clicks through each continent and country to load the school information.
  Extracts the school names and URLs.
  Saves the data to output_file.csv.

**Output**

The script outputs a CSV file named output_file.csv with the following columns:

  Country: The country where the school is located.
  School Name: The name of the school.
  School Url: The URL of the school's website.
