from read_data import read_data
import pandas as pd
import numpy as np

data = read_data()


def tenure_statistics():
    tenure_mean = round(data['Tenure'].mean(), 2)
    tenure_median = data['Tenure'].median()
    tenure_min = data['Tenure'].min()
    tenure_max = data['Tenure'].max()
    tenure_q1 = data['Tenure'].quantile(0.25)
    tenure_q3 = data['Tenure'].quantile(0.75)
    tenure_std = round(data['Tenure'].std(), 2)

    tenure_summary = {
        "Mean": tenure_mean,
        "Median": tenure_median,
        "Min": tenure_min,
        "Max": tenure_max,
        "Q1": tenure_q1,
        "Q3": tenure_q3,
        "Std": tenure_std,
    }

    return tenure_summary


def tenure():
    return data['Tenure']


def monthly_charges_statistics():
    monthly_charges_mean = round(data['Monthly_Charges'].mean(), 2)
    monthly_charges_median = data['Monthly_Charges'].median()
    monthly_charges_min = data['Monthly_Charges'].min()
    monthly_charges_max = data['Monthly_Charges'].max()
    monthly_charges_q1 = data['Monthly_Charges'].quantile(0.25)
    monthly_charges_q3 = data['Monthly_Charges'].quantile(0.75)
    monthly_charges_std = round(data['Monthly_Charges'].std(), 2)

    monthly_charges_summary = {
        "Mean": monthly_charges_mean,
        "Median": monthly_charges_median,
        "Min": monthly_charges_min,
        "Max": monthly_charges_max,
        "Q1": monthly_charges_q1,
        "Q3": monthly_charges_q3,
        "Std": monthly_charges_std
    }

    return monthly_charges_summary


def monthly_charges():
    return data['Monthly_Charges']


def churn_statistics():
    nr_of_customers = data['Customer_ID'].nunique()
    churn_no = data['Churn'].value_counts()['No']
    churn_yes = data['Churn'].value_counts()['Yes']
    total_customers = churn_no + churn_yes

    churn_no_percent = round((churn_no / total_customers) * 100)
    churn_yes_percent = round((churn_yes / total_customers) * 100)

    churn_summary = {
        "Number of Customers": nr_of_customers,
        "Active Contracts": churn_no,
        "Terminated": churn_yes,
        "Active Contracts (%)": churn_no_percent,
        "Terminated (%)": churn_yes_percent
    }

    return churn_summary


def churn():
    return data['Churn'].value_counts()


def tenure_churn():
    bins = np.arange(0, data['Tenure'].max() + 5, 5)
    data['Tenure_bin'] = pd.cut(data['Tenure'], bins=bins, right=False)

    grouped = data.groupby(['Tenure_bin', 'Churn']).size().unstack(fill_value=0)

    grouped = grouped.div(grouped.sum(axis=1), axis=0)

    return grouped
