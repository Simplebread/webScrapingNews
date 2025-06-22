<a id="readme-top"></a>
Web Scraper for RSS News

Python Web Scraper for News using RSS and Beautiful Soup

<br />
<br />

## Table of Contents

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#test-cases--coverage-summary">Test Cases & Coverage Summary</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## About The Project

* Used to scrape and gather information from RSS news feed
* Store and archive news feed
* Main purpose is to educate on news
* Features: SQLite, Local Keywords for Comparison

### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* [![BeautifulSoup](https://img.shields.io/badge/Beautiful%20Soup-4.9.3-green?style=for-the-badge&logo=python&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [![Requests](https://img.shields.io/badge/Requests-2.28.1-blue?style=for-the-badge&logo=python&logoColor=white)](https://requests.readthedocs.io/en/latest/)
* [SQLite](https://www.sqlite.org/): For database management.

## Getting Started

This section outlines how to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

List anything users need to have installed *before* they can run your project.
* Python 3.x
* `pip` (Python package installer)


### Installation

Provide step-by-step instructions on how to install and set up your project.

1.  **Clone the repo**
    ```bash
    git clone [https://github.com/Simplebread/webScrapingNews.git](https://github.com/Simplebread/webScrapingNews.git)
    cd webScrapingNews
    ```
2.  **Create Virtual Environment**
    ```bash
    python -m venv venv
    
    # On macOS / Linux
    source venv/bin/activate
    
    # On Windows PowerShell
    .\venv\Scripts\activate
    ```
3.  **Install Python packages**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure (if applicable)**
    * Add/Remove RSS news feed (URL) in `config.py` and add more onto the keywords

## Usage
```bash
python run_scraper.py


```

## Roadmap
* [x] Add robust error handling for RSS feed fetching.
* [x] Implement dynamic country detection.
* [ ] Support more RSS feed sources.
* [ ] Allow fetching RSS feed sources from more than a year ago.
* [ ] Integrate a search functionality for archived news.

## Contact
* email: raymondblue822@gmail.com

## Acknowledgements
* Mr. Subhojeet: assisting and providing feedback
* ChatGPT: assisting and providing feedback