# Project Name: Translation Memory Data Pipeline

## 1. Introduction

The Translation Memory Data Pipeline project is aimed at designing and implementing a simple data pipeline to extract, transform, and load (ETL) data from a Translation Memory eXchange (TMX) file, which can be downloaded from [Opus TMX Data](https://opus.nlpl.eu/download.php?f=UN/v20090831/tmx/ar-en.tmx.gz), into a relational database. The TMX file contains parallel translations between English and Arabic languages. The primary goal of this project is to clean and structure the data before loading it into the database.

## File Details
### [reader_module.py](https://github.com/divyechopra/ET_Assessment_test/blob/main/reader_module.py)

This module provides functions to download a file from a URL, save it to a specified folder(data), and decompress it if it's a gzip file.

   ```
      import os
      import requests
      import gzip

      # Functions:
      # - download_and_save_file(url, folder)

   ```

### [tmx_to_dataframe.py](https://github.com/divyechopra/ET_Assessment_test/blob/main/txml_to_dataframe.py)
<a name="tmx_to_dataframepy"></a>
This module converts a TMX (Translation Memory eXchange) file to a DataFrame in CSV format. It extracts language and text pairs from the TMX file.

   ```
      import xml.etree.ElementTree as ET
      import pandas as pd

      # Functions:
      # - convert_tmx_to_dataframe(input_file_path, output_csv_path)

   ```
### [basictransformation.py](https://github.com/divyechopra/ET_Assessment_test/blob/main/basictransformation.py)
<a name="basictransformationpy"></a>
This module performs basic text preprocessing tasks on the data, including text cleaning, tokenization, stopword removal, and stemming (for English text).

   ```   
      import nltk
      from nltk.corpus import stopwords
      from nltk.tokenize import word_tokenize
      from nltk.stem import SnowballStemmer
      import pandas as pd

      # Functions:
      # - preprocess_text(file_path, max_seq_length=10)
   ```

### [load_data.py](https://github.com/divyechopra/ET_Assessment_test/blob/main/load_data.py)
<a name="load_datapy"></a>
This module uploads a DataFrame to a MySQL database. It creates the database if it doesn't exist, drops the table if it exists, and then creates the table and inserts the data.


   ```
      import pandas as pd
      from sqlalchemy import create_engine, text

      # Functions:
      # - upload_dataframe_to_mysql(dataframe, database_name, table_name, host, user, password)\
   ```

### [main.py](https://github.com/divyechopra/ET_Assessment_test/blob/main/main.py)
<a name="main.py" ></a>
This is the main script that orchestrates the entire ETL process. It downloads a TMX file, converts it to a DataFrame, performs text preprocessing, and uploads the data to a MySQL database.


## 2. Project Structure

The project can be broken down into the following main steps:

### Data Source
- The data source is the TMX file available at [Opus TMX Data](https://opus.nlpl.eu/download.php?f=UN/v20090831/tmx/ar-en.tmx.gz).

### Data Transformation
- Perform necessary transformations to ensure the proper reading of English and Arabic characters from the TMX file.

### Database
- Choose and set up a relational database of your choice (e.g., PostgreSQL, MySQL) to store the transformed data.

### ETL Process
- Create a reader module for reading TMX files.
- Apply the necessary transformations to clean and structure the data.
- Load the cleaned data into the chosen database.

## 3. Environment

To run this project, ensure you have the following environment set up:

- Operating System: Windows 10/11
- Database Tool: MySQL Workbench (or equivalent for your chosen database)
- Anaconda

## 4. Execution Steps

Follow these steps to execute the project:

1. Create a Conda environment with a Python version greater than 3.8.
   
   ```
   conda create --name translation_memory python=3.9
   ```

2. Activate the environment.

   ```
   conda activate translation_memory
   ```

3. Install the required libraries.

   ```
   pip install -r requirements.txt
   ```

4. Modify the `.env` file parameters to configure your MySQL database connection.

5. Run the main script to execute the ETL process.

   ```
   python main.py
   ```

The data in MySQL Workbench: 


## 5. Contributors

- [divye chopra](https://github.com/divyechopra)

## 6. License

This project is open-source, and the code can be used and modified under any open-source license of your choice.
