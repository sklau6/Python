import pandas as pd

def read_csv_file(file_path: str) -> pd.DataFrame:
    data = pd.read_csv(file_path)
    return data

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    # Fill missing values with default values
    data['first_name'] = data['first_name'].fillna('Unknown')
    data['last_name'] = data['last_name'].fillna('Unknown')
    data['email'] = data['email'].fillna('unknown@example.com')
    data['age'] = data['age'].fillna(data['age'].mean())

    # Remove duplicates based on 'email' column
    data = data.drop_duplicates(subset='email', keep='first')

    # Convert email column to lowercase
    data['email'] = data['email'].str.lower()

    return data

def main():
    file_path = 'data.csv'

    data = read_csv_file(file_path)
    clean_data1 = clean_data(data)

    print(clean_data1)

if __name__ == '__main__':
    main()
