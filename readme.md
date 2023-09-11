# Project Name: Translation Memory Data Pipeline

## 1. Introduction

The Translation Memory Data Pipeline project is aimed at designing and implementing a simple data pipeline to extract, transform, and load (ETL) data from a Translation Memory eXchange (TMX) file, which can be downloaded from [Opus TMX Data](https://opus.nlpl.eu/download.php?f=UN/v20090831/tmx/ar-en.tmx.gz), into a relational database. The TMX file contains parallel translations between English and Arabic languages. The primary goal of this project is to clean and structure the data before loading it into the database.

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
   conda create --name translation_memory python=3.8
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

## 5. Contributors

- [divye chopra](https://github.com/divyechopra)

## 6. License

This project is open-source, and the code can be used and modified under any open-source license of your choice.
