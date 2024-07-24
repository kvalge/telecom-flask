from data.clean_data import clean_data
import pandas as pd
import numpy as np
import statsmodels.api as sm

data = clean_data()


def tenure_summary_statistics():
    return summary_statistics('Tenure')


def tenure():
    return data['Tenure']


def monthly_charges_summary_statistics():
    return summary_statistics('Monthly_Charges')


def monthly_charges():
    return data['Monthly_Charges']


def total_charges_summary_statistics():
    return summary_statistics('Total_Charges')


def total_charges():
    return data['Total_Charges']


def summary_statistics(variable):
    variable_mean = round(data[variable].mean(), 1)
    variable_median = round(data[variable].median(), 1)
    variable_min = round(data[variable].min(),1)
    variable_max = round(data[variable].max(),1)
    variable_q1 = round(data[variable].quantile(0.25), 1)
    variable_q3 = round(data[variable].quantile(0.75), 1)
    variable_std = round(data[variable].std(), 1)
    variable_summary = {
        "Mean": variable_mean,
        "Median": variable_median,
        "Min": variable_min,
        "Max": variable_max,
        "Q1": variable_q1,
        "Q3": variable_q3,
        "Std": variable_std,
    }
    return variable_summary


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

    tenure_churn_summary = data.groupby(['Tenure_bin', 'Churn']).size().unstack(fill_value=0)

    tenure_churn_summary = tenure_churn_summary.div(tenure_churn_summary.sum(axis=1), axis=0)

    return tenure_churn_summary


def monthly_charges_churn():
    bins = np.arange(10, data['Monthly_Charges'].max() + 10, 10)
    data['Monthly_Charges_bin'] = pd.cut(data['Monthly_Charges'], bins=bins, right=False)

    monthly_churn_summary = data.groupby(['Monthly_Charges_bin', 'Churn']).size().unstack(fill_value=0)

    monthly_churn_summary = monthly_churn_summary.div(monthly_churn_summary.sum(axis=1), axis=0)

    return monthly_churn_summary


def monthly_total_charges_churn():
    bins = np.arange(10, max(list(monthly_charges())) + 10, 10)

    data['Monthly_Charges_bin'] = pd.cut(data['Monthly_Charges'], bins=bins)

    monthly_total_churn_summary = data.groupby(['Monthly_Charges_bin', 'Churn'])[
        'Total_Charges'].sum().unstack().fillna(0)

    return monthly_total_churn_summary


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


def churn_by_age_group_monthly_mean():
    mean = data.groupby(['Churn', 'Senior_Citizen'])['Monthly_Charges'].mean()

    by_mean = {
        'Active & Age < 65': round(list(mean)[0], 2),
        'Active & Age > 65': round(list(mean)[1], 2),
        'Terminated & Age < 65': round(list(mean)[2], 2),
        'Terminated & Age > 65': round(list(mean)[3], 2)
    }

    return by_mean


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


def churn_by_partner_monthly_mean():
    mean = data.groupby(['Churn', 'Partner'])['Monthly_Charges'].mean()

    by_mean = {
        'Active & Has no partner': round(list(mean)[0], 2),
        'Active & Has partner': round(list(mean)[1], 2),
        'Terminated & Has no partner': round(list(mean)[2], 2),
        'Terminated & Has partner': round(list(mean)[3], 2)
    }

    return by_mean


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


def churn_by_dependents_monthly_mean():
    mean = data.groupby(['Churn', 'Dependents'])['Monthly_Charges'].mean()

    by_mean = {
        'Active & Has no dependents': round(list(mean)[0], 2),
        'Active & Has dependents': round(list(mean)[1], 2),
        'Terminated & Has no dependents': round(list(mean)[2], 2),
        'Terminated & Has dependents': round(list(mean)[3], 2)
    }

    return by_mean


def av_tenure_by_sociodem():
    av_age = data.groupby('Senior_Citizen')['Tenure'].mean()
    av_dependents = data.groupby('Dependents')['Tenure'].mean()
    av_partner = data.groupby('Partner')['Tenure'].mean()

    return av_age, av_dependents, av_partner


