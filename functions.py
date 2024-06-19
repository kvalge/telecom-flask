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

    churn_no_percentage = round((churn_no / total_customers) * 100)
    churn_yes_percentage = round((churn_yes / total_customers) * 100)

    churn_summary = {
        "Number of Customers": nr_of_customers,
        "Active Contracts": churn_no,
        "Terminated": churn_yes,
        "Active Contracts (%)": churn_no_percentage,
        "Terminated (%)": churn_yes_percentage
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


def monthly_charges_churn():
    bins = np.arange(10, data['Monthly_Charges'].max() + 10, 10)
    data['Monthly_Charges_bin'] = pd.cut(data['Monthly_Charges'], bins=bins, right=False)

    grouped = data.groupby(['Monthly_Charges_bin', 'Churn']).size().unstack(fill_value=0)

    grouped = grouped.div(grouped.sum(axis=1), axis=0)

    return grouped


def age_group_statistics():
    senior_no = data['Senior_Citizen'].value_counts()['No']
    senior_yes = data['Senior_Citizen'].value_counts()['Yes']
    total_customers = senior_no + senior_yes

    senior_no_percentage = round((senior_no / total_customers) * 100)
    senior_yes_percentage = round((senior_yes / total_customers) * 100)

    age_group_summary = {
        "Age < 65": senior_no,
        "Age > 65": senior_yes,
        "Age < 65 (%)": senior_no_percentage,
        "Age > 65 (%)": senior_yes_percentage
    }

    return age_group_summary


def age_group():
    return data['Senior_Citizen'].value_counts()


def partner_statistics():
    partner_no = data['Partner'].value_counts()['No']
    partner_yes = data['Partner'].value_counts()['Yes']
    total_customers = partner_no + partner_yes

    partner_no_percentage = round((partner_no / total_customers) * 100)
    partner_yes_percentage = round((partner_yes / total_customers) * 100)

    partner_summary = {
        "Has no partner": partner_no,
        "Has partner": partner_yes,
        "Has no partner (%)": partner_no_percentage,
        "Has partner (%)": partner_yes_percentage
    }

    return partner_summary


def partner():
    return data['Partner'].value_counts()


def dependents_statistics():
    dependents_no = data['Dependents'].value_counts()['No']
    dependents_yes = data['Dependents'].value_counts()['Yes']
    total_customers = dependents_yes + dependents_no

    dependents_no_percentage = round((dependents_no / total_customers) * 100)
    dependents_yes_percentage = round((dependents_yes / total_customers) * 100)

    dependents_summary = {
        "Has no dependents": dependents_no,
        "Has dependents": dependents_yes,
        "Has no dependents (%)": dependents_no_percentage,
        "Has dependents (%)": dependents_yes_percentage
    }

    return dependents_summary


def dependents():
    return data['Dependents'].value_counts()


def phone_statistics():
    phone_no = data['Phone_Service'].value_counts()['No']
    phone_yes = data['Phone_Service'].value_counts()['Yes']
    total_customers = phone_no + phone_yes

    phone_no_percentage = round((phone_no / total_customers) * 100)
    phone_yes_percentage = round((phone_yes / total_customers) * 100)

    phone_summary = {
        "Has phone service": phone_yes,
        "Has no phone service": phone_no,
        "Has phone service (%)": phone_yes_percentage,
        "Has no phone service (%)": phone_no_percentage
    }

    return phone_summary


def phone():
    return data['Phone_Service'].value_counts()


def internet_statistics():
    dsl = data['Internet_Service'].value_counts()['DSL']
    fiber = data['Internet_Service'].value_counts()['Fiber_optic']
    internet_no = data['Internet_Service'].value_counts()['No']
    total_customers = dsl + fiber + internet_no

    dsl_percentage = round((dsl / total_customers) * 100)
    fiber_percentage = round((fiber / total_customers) * 100)
    internet_no_percentage = round((internet_no / total_customers) * 100)

    internet_summary = {
        "Has dsl service": dsl,
        "Has fiber optic service": fiber,
        "Has no internet service": internet_no,
        "Has dsl service (%)": dsl_percentage,
        "Has fiber optic service (%)": fiber_percentage,
        "Has no internet service (%)": internet_no_percentage
    }

    return internet_summary


def internet():
    return data['Internet_Service'].value_counts()


def streaming_tv_statistics():
    tv_yes = data['Streaming_TV'].value_counts()['Yes']
    tv_no = data['Streaming_TV'].value_counts()['No']
    internet_no = data['Streaming_TV'].value_counts()['No_internet_service']
    total_customers = tv_yes + tv_no + internet_no

    tv_yes_percentage = round((tv_yes / total_customers) * 100)
    tv_no_percentage = round((tv_no / total_customers) * 100)
    internet_no_percentage = round((internet_no / total_customers) * 100)

    streaming_tv_summary = {
        "Has TV service": tv_yes,
        "Has no TV service": tv_no,
        "Has no internet service": internet_no,
        "Has TV service (%)": tv_yes_percentage,
        "Has no TV service (%)": tv_no_percentage,
        "Has no internet service (%)": internet_no_percentage
    }

    return streaming_tv_summary


def streaming_tv():
    return data['Streaming_TV'].value_counts()
