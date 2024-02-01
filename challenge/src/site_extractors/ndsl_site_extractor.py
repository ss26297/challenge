"""
Created on 24/01/2024

@author: SSeeruttun
"""

from .base_extractor import BaseScraper
from bs4 import BeautifulSoup
import pandas as pd

class NDSLScraper(BaseScraper):
    """
    Web scraper for the NDSL site.

    Inherits from BaseScraper.

    Methods:
    - extract_values(table: str, text: str) -> Any:
        Extracts values from the HTML content.

    - process_input_data(input_data: Any) -> pd.DataFrame:
        Processes the extracted data.

    - execute(table: str, text: str) -> pd.DataFrame:
        Executes the extraction and processing.

    """
    def __init__(self, html_content):
        """
        Initializes the NDSLScraper instance.

        Parameters:
        - html_content (str): HTML content to be processed by the scraper.
        """
        super().__init__(html_content)

    def extract_values(self, table, text):
        """
        Extracts values from the HTML content.

        Parameters:
        - table (str): CSS selector for the target table.
        - text (str): Text to identify the specific table.

        Returns:
        - Any: Extracted values from the HTML content.
        """
        try:
            soup = BeautifulSoup(self.html_content, 'html.parser')
            # Find the table with the specific heading
            target_table = None
            for table in soup.select(table):
                heading = table.find('th', string=text)
                if heading:
                    target_table = table
                    break
            # Extracting data from the target table
            if target_table:
                table_data = []
                for row in target_table.select('tbody tr'):
                    row_data = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
                    table_data.append(row_data)
                return table_data
            else:
                raise ValueError(f"Table with {text} not found.")
        except Exception as e:
            print(f"Error extracting values: {e}")
            return None

    def process_input_data(self, input_data):
        """
        Processes the extracted data.

        Parameters:
        - input_data (Any): Extracted data from the HTML content.

        Returns:
        - pd.DataFrame: Processed data in the form of a DataFrame.
        """
        try:
            title = input_data[0][0]
            header = input_data[1]
            # Check if 'No Record Found' is present
            if 'No Record Found' in input_data[2]:
                print(f"{title}: No Record Found")
                return pd.DataFrame()  # Return an empty DataFrame
            else:
                data_rows = input_data[2:]
                # Convert data to Pandas DataFrame
                df = pd.DataFrame(data_rows, columns=header)
                return df
        except Exception as e:
            print(f"Error processing input data: {e}")
            return None

    def execute(self, table, text):
        """
        Executes the extraction and processing.

        Parameters:
        - table (str): CSS selector for the target table.
        - text (str): Text to identify the specific table.

        Returns:
        - pd.DataFrame: Processed data in the form of a DataFrame.
        """
        try:
            # Extract values from the HTML content
            extracted_data = self.extract_values(table, text)
            if extracted_data is not None:
                # Process the extracted data
                df = self.process_input_data(extracted_data)
                return df
            else:
                return None
        except Exception as e:
            print(f"Error during execution: {e}")
            return None


