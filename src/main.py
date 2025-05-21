# main.py
import pandas as pd
import numpy as np
import logging
import os

# --- Configure Logging ---
logger = logging.getLogger(__name__)
def setup_logging():
    log_file_path = "data/data_processing.log" # Relative path
    log_dir = os.path.dirname(log_file_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir) # Ensure data directory exists for the log

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG) # Process all messages from DEBUG up
    logger.propagate = False

def process_some_data(input_file="data/sample_input.csv"):
    logger.info(f"Attempting to read data from {input_file}")
    try:
        # Ensure data directory exists if we plan to read a default file from it
        data_dir_for_input = os.path.dirname(input_file)
        if data_dir_for_input and not os.path.exists(data_dir_for_input):
             os.makedirs(data_dir_for_input)
             logger.info(f"Created directory: {data_dir_for_input}")
        
        # For simplicity, let's assume sample_input.csv exists or is created manually for now
        # Or add logic here to create it if it doesn't exist
        if not os.path.exists(input_file):
            logger.warning(f"{input_file} not found. Creating a dummy one.")
            # Create a dummy sample_input.csv for the script to run
            dummy_df = pd.DataFrame({'A': [1,2], 'B': [3,4]})
            dummy_df.to_csv(input_file, index=False)

        df = pd.read_csv(input_file)
        logger.info("Data read successfully.")
        df["processed_value"] = df.iloc[:, 0] * 100 # Example processing
        
        output_file = "data/processed_output.csv"
        df.to_csv(output_file, index=False)
        logger.info(f"Processed data saved to {output_file}")
        return df
    except Exception as e:
        logger.error(f"Error during data processing: {e}", exc_info=True)
        return pd.DataFrame()

if __name__ == "__main__":
    setup_logging()
    logger.info("Script started.")
    # Create a dummy data/sample_input.csv if it doesn't exist so the script can run
    if not os.path.exists("data"): os.makedirs("data")
    if not os.path.exists("data/sample_input.csv"):
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).to_csv("data/sample_input.csv", index=False)
        logger.info("Created dummy data/sample_input.csv")

    process_some_data()
    logger.info("Script finished.")