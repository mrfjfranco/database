import mysql.connector
import pandas as pd
from mysql.connector import Error

# Database configuration
db_config = {
    'user': 'admin',
    'password': 'Francisc0-1981',
    'host': 'mydb.cboo2eeuw11g.us-east-2.rds.amazonaws.com',
    'database': 'fulfillment',
    'port': 3306
}

# Function to fetch data from act_errors table
def fetch_act_errors():
    try:
        # Establish a database connection
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            # Query to retrieve data from the table
            query = "SELECT ticket_id, imei, sim, error, part_number FROM act_errors"
            
            # Using pandas to read the query into a DataFrame
            df = pd.read_sql(query, connection)

            # Saving the DataFrame to an Excel file
            output_file = 'act_errors_records.xlsx'
            df.to_excel(output_file, index=False)

            print(f"Data exported successfully to {output_file}")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()

# Fetch and export the data
fetch_act_errors()