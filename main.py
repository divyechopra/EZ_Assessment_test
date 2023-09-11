import sys
import os
import pandas as pd
from dotenv import load_dotenv
from reader_module import download_and_save_file
from txml_to_dataframe import convert_tmx_to_dataframe
from basictransformation import preprocess_text
from load_data import upload_dataframe_to_mysql
from datetime import datetime

url = "https://opus.nlpl.eu/download.php?f=UN/v20090831/tmx/ar-en.tmx.gz"
data_folder = "data"
log_file = "log.txt"

def log(message):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{current_datetime}] {message}"
        print(log_message)


load_dotenv()

if __name__ == "__main__":
    # Redirect stdout to the log file
    sys.stdout = open(log_file, "a")
    
    log("Script started.")
    result = download_and_save_file(url, data_folder)

    if result:
        print("****************************************")
        print(f"File downloaded and saved to {result}")
        input_file_path = 'data/ar-en.tmx'
        output_csv_path = 'data/ar-en.csv'
        convert_tmx_to_dataframe(input_file_path, output_csv_path)
        
        preprocessed_df = preprocess_text(output_csv_path)
        print("****************************************")
        print("Preprocessed data successfully.")

        # Retrieve values from environment variables
        database_name = os.getenv("DATABASE_NAME")
        table_name = os.getenv("TABLE_NAME")
        host = os.getenv("HOST")
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        
        # Check if any of the required environment variables is missing
        if None in (database_name, table_name, host, user, password):
            raise Exception("One or more required environment variables are missing.")
        
        # Call the function to upload the DataFrame
        upload_dataframe_to_mysql(preprocessed_df, database_name, table_name, host, user, password)

    else:
        print("Download failed.")
    
    # Restore stdout
    sys.stdout.close()
    sys.stdout = sys.__stdout__











    
