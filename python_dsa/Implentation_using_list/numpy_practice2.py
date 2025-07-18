import pandas as pd

def read_csv_file():

    # Read the Excel file into a pandas DataFrame
    df = pd.read_csv('c-section.csv')

	# Display the first few rows of the DataFrame
    print(df.count())
    print(df.head())
    print(df.tail())

read_csv_file()