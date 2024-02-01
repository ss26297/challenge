# Schroders Challenge

The **Web Data Scraper** project is a versatile Python application designed for extracting structured data from web pages. It employs Selenium for web scraping and Beautiful Soup for HTML parsing. The project is modular, allowing users to define multiple scraping configurations for different websites.

## Key Features
- Modular Design: Easily extendable to add new web scraping modules for various websites.
- Dynamic Configuration: Users can configure scraping parameters such as URLs, HTML elements, and additional arguments through a CSV file.
- Logging: Error logs are maintained in a CSV file, providing insights into the success or failure of each scraping operation.

## Prerequisites

Make sure you have the following installed before proceeding:

- Python 3.10.11
- Pip
- Google Chrome

## Installation Steps

- Clone the repository:

```bash
git clone https://github.com/ss26297/challenge.git
```

- Navigate to the project directory

```bash
cd yourproject
```

- Create a virtual environment
```bash
python3.10 -m venv venv
```

- Activate the virtual environment (macOS/Linux)
```bash
source venv/bin/activate
```

- Activate the virtual environment (Windows)
```bash
.\venv\Scripts\activate
```

## Install dependencies

- Navigate to your project repo

```bash
cd challenge
```
- Install the dependencies

```bash
pip install -r requirements.txt
```

## Usage

- Navigate to the source code repository

```bash
cd src
```

- run the main python script using the following command

```bash
python main.py
```

## Configuration
- Details about the configuration file (**config.yaml**) and its parameters are documented for user reference.


