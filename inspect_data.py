from data.read_data import read_data
import pandas as pd
import statsmodels.api as sm


def inspect_data():
    data = read_data()

    file = open('data_insight/basic_insight.txt', 'w')

    file.write('Number of rows: {}\n'.format(data.shape[0]))
    file.write('Number of columns: {}\n'.format(data.shape[1]) + '\n')

    file.write(f'Column types: \n{data.dtypes}\n' + '\n')

    missing_values_count = data.isnull().sum()
    file.write(f'Missing values: \n{missing_values_count}\n' + '\n')

    column_name = 'Total_Charges'
    numeric_column = pd.to_numeric(data[column_name], errors='coerce')
    invalid_rows = data[numeric_column.isna()]
    file.write(f'Rows of missing values of "Total Charges" column: \n{invalid_rows}\n' + '\n')

    data['Total_Charges'] = pd.to_numeric(data['Total_Charges'], errors='coerce')
    data.dropna(subset=['Total_Charges'])

    file.write(f'Summary statistics: {data[["Tenure", "Monthly_Charges", "Total_Charges"]].describe()}\n' + '\n')

    file.write('Data of the first row:\n {}\n'.format(data.iloc[0]) + '\n')

    file.write('Selecting a section of first 3 rows of customers id and monthly charges:\n {}\n'.format(
        data[['Customer_ID', 'Monthly_Charges']].iloc[0:3]) + '\n')

    file.write('Selecting a cell of first id: \n {}\n'.format(data[['Customer_ID']].iloc[0]) + '\n')

    file.write('Selecting a cell of first id: \n {}\n'.format(data.at[0, 'Customer_ID']) + '\n')

    file.write('Mean of monthly charges: {0}\nMax of monthly charges: {1}\nMin of monthly charges: {2}: \n'
               .format(data['Monthly_Charges'].mean(), data['Monthly_Charges'].max(),
                       data['Monthly_Charges'].min()) + '\n')

    filtered_total_charges = data[data['Total_Charges'] != '_']
    file.write('Mean of total charges: {0}\nMax of total charges: {1}\nMin of total charges: {2}: \n'
               .format(filtered_total_charges['Total_Charges'].mean(),
                       filtered_total_charges['Total_Charges'].max(),
                       filtered_total_charges['Total_Charges'].min()) + '\n')

    count_churn = data.groupby(['Churn'])['Churn'].count()
    file.write('Count of churn: \n{}\n'.format(count_churn) + '\n')

    count_senior = data.groupby(['Senior_Citizen'])['Senior_Citizen'].count()
    file.write('Number of customers under and over 65: \n{}\n'.format(count_senior) + '\n')

    count_partner = data.groupby(['Partner'])['Partner'].count()
    file.write('Number of customers without and with partner: \n{}\n'.format(count_partner) + '\n')

    count_dependents = data.groupby(['Dependents'])['Dependents'].count()
    file.write('Number of customers without and with dependents: \n{}\n'.format(count_dependents) + '\n')

    file.write('Mean of tenure: {0}\nMax of tenure: {1}\nMin of tenure: {2}: \n'
               .format(data['Tenure'].mean(), data['Tenure'].max(), data['Tenure'].min()) + '\n')

    count_phone_service = data.groupby(['Phone_Service'])['Phone_Service'].count()
    file.write('Count of phone services: \n{}\n'.format(count_phone_service) + '\n')

    count_multiple_lines = data.groupby(['Multiple_Lines'])['Multiple_Lines'].count()
    file.write('Count of multiple telephone lines service: \n{}\n'.format(count_multiple_lines) + '\n')

    count_internet_service = data.groupby(['Internet_Service'])['Internet_Service'].count()
    file.write('Count of internet service: \n{}\n'.format(count_internet_service) + '\n')

    count_online_security = data.groupby(['Online_Security'])['Online_Security'].count()
    file.write('Count of online security service: \n{}\n'.format(count_online_security) + '\n')

    count_online_backup = data.groupby(['Online_Backup'])['Online_Backup'].count()
    file.write('Count of online backup service: \n{}\n'.format(count_online_backup) + '\n')

    count_device_protection = data.groupby(['Device_Protection'])['Device_Protection'].count()
    file.write('Count of device protection service: \n{}\n'.format(count_device_protection) + '\n')

    count_tech_support = data.groupby(['Tech_Support'])['Tech_Support'].count()
    file.write('Count of tech support: \n{}\n'.format(count_tech_support) + '\n')

    count_streaming_tv = data.groupby(['Streaming_TV'])['Streaming_TV'].count()
    file.write('Count of streaming TV: \n{}\n'.format(count_streaming_tv) + '\n')

    count_streaming_movies = data.groupby(['Streaming_Movies'])['Streaming_Movies'].count()
    file.write('Count of streaming movies service: \n{}\n'.format(count_streaming_movies) + '\n')

    count_contract = data.groupby(['Contract'])['Contract'].count()
    file.write('Count of contracts by period: \n{}\n'.format(count_contract) + '\n')

    count_contract = data.groupby(['Contract'])['Contract'].count()
    file.write('Count of contracts by period: \n{}\n'.format(count_contract) + '\n')

    count_paperless_billing = data.groupby(['Paperless_Billing'])['Paperless_Billing'].count()
    file.write('Count of billing by type: \n{}\n'.format(count_paperless_billing) + '\n')

    count_payment_method = data.groupby(['Payment_Method'])['Payment_Method'].count()
    file.write('Count of payment method by type: \n{}\n'.format(count_payment_method) + '\n')

    count_payment_method = data.groupby(['Payment_Method'])['Payment_Method'].count()
    file.write('Count of payment method by type: \n{}\n'.format(count_payment_method) + '\n')

    churn_count = data[data.Churn == 'Yes'].groupby('Senior_Citizen').agg({'Churn': 'count'}).reset_index()
    churn_count['percentage'] = 100 * churn_count.Churn / churn_count.Churn.sum()
    file.write(f'Churn share by age group:\n{round(churn_count, 2)}\n' + '\n')

    tenure_mean_std_by_churn = data.groupby('Churn').agg({'Tenure': ['mean', 'std']}).reset_index()
    file.write(f'Tenure mean and std by churn:\n{round(tenure_mean_std_by_churn, 2)}\n' + '\n')


# How different categorical variables impact tenure
    x = pd.get_dummies(
        data[['Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 'Internet_Service', 'Streaming_TV']],
        drop_first=True)
    y = data['Tenure']
    x = sm.add_constant(x)
    model = sm.OLS(y, x.astype(float)).fit()
    file.write(f'{model.summary()}\n' + '\n')

    # How different categorical variables impact monthly charges
    y = data['Monthly_Charges']
    x = sm.add_constant(x)
    model = sm.OLS(y, x.astype(float)).fit()
    file.write(f'{model.summary()}')

    file.close()


inspect_data()
