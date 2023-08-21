# Analystt.ai

This project involves scraping data from Amazon search results and performing data preprocessing to generate a CSV file with useful information.

## Files and Workflow

- `final.py`: Python script for Task 1.
- `output_{page_number}.html`: HTML files corresponding to the respective page numbers after the search.
- The outpt of task 1 is saved in `final_output.txt`
- `analystt.csv`: CSV file containing raw data gathered from Amazon search results using webscraper.io extension.
- `Untitled.ipynb`: Jupyter Notebook used for data preprocessing. This notebook was used to clean and process data from `analystt.csv` to generate the required `output.csv`.

## Project Steps for task 2

1. **Scraping Amazon Data** (`final.py`):
   - Due to restrictions with BeautifulSoup, the web scraping tool webscraper.io extension was used.
   - The resulting data was saved as analystt.csv.

2. **Data Preprocessing** (`Untitled.ipynb`):
   - The data gathered from the HTML files was loaded into a CSV file named `analystt.csv`.
   - Data preprocessing was performed in the Jupyter Notebook `Untitled.ipynb`.
   - The cleaned and processed data was saved as `output.csv`.

