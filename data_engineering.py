import pandas as pd
import sqlite3

# Read data from CSV file
def read_csv_file(file_path: str) -> pd.DataFrame:
    data = pd.read_csv(file_path)
    return data

# Clean and transform data
def clean_transform_data(data: pd.DataFrame) -> pd.DataFrame:
    # Drop rows with missing values
    data = data.dropna()

    # Convert date column to datetime format
    data['date'] = pd.to_datetime(data['date'])

    # Create new columns for year, month, and day
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day

    # Convert categorical columns to uppercase
    data['category'] = data['category'].str.upper()
    data['sub_category'] = data['sub_category'].str.upper()

    return data

# Load data into SQLite database
def load_data_to_sqlite(data: pd.DataFrame, db_name: str):
    conn = sqlite3.connect(db_name)
    data.to_sql('sales_data', conn, if_exists='replace', index=False)
    conn.close()

# Main function
def main():
    file_path = 'sales_data.csv'
    db_name = 'sales_data.db'

    data = read_csv_file(file_path)
    clean_data = clean_transform_data(data)
    load_data_to_sqlite(clean_data, db_name)

if __name__ == '__main__':
    main()
