import matplotlib.pyplot as plt
import numpy as np


def tenure_histogram(tenure_data):
    plt.figure(figsize=(10, 6))
    plt.hist(tenure_data, bins=25, color='#034362', edgecolor='w', alpha=0.95)
    plt.xlabel('Tenure')
    plt.ylabel('Number of Contracts')
    plt.title('Distribution of Tenure')

    plt.savefig('static/graphs/tenure_histogram.png')
    plt.close()


def tenure_boxplot(tenure_data):
    plt.figure(figsize=(6, 2))
    box_plot = plt.boxplot(tenure_data, vert=False, patch_artist=True, boxprops=dict(facecolor='#034362'))
    for median in box_plot['medians']:
        median.set_color('white')
    plt.yticks([])

    plt.savefig('static/graphs/tenure_boxplot.png')
    plt.close()


def monthly_charges_histogram(charges_data):
    plt.figure(figsize=(10, 6))
    plt.hist(charges_data, bins=25, color='#034362', edgecolor='w', alpha=0.95)
    plt.xlabel('Monthly Charges')
    plt.ylabel('Number of Contracts')
    plt.title('Distribution of Monthly Charges')

    plt.savefig('static/graphs/monthly_charges_histogram.png')
    plt.close()


def monthly_charges_boxplot(charges_data):
    plt.figure(figsize=(6, 2))
    box_plot = plt.boxplot(charges_data, vert=False, patch_artist=True, boxprops=dict(facecolor='#034362'))
    for median in box_plot['medians']:
        median.set_color('white')
    plt.yticks([])

    plt.savefig('static/graphs/monthly_charges_boxplot.png')
    plt.close()


def churn_pie(churn_data):
    labels = churn_data.index
    sizes = churn_data.values
    colors = ['#0B9AB6', '#034362']
    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    plt.savefig('static/graphs/churn_pie.png')
    plt.close()


def tenure_churn_bar(tenure_churn_data):
    fig, ax = plt.subplots(figsize=(8, 5))
    tenure_churn_data.plot(kind='bar', stacked=True, color=['#0B9AB6', '#034362'], edgecolor='w', width=1, ax=ax)
    plt.title('Churn by Tenure')
    plt.xlabel('Tenure')
    plt.xticks(rotation=0, fontsize=7)
    plt.legend(title='Churn')
    for container in ax.containers:
        ax.bar_label(container, label_type='center', fmt='%.2f', fontsize=8, color='white')
    plt.tight_layout()

    plt.savefig('static/graphs/tenure_churn_bar.png')
    plt.close()


def monthly_charges_churn_bar(monthly_charges_churn_data):
    fig, ax = plt.subplots(figsize=(8, 5))
    monthly_charges_churn_data.plot(kind='bar', stacked=True, color=['#0B9AB6', '#034362'], edgecolor='w', width=1,
                                    ax=ax)
    plt.title('Churn by Monthly Charges')
    plt.xlabel('Monthly Charges')
    plt.xticks(rotation=0, fontsize=6)
    plt.legend(title='Churn')
    for container in ax.containers:
        ax.bar_label(container, label_type='center', fmt='%.2f', fontsize=8, color='white')
    plt.tight_layout()

    plt.savefig('static/graphs/monthly_charges_churn_bar.png')
    plt.close()


def monthly_total_churn_bar(summary):
    fig, ax = plt.subplots(figsize=(8, 5))
    bar_width = 0.9
    indices = np.arange(len(summary))
    ax.bar(indices, summary['Yes'], bar_width, label='Churn Yes', color='#034362')
    ax.bar(indices, summary['No'], bar_width, bottom=summary['Yes'], label='Churn No', color='#0B9AB6')
    ax.set_title('Total Revenue by Monthly Charges and Churn')
    ax.set_xlabel('Monthly Charges')
    ax.set_ylabel('Total Charges')
    ax.set_xticks(indices)
    ax.set_xticklabels([f'{interval.left:.0f}-{interval.right:.0f}' for interval in summary.index], rotation=0)
    ax.legend()

    plt.savefig('static/graphs/monthly_total_churn_bar.png')
    plt.close()


def age_group_bar(age_group_data):
    plt.figure(figsize=(6, 4))
    bars = plt.bar(age_group_data.index, age_group_data.values, color=['#0B9AB6', '#034362'])
    plt.title('Age Group')
    plt.ylabel('Number of Contracts')
    plt.xticks(ticks=[0, 1], labels=['Age < 65', 'Age > 65'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, yval, va='top', ha='center', color='white',
                 fontsize=10)

    plt.savefig('static/graphs/age_group_bar.png')
    plt.close()


def partner_bar(partner_data):
    plt.figure(figsize=(6, 4))
    bars = plt.bar(partner_data.index, partner_data.values, color=['#0B9AB6', '#034362'])
    plt.title('Partnership')
    plt.ylabel('Number of Contracts')
    plt.xticks(ticks=[0, 1], labels=['Has no partner', 'Has partner'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, yval, va='top', ha='center', color='white',
                 fontsize=10)

    plt.savefig('static/graphs/partner_bar.png')
    plt.close()


def dependents_bar(dependents_data):
    plt.figure(figsize=(6, 4))
    bars = plt.bar(dependents_data.index, dependents_data.values, color=['#0B9AB6', '#034362'])
    plt.title('Dependents')
    plt.ylabel('Number of Contracts')
    plt.xticks(ticks=[0, 1], labels=['Has no dependents', 'Has dependents'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, yval, va='top', ha='center', color='white',
                 fontsize=10)

    plt.savefig('static/graphs/dependents_bar.png')
    plt.close()


def phone_bar(phone_data):
    plt.figure(figsize=(6, 4))
    bars = plt.bar(phone_data.index, phone_data.values, color=['#0B9AB6', '#034362'])
    plt.title('Phone Service')
    plt.ylabel('Number of Contracts')
    plt.xticks(ticks=[0, 1], labels=['Has phone service', 'Has no phone service'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, yval, va='top', ha='center', color='white',
                 fontsize=10)

    plt.savefig('static/graphs/phone_bar.png')
    plt.close()


def internet_bar(internet_data):
    plt.figure(figsize=(6, 4))
    bars = plt.bar(internet_data.index, internet_data.values, color=['#0B9AB6', '#0283C5', '#034362'])
    plt.title('Internet Service')
    plt.ylabel('Number of Contracts')
    plt.xticks(ticks=[0, 1, 2], labels=['fiber optic', 'dsl', 'has no internet service'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, yval, va='top', ha='center', color='white',
                 fontsize=10)

    plt.savefig('static/graphs/internet_bar.png')
    plt.close()


def streaming_tv_bar(streaming_tv_data):
    plt.figure(figsize=(6, 4))
    bars = plt.bar(streaming_tv_data.index, streaming_tv_data.values, color=['#0B9AB6', '#0283C5', '#034362'])
    plt.title('Streaming TV Service')
    plt.ylabel('Number of Contracts')
    plt.xticks(ticks=[0, 1, 2], labels=['has no tv', 'has tv', 'has no internet service'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, yval, va='top', ha='center', color='white',
                 fontsize=10)

    plt.savefig('static/graphs/streaming_tv_bar.png')
    plt.close()
