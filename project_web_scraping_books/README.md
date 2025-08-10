
# Project: Web Scraping and Analysis of "Books to Scrape"

This project is a straightforward, end-to-end demonstration of the data acquisition and analysis lifecycle, starting with web scraping. While the target website, `books.toscrape.com`, is a sandbox designed for scraping, this project showcases the fundamental and essential workflow.

### The Process

1.  **Data Acquisition (Web Scraping):** A Python script was built using the `requests` and `BeautifulSoup` libraries. The script was designed to navigate through all 50 pages of the website's catalogue and programmatically extract the title, price, and star rating for all 1,000 books.
2.  **Data Structuring:** The scraped data was then structured into a clean, analysis-ready pandas DataFrame.
3.  **Exploratory Data Analysis (EDA):** A brief EDA was performed on the newly created dataset. The most interesting finding was the **lack of any correlation between a book's price and its rating**, challenging the common assumption that quality and price are linked.

### Skill Showcase

This project demonstrates a foundational understanding of:
*   Building a robust, multi-page web scraper.
*   Parsing HTML to extract specific data points.
*   Creating a unique dataset from scratch.
*   Performing an initial analysis on the self-collected data.

**The full scraper and analysis can be found in the notebook:**
*   [View the Notebook](./Book_Scraping_and_EDA.ipynb)
