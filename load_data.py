import pandas as pd
from sqlalchemy import create_engine,text


def upload_dataframe_to_mysql(dataframe, database_name, table_name, host, user, password):
    # Create a MySQL connection using SQLAlchemy
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database_name}")
    connection = engine.connect()

    # Create the database if it doesn't exist
    create_database_query = text(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    use_database_query = text(f"USE {database_name}")
    connection.execute(create_database_query)
    connection.execute(use_database_query)

    # SQL query to drop the table if it exists
    drop_table_query = text(f"DROP TABLE IF EXISTS {table_name}")
    
    connection.execute(drop_table_query)

    # Create the table if it doesn't exist
    dataframe.to_sql(table_name, con=engine, index=False)

    print(f"Data uploaded to {database_name}.{table_name}")
    connection.close()
