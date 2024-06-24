from data.read_data import read_data
import pandas as pd


def clean_data():
    data = read_data()

    data['Total_Charges'] = pd.to_numeric(data['Total_Charges'], errors='coerce')
    data.dropna(subset=['Total_Charges'])

    return data
