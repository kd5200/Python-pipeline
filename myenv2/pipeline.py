
import pandas as pd
import psycopg2
from psycopg2 import Error
from env import PGpassword
import boto3





try:
    connection = psycopg2.connect(user="postgres",
                                  password= PGpassword,
                                  host="localhost",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL database:", error)


    # Close the database connection outside the try-except block.
def close_db(): 
    if connection:
        cursor.close()
        connection.close()
    print("PostgreSQL connection is closed")


cursor.execute("SELECT * FROM Population_data")
records = cursor.fetchall()

# Process the fetched data
for row in records:
    print("Column1:", row[0])
    print("Column2:", row[1])