def av_monthly_charges_by_sociodem():
    av_age = data.groupby('Senior_Citizen')['Monthly_Charges'].mean()
    av_dependents = data.groupby('Dependents')['Monthly_Charges'].mean()
    av_partner = data.groupby('Partner')['Monthly_Charges'].mean()

    return av_age, av_dependents, av_partner


def total_charges_churn_by_sociodem():
    total_charges = data.groupby(['Churn', 'Senior_Citizen', 'Partner', 'Dependents'])['Total_Charges'].sum()
    return total_charges


def total_charges_churn_by_services():
    total_charges = data.groupby(['Churn', 'Phone_Service', 'Internet_Service', 'Streaming_TV'])['Total_Charges'].sum()
    return total_charges


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


def churn_by_phone_monthly_mean():
    mean = data.groupby(['Churn', 'Phone_Service'])['Monthly_Charges'].mean()

    by_mean = {
        'Active & Has phone service': round(list(mean)[0], 2),
        'Active & Has no phone service': round(list(mean)[1], 2),
        'Terminated & Has phone service': round(list(mean)[2], 2),
        'Terminated & Has no phone service': round(list(mean)[3], 2)
    }

    return by_mean


def churn_by_phone_monthly_mean_data():
    mean = data.groupby(['Churn', 'Phone_Service'])['Monthly_Charges'].mean().unstack()

    return mean.round(2)


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


def churn_by_internet_monthly_mean():
    mean = data.groupby(['Churn', 'Internet_Service'])['Monthly_Charges'].mean()

    by_mean = {
        'Active & Has dsl service': round(list(mean)[0], 2),
        'Active & Has fiber optic service': round(list(mean)[1], 2),
        'Active & No internet service': round(list(mean)[2], 2),
        'Terminated & Has dsl service': round(list(mean)[3], 2),
        'Terminated & Has fiber optic service': round(list(mean)[4], 2),
        'Terminated & No internet service': round(list(mean)[5], 2)
    }

    return by_mean


def churn_by_internet_monthly_mean_data():
    mean = data.groupby(['Churn', 'Internet_Service'])['Monthly_Charges'].mean().unstack()

    return mean.round(2)


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


def churn_by_streaming_tv_monthly_mean():
    mean = data.groupby(['Churn', 'Streaming_TV'])['Monthly_Charges'].mean()

    by_mean = {
        'Active & Has no TV service': round(list(mean)[0], 2),
        'Active & Has no internet service': round(list(mean)[1], 2),
        'Active & Has TV service': round(list(mean)[2], 2),
        'Terminated & Has no TV service': round(list(mean)[3], 2),
        'Terminated & Has no internet service': round(list(mean)[4], 2),
        'Terminated & Has TV service': round(list(mean)[5], 2)
    }

    return by_mean


def churn_by_streaming_tv_monthly_mean_data():
    mean = data.groupby(['Churn', 'Streaming_TV'])['Monthly_Charges'].mean().unstack()

    return mean.round(2)


def tenure_model_summary():
    x = pd.get_dummies(
        data[['Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 'Internet_Service', 'Streaming_TV']],
        drop_first=True)
    y = data['Tenure']
    x = sm.add_constant(x)
    model = sm.OLS(y, x.astype(float)).fit()
    with open('templates/tenure_model_summary.html', 'w') as f:
        f.write(model.summary().as_html())


def monthly_charges_model_summary():
    x = pd.get_dummies(
        data[['Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 'Internet_Service', 'Streaming_TV']],
        drop_first=True)
    y = data['Monthly_Charges']
    x = sm.add_constant(x)
    model = sm.OLS(y, x.astype(float)).fit()
    with open('templates/monthly_charges_model_summary.html', 'w') as f:
        f.write(model.summary().as_html())


def total_charges_model_summary():
    x = pd.get_dummies(
        data[['Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 'Internet_Service', 'Streaming_TV']],
        drop_first=True)
    y = data['Total_Charges']
    x = sm.add_constant(x)
    model = sm.OLS(y, x.astype(float)).fit()
    with open('templates/total_charges_model_summary.html', 'w') as f:
        f.write(model.summary().as_html())
