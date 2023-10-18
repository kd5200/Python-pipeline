import psycopg2
from psycopg2 import Error
import boto3
from env import *


#testing the pipeline to connect Postgresql to redshift and pass data between the two systems.

# Establish PostgreSQL Connection
pg_conn = psycopg2.connect(host=pg_host, port=pg_port, dbname=pg_dbname, user=pg_user, password=pg_password)
pg_cursor = pg_conn.cursor()

# Query data from PostgreSQL
pg_cursor.execute("SELECT * FROM Population_data")
data = pg_cursor.fetchall()

# Establish Redshift Connection
rs_conn = psycopg2.connect(host=rs_host, port=rs_port, dbname=rs_dbname, user=rs_user, password=rs_password)
rs_cursor = rs_conn.cursor()

# Load data into Redshift
for row in data:
    rs_cursor.execute("INSERT INTO population VALUES (%s, %s, %s)", row)

# Commit and close connections
rs_conn.commit()
rs_conn.close()
pg_conn.close()