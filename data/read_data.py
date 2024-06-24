import pandas as pd


def read_data():
    try:
        dataset = pd.read_excel('data/customer_churn.xlsx')
        return dataset
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
