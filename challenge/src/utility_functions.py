"""
Created on 24/01/2024

@author: SSeeruttun
"""

from selenium import webdriver
import os
import pandas as pd
from datetime import datetime

def extract_html_headless(url):
    """
    Extracts HTML content from a given URL using a headless browser.
    IMPORTANT: Requires Google Chrome
    Parameters:
    - url (str): The URL to extract HTML content from.

    Returns:
    - str or None: Extracted HTML content if successful, None otherwise.
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        html_content = driver.page_source
        return html_content
    except Exception as e:
        print(f"Error extracting HTML from {url}: {e}")
        return None
    finally:
        driver.quit()

def save_to_csv(df, csv_filename):
    """
    Saves a DataFrame to a CSV file, either creating a new file or appending to an existing one.

    Parameters:
    - df (pd.DataFrame): The DataFrame to save.
    - csv_filename (str): The path to the CSV file.

    Returns:
    - None
    """
    try:
        if os.path.exists(csv_filename):
            df.to_csv(csv_filename, mode='a', header=False, index=False)
            print(f"Appended data to {csv_filename}")
        else:
            df.to_csv(csv_filename, index=False)
            print(f"Saved data to {csv_filename}")
    except Exception as e:
        print(f"Error saving data to {csv_filename}: {e}")

def log_error(web_id, status, message, log_filename='../output/log.csv'):
    """
    Logs an error entry to a CSV log file.

    Parameters:
    - web_id (str): Identifier for the website or extraction task.
    - status (str): Status of the extraction (e.g., 'fail', 'passed').
    - message (str): Error message or status description.
    - log_filename (str): Path to the log CSV file.

    Returns:
    - None
    """
    log_columns = ['timestamp', 'web_id', 'status', 'message']
    try:
        # Read the existing log file or create a new one
        try:
            log_df = pd.read_csv(log_filename)
        except FileNotFoundError:
            # Create a new log file if it doesn't exist
            log_df = pd.DataFrame(columns=log_columns)

        # Append the new log entry
        new_entry = pd.DataFrame({
            'timestamp': [datetime.now()],
            'web_id': [web_id],
            'status': [status],
            'message': [message]
        })

        if log_df.empty:
            log_df = new_entry
        else:
            log_df = pd.concat([log_df, new_entry], ignore_index=True)

        # Save the log to a CSV file
        log_df.to_csv(log_filename, index=False, mode='w')
    except Exception as e:
        print(f"Error logging to {log_filename}: {e}")



