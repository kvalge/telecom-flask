import matplotlib.pyplot as plt


def tenure_histogram(tenure_data):
    plt.figure(figsize=(10, 6))
    plt.hist(tenure_data, bins=25, color='#034362', edgecolor='w', alpha=0.95)
    plt.xlabel('Tenure')
    plt.ylabel('Frequency')
    plt.title('Distribution of Tenure')
    plt.savefig('static/graphs/tenure_histogram.png')
    plt.close()


def tenure_boxplot(tenure_data):
    plt.figure(figsize=(6, 2))
    plt.boxplot(tenure_data, vert=False, patch_artist=True, boxprops=dict(facecolor='#034362'))
    plt.yticks([])
    plt.savefig('static/graphs/tenure_boxplot.png')
    plt.close()


def monthly_charges_histogram(charges_data):
    plt.figure(figsize=(10, 6))
    plt.hist(charges_data, bins=25, color='#034362', edgecolor='w', alpha=0.95)
    plt.xlabel('Monthly Charges')
    plt.ylabel('Frequency')
    plt.title('Distribution of Monthly Charges')
    plt.savefig('static/graphs/monthly_charges_histogram.png')
    plt.close()


def monthly_charges_boxplot(charges_data):
    plt.figure(figsize=(6, 2))
    plt.boxplot(charges_data, vert=False, patch_artist=True, boxprops=dict(facecolor='#034362'))
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
    fig, ax = plt.subplots(figsize=(8, 7))

    tenure_churn_data.plot(kind='bar', stacked=True, color=['#0B9AB6', '#034362'], edgecolor='w', width=1, ax=ax)

    plt.title('Churn by Tenure')
    plt.xlabel('Tenure')
    plt.xticks(rotation=60)
    plt.legend(title='Churn')
    for container in ax.containers:
        ax.bar_label(container, label_type='center', fmt='%.2f', fontsize=8, color='white')

    plt.tight_layout()
    plt.savefig('static/graphs/tenure_churn_bar.png')
    plt.close()
