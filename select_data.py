import sqlite3

def select_data_from_sqlite(db_name: str):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SELECT query
    cursor.execute("SELECT * FROM sales_data where sub_category = 'COMPUTERS'")

    # Fetch all rows from the result of the query
    rows = cursor.fetchall()

    # Print column names
    column_names = [description[0] for description in cursor.description]
    print(column_names)

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

# Main function
def main():
    db_name = 'sales_data.db'
    select_data_from_sqlite(db_name)

if __name__ == '__main__':
    main()
