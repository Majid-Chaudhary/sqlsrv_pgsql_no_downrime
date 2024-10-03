import pyodbc
import time
import random
import string

# random names
def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=10))

# insert one record/second into the 'actor' table
def insert_actor_record(connection):
    try:
        cursor = connection.cursor()
        while True:
            first_name = generate_random_name()
            last_name = generate_random_name()
            
            # query to insert a record
            insert_query = """
                INSERT INTO dbo.actor (first_name, last_name, last_update)
                VALUES (?, ?, GETDATE());
            """
            
            # Execute query
            cursor.execute(insert_query, (first_name, last_name))
            connection.commit()  # Commit the transaction
            print(f"Inserted actor: {first_name} {last_name}")

            # 1 second wait
            time.sleep(1)
    except Exception as error:
        print(f"Error while inserting data: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("SQL Server connection is closed")

def main():
    try:
        # connection to the SQL Server database
        connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=192.168.31.170;'
        'DATABASE=sakila;'
        'UID=SA;'
        'PWD=Delta_12345678;'
        'Encrypt=no;'
    )
        
        # Start inserting actor records
        insert_actor_record(connection)
    
    except Exception as error:
        print(f"Failed to connect to SQL Server: {error}")

if __name__ == "__main__":
    main()
