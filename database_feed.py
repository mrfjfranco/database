import mysql.connector
import csv
from mysql.connector import Error

# Database configuration
db_config = {
    'user': 'admin',
    'password': 'Francisc0-1981',
    'host': 'mydb.cboo2eeuw11g.us-east-2.rds.amazonaws.com',
    'database': 'fulfillment',
    'port': 3306
}

# Function to insert data into the act_errors table
def insert_act_error(ticket_id, imei, sim, error, part_number):
    try:
        # Establish a database connection
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # Insert query
            insert_query = """INSERT INTO act_errors (ticket_id, imei, sim, error, part_number)
                              VALUES (%s, %s, %s, %s, %s)"""
            record = (ticket_id, imei, sim, error, part_number)

            # Execute the insert query
            cursor.execute(insert_query, record)

            # Commit the transaction
            connection.commit()

            print(f"Record {ticket_id} inserted successfully into act_errors table.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# File path to the CSV file
csv_file_path = 'act_errors_data.csv'  # Assuming the file is in the same folder as this script

# Read data from CSV file and insert into MySQL table
with open(csv_file_path, mode='r', encoding='ISO-8859-1') as file:  # Specify the encoding
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    # Loop through each row and insert data
    for row in csv_reader:
        ticket_id, imei, sim, error, part_number = row
        insert_act_error(ticket_id, imei, sim, error, part_number)

print("Data insertion completed successfully!")