# function to load data from a CSV file
import pandas as pd

def load_data(path):
    """
    Load data from a CSV file and return a DataFrame.
    
    Parameters:
    path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    df = pd.read_csv(path)
    print("\n", df.head())

    # metadata summary
    print("\n-----df.info()-----")
    print("\n", df.info())
     
    # statistics summary
    print("\n-----df.describe()-----")
    print(df.describe())

    return df