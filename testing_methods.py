import matplotlib.pyplot as plt
import numpy as np
import squarify
import seaborn as sns
import statsmodels.api as sm
import pandas as pd
import scipy.stats as stats

import pandas as pd

from data.read_data import read_data
from data_analysis_functions import tenure, monthly_charges, total_charges


# def total_charges_qqplot(charges_data):
#     sm.qqplot(charges_data, line='45')
#     plt.title('Total Charges QQ-Plot ')
#     plt.xlabel('Theoretical Quantiles')
#     plt.ylabel('Sample Quantiles')
#
#     # plt.savefig('static/graphs/total_charges_qqplot.png')
#     plt.show()
#     plt.close()
#
#
# charges_data = [
#     29.85, 1889.5, 108.15, 1840.75, 151.65, 820.5, 1949.4,
#     301.9, 3046.05, 3487.95, 587.45, 326.8, 5681.1, 5036.3
# ]
#
# total_charges_qqplot(charges_data)


# Lae andmed failist
# df = pd.read_csv('your_data_file.csv')
# charges_data = df['total_charges'].dropna().astype(float).values

# Q-Q plot
def total_charges_qqplot(charges_data):
    sm.qqplot(charges_data, line='45')

    plt.title('Total Charges QQ-Plot')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')

    # plt.savefig('static/graphs/total_charges_qqplot.png')
    plt.show()
    plt.close()


def clean_data():
    data = read_data()

    data['Total_Charges'] = pd.to_numeric(data['Total_Charges'], errors='coerce')
    data = data.dropna(subset=['Total_Charges'])

    return data


data = clean_data()
charges_data = data['Total_Charges']
total_charges_qqplot(charges_data)



# Shapiro-Wilk test
stat, p_value = stats.shapiro(charges_data)
print(f"Shapiro-Wilk Test: Statistics={stat}, p-value={p_value}")