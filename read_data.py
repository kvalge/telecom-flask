import pandas as pd


def read_data():
    try:
        dataset = pd.read_excel('customer_churn.xlsx')

        dataset['Total_Charges'] = pd.to_numeric(dataset['Total_Charges'], errors='coerce')
        dataset.dropna(subset=['Total_Charges'])

        return dataset
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
