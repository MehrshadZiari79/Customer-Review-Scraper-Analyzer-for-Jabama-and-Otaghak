This project contains a set of Python scripts for scraping, cleaning, and categorizing room comments from the Jabama and Otaghak websites. The objective is to collect user comments about various accommodation types and process them into a structured dataset for analysis, focusing on Persian-language comments.

Features
Scraping Comments:

Jabama_Scrap.py scrapes comments from Jabama's apartment pages using Selenium.
Comments, along with additional metadata like location and room type, are saved to a CSV file (cm_jabama.csv).
Data Merging:

comment_cleaning.py merges comments from different sources (Jabama and Otaghak) into a combined dataset (merged_comments.csv) for unified analysis.
Comment Cleaning:

The script performs data cleaning on the merged comments:
Removes comments containing English letters (non-Persian).
Excludes comments with fewer than 5 characters.
Saves cleaned comments to cleaned_cms.csv.
Room Type Standardization:

The final script categorizes room types based on common Persian terms and saves the processed data to cms_grouped.csv.
Project Structure
Jabama_Scrap.py: Main scraping script for Jabama pages.
comment_cleaning.py: Cleans, merges, and categorizes comments from both Jabama and Otaghak sources.
cleaned_cms.csv: Contains the cleaned dataset with comments in Persian only.
cms_grouped.csv: Final dataset with standardized room type categories.
scraping_errors.log: Log file for tracking scraping issues.
Usage
Install Dependencies:

Ensure Python, Selenium, and other dependencies (listed below) are installed:
bash
Copy code
pip install pandas selenium psutil
Run the Scraper:

Update the chrome_driver_path in Jabama_Scrap.py to the path of your chromedriver.
Execute Jabama_Scrap.py:
bash
Copy code
python Jabama_Scrap.py
Data will be saved in batches to cm_jabama.csv.
Data Cleaning and Merging:

Run the data cleaning and merging steps sequentially to produce merged_comments.csv and cleaned_cms.csv.
Room Type Grouping:

Run the final script to standardize room types and save to cms_grouped.csv.
Dependencies
Selenium: For web scraping.
pandas: For data manipulation.
psutil: For process management.
