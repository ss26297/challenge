"""
Created on 24/01/2024

@author: SSeeruttun
"""

import pandas as pd
from utility_functions import extract_html_headless, save_to_csv, log_error
from site_extractors.ndsl_site_extractor import NDSLScraper
import yaml

def main():
    """
    Main function to execute web scraping based on the provided configuration.

    Reads configuration from the config.yaml file, iterates through the input CSV file, performs web scraping, and logs
    the results.

    """
    # Read configuration from the config.yaml file
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    try:
        # Read the configuration CSV
        config_df = pd.read_csv(config['input_filename'])

        # Check if the required columns are present
        required_columns = {'web_id', 'url', 'table_to_extract', 'additional_argument', 'file_path', 'scraper_object'}
        if not required_columns.issubset(config_df.columns):
            raise ValueError(f"Missing required columns in input file")

        for _, row in config_df.iterrows():
            # Extract configuration values
            web_id = row['web_id']
            url = row['url']
            table_to_extract = row['table_to_extract']
            additional_argument = row['additional_argument']
            csv_filename = row['file_path']
            scraper_object = row['scraper_object']
            # Extract HTML from the site using the utility function
            html_content = extract_html_headless(url)
            # Create an instance of the SiteExtractor class
            scraper_class = NDSLScraper
            scraper_object = scraper_class(html_content)
            # Execute the extraction and processing
            result_df = scraper_object.execute(table_to_extract, additional_argument)
            # Save the result to a CSV file using the utility function
            save_to_csv(result_df, csv_filename)
            # Log success
            log_error(web_id, 'pass', "Extraction successful", config['log_filename'])

    except Exception as e:
        # Log errors
        log_error(web_id, 'fail', f"Error: {str(e)}", config['log_filename'])

if __name__ == "__main__":
    main()