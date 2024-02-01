"""
Created on 24/01/2024

@author: SSeeruttun
"""

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import pandas as pd

class BaseScraper(ABC):
    """
    Abstract base class for web scrapers.

    Attributes:
    - html_content (str): HTML content to be processed by the scraper.

    Methods:
    - extract_values(table: str, text: str) -> Any:
        Abstract method to extract values from HTML content.

    - process_input_data(input_data: Any) -> pd.DataFrame:
        Abstract method to process the extracted data.

    """
    def __init__(self, html_content):
        """
        Initializes the BaseScraper instance.

        Parameters:
        - html_content (str): HTML content to be processed by the scraper.
        """
        self.html_content = html_content

    @abstractmethod
    def extract_values(self, table, text):
        """
        Abstract method to extract values from HTML content.

        Parameters:
        - table (str): CSS selector for the target table.
        - text (str): Text to identify the specific table.

        Returns:
        - Any: Extracted values from the HTML content.
        """
        pass

    @abstractmethod
    def process_input_data(self, input_data):
        """
        Abstract method to process the extracted data.

        Parameters:
        - input_data (Any): Extracted data from the HTML content.

        Returns:
        - pd.DataFrame: Processed data in the form of a DataFrame.
        """
        pass