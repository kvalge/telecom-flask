import matplotlib.pyplot as plt
import numpy as np
import squarify
import seaborn as sns
import statsmodels.api as sm

from data_analysis_functions import tenure, monthly_charges, total_charges


def tenure_histogram(tenure_data):
    summary_statistics_histogram(tenure_data, 'tenure')


def tenure_boxplot(tenure_data):
    summary_statistics_boxplot(tenure_data, 'tenure')


def monthly_charges_histogram(charges_data):
    summary_statistics_histogram(charges_data, 'monthly charges')


def monthly_charges_boxplot(charges_data):
    summary_statistics_boxplot(charges_data, 'monthly charges')


def total_charges_histogram(charges_data):
    summary_statistics_histogram(charges_data, 'total charges')


def total_charges_boxplot(charges_data):
    summary_statistics_boxplot(charges_data, 'total charges')


def total_charges_qqplot(charges_data):
    sm.qqplot(charges_data, line='45')
    plt.title('Total Charges QQ-Plot ')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')

    plt.savefig('static/graphs/total_charges_qqplot.png')
    plt.close()


def churn_pie(churn_data):
    labels = churn_data.index
    sizes = churn_data.values
    colors = ['#0B9AB6', '#034362']
    explode = (0, 0.1)
    plt.figure(figsize=(3, 3))
    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    plt.savefig('static/graphs/churn_pie.png')
    plt.close()


def tenure_churn_bar(tenure_churn_data):
    churn_bar(tenure_churn_data, 'tenure')


def monthly_charges_churn_bar(monthly_charges_churn_data):
    churn_bar(monthly_charges_churn_data, 'monthly charges')


def monthly_total_churn_bar(summary):
    fig, ax = plt.subplots(figsize=(8, 5))
    bar_width = 0.9
    indices = np.arange(len(summary))

    total_charges = summary['Yes'] + summary['No']
    total_charges_sum = total_charges.sum()

    bars_terminated = ax.bar(indices, summary['Yes'], bar_width, label='Terminated', color='#034362')
    bars_active = ax.bar(indices, summary['No'], bar_width, bottom=summary['Yes'], label='Active', color='#0B9AB6')
    ax.set_title('Total Revenue by Monthly Charges and Churn')
    ax.set_xlabel('Monthly Charges')
    ax.set_ylabel('Total Charges')
    ax.set_xticks(indices)
    ax.set_xticklabels([f'{interval.left:.0f}-{interval.right:.0f}' for interval in summary.index], rotation=0)
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    ax.legend()

    for i, (bar_terminated, bar_active) in enumerate(zip(bars_terminated, bars_active)):
        bar_total = bar_terminated.get_height() + bar_active.get_height()
        percentage = (bar_total / total_charges_sum) * 100
        ax.text(bar_terminated.get_x() + bar_terminated.get_width() / 2,
                bar_total,
                f'{percentage:.1f}%',
                ha='center',
                va='bottom',
                fontsize=8)

    explanation = (
        "Percentage shows share of total charges \nof every monthly charges bin of \nall sum of total charges"
    )
    plt.gcf().text(0.32, 0.75, explanation, ha='center', va='top', fontsize=10, multialignment='left')

    plt.savefig('static/graphs/monthly_total_churn_bar.png')
    plt.close()


def total_revenue_by_tenure_churn_bar(summary):
    fig, ax = plt.subplots(figsize=(8, 5))
    bar_width = 0.9
    indices = np.arange(len(summary))

    tenure = summary['Yes'] + summary['No']
    total_charges_sum = tenure.sum()

    bars_terminated = ax.bar(indices, summary['Yes'], bar_width, label='Terminated', color='#034362')
    bars_active = ax.bar(indices, summary['No'], bar_width, bottom=summary['Yes'], label='Active', color='#0B9AB6')
    ax.set_title('Total Revenue by Tenure and Churn')
    ax.set_xlabel('Total Charges')
    ax.set_ylabel('Tenure')
    ax.set_xticks(indices)
    ax.set_xticklabels([f'{interval.left:.0f}-{interval.right:.0f}' for interval in summary.index], rotation=0)
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    ax.legend()

    for i, (bar_terminated, bar_active) in enumerate(zip(bars_terminated, bars_active)):
        bar_total = bar_terminated.get_height() + bar_active.get_height()
        percentage = (bar_total / total_charges_sum) * 100
        ax.text(bar_terminated.get_x() + bar_terminated.get_width() / 2,
                bar_total,
                f'{percentage:.1f}%',
                ha='center',
                va='bottom',
                fontsize=8)

    explanation = (
        "Percentage shows share of average tenure \nof every revenue bin of all tenures\n(churned + not churned)"
    )
    plt.gcf().text(0.32, 0.75, explanation, ha='center', va='top', fontsize=10, multialignment='left')

    plt.savefig('static/graphs/total_churn_bar.png')
    plt.close()


def age_group_bar(age_group_data):
    two_bars(age_group_data, 'age group', ['Age < 65', 'Age > 65'])


def churn_by_age_group_monthly_mean_bar(mean_data):
    churn_by_sociodem_spends_mean_bar(mean_data, 'age group', 'monthly')


def churn_by_age_group_total_mean_bar(mean_data):
    churn_by_sociodem_spends_mean_bar(mean_data, 'age group', 'total')


def partner_bar(partner_data):
    two_bars(partner_data, 'partner', ['Has no partner', 'Has partner'])


def churn_by_partner_monthly_mean_bar(mean_data):
    churn_by_sociodem_spends_mean_bar(mean_data, 'partner', 'monthly')


def churn_by_partner_total_mean_bar(mean_data):
    churn_by_sociodem_spends_mean_bar(mean_data, 'partner', 'total')


def dependents_bar(dependents_data):
    two_bars(dependents_data, 'dependents', ['Has no dependents', 'Has dependents'])


def churn_by_dependents_monthly_mean_bar(mean_data):
    churn_by_sociodem_spends_mean_bar(mean_data, 'dependents', 'monthly')


def churn_by_dependents_total_mean_bar(mean_data):
    churn_by_sociodem_spends_mean_bar(mean_data, 'dependents', 'total')


def av_tenure_by_sociodem_line(sociodem_data):
    av_by_sociodem_line(sociodem_data, 'tenure', tenure(), 5)


def av_monthly_charges_by_sociodem_line(sociodem_data):
    av_by_sociodem_line(sociodem_data, 'monthly charges', monthly_charges(), 10)


def av_total_charges_by_sociodem_line(sociodem_data):
    av_by_sociodem_line(sociodem_data, 'total charges', total_charges(), 500)


def phone_bar(phone_data):
    two_bars(phone_data, 'Phone Service', ['Has phone service', 'Has no phone service'])


def internet_bar(internet_data):
    three_bars(internet_data, 'internet service', ['fiber optic', 'dsl', 'has no internet service'])


def streaming_tv_bar(streaming_tv_data):
    three_bars(streaming_tv_data,
               'streaming service',
               ['has no tv', 'has tv', 'has no internet service'])


def phone_churn_monthly_heatmap(by_mean):
    service_churn_spends_heatmap(by_mean,
                                 'phone service',
                                 [00.5, 1.5],
                                 ['has no phone service', 'has phone service'],
                                 'Monthly')


def phone_churn_total_heatmap(by_mean):
    service_churn_spends_heatmap(by_mean,
                                 'phone service total',
                                 [00.5, 1.5],
                                 ['has no phone service', 'has phone service'],
                                 'Total')


def internet_churn_monthly_heatmap(by_mean):
    service_churn_spends_heatmap(by_mean,
                                 'internet service',
                                 [0.5, 1.5, 2.5],
                                 ['dsl', 'fiber optic', 'has no internet service'],
                                 'Monthly')


def internet_churn_total_heatmap(by_mean):
    service_churn_spends_heatmap(by_mean,
                                 'internet service total',
                                 [0.5, 1.5, 2.5],
                                 ['dsl', 'fiber optic', 'has no internet service'],
                                 'Total')


def streaming_tv_churn_monthly_heatmap(by_mean):
    service_churn_spends_heatmap(by_mean,
                                 'streaming',
                                 [0.5, 1.5, 2.5],
                                 ['has no tv', 'has no internet service', 'has tv'],
                                 'Monthly')


def streaming_tv_churn_total_heatmap(by_mean):
    service_churn_spends_heatmap(by_mean,
                                 'streaming total',
                                 [0.5, 1.5, 2.5],
                                 ['has no tv', 'has no internet service', 'has tv'],
                                 'Total')


def total_charges_churn_by_sociodem_treemap(sociodem_data):
    total_charges_churn_treemap(sociodem_data,
                                'sociodemographics',
                                ['Age over 65', 'Partner', 'Dependents'],
                                12,
                                9,
                                14)


def total_charges_churn_by_services_treemap(services_data):
    total_charges_churn_treemap(services_data,
                                'services',
                                ['Phone', 'Internet', 'TV'],
                                17,
                                14,
                                20)


def total_charges_churn_by_sociodem_and_services_treemap(sociodem_data):
    total_charges_churn_treemap(sociodem_data,
                                'sociodemographics&services',
                                ['Age over 65', 'Partner', 'Dependents', 'Phone', 'Internet', 'TV'],
                                12,
                                9,
                                14)


def summary_statistics_histogram(tenure_data, name):
    plt.figure(figsize=(10, 6))
    plt.hist(tenure_data, bins=25, color='#0B9AB6', edgecolor='w', alpha=0.95)
    plt.ylabel('Number of Contracts')
    plt.title(f'Distribution of {name.title()}')

    plt.savefig(f'static/graphs/{name.replace(" ", "_")}_histogram.png')
    plt.close()


def summary_statistics_boxplot(tenure_data, name):
    plt.figure(figsize=(5, 1.5))
    box_plot = plt.boxplot(tenure_data, vert=False, patch_artist=True, boxprops=dict(facecolor='#0B9AB6'), widths=0.6)
    for median in box_plot['medians']:
        median.set_color('white')
    plt.xticks(fontsize=7)
    plt.yticks([])
    plt.xlabel(f'{name.title()}', fontsize=7)
    plt.tight_layout()

    plt.savefig(f'static/graphs/{name.replace(" ", "_")}_boxplot.png')
    plt.close()


def churn_bar(tenure_churn_data, name):
    fig, ax = plt.subplots(figsize=(8, 5))
    tenure_churn_data.plot(kind='bar', stacked=True, color=['#0B9AB6', '#034362'], edgecolor='w', width=1, ax=ax)
    plt.title(f'Churn by {name.title()}')
    plt.xlabel(f'{name.title()}')
    plt.xticks(rotation=0, fontsize=6)
    plt.yticks(fontsize=7)
    plt.legend(title='Churn')
    for container in ax.containers:
        ax.bar_label(container, label_type='center', fmt='%.2f', fontsize=8, color='white')
    plt.tight_layout()

    plt.savefig(f'static/graphs/{name.replace(" ", "_")}_churn_bar.png')
    plt.close()


def two_bars(data, name, labels):
    plt.figure(figsize=(5, 3))
    bars = plt.bar(data.index, data.values, color=['#0B9AB6', '#034362'])
    plt.title(f'{name.title()}')
    plt.ylabel('Number of Contracts', fontsize=7)
    plt.yticks(fontsize=7)
    plt.xticks(ticks=[0, 1], labels=labels, fontsize=8)

    data_sum = sum(list(data))
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, f'{round(yval / data_sum * 100)}%', va='top',
                 ha='center', color='white',
                 fontsize=10)

    plt.savefig(f'static/graphs/{name.replace(" ", "_")}_bar.png')
    plt.close()


def three_bars(data, name, labels):
    plt.figure(figsize=(5, 3))
    bars = plt.bar(data.index, data.values, color=['#0B9AB6', '#0283C5', '#034362'])
    plt.title(f'{name.title()}')
    plt.ylabel('Number of Contracts', fontsize=7)
    plt.yticks(fontsize=7)
    plt.xticks(ticks=[0, 1, 2], labels=labels, fontsize=8)

    data_sum = sum(list(data))
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval - yval * 0.1, f'{round(yval / data_sum * 100)}%', va='top',
                 ha='center', color='white',
                 fontsize=10)

    plt.savefig(f'static/graphs/{name.replace(" ", "_")}_bar.png')
    plt.close()


def churn_by_sociodem_spends_mean_bar(mean_data, name, spend_period):
    data = dict(sorted(mean_data.items(), key=lambda item: item[1]))

    labels = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots(figsize=(5, 2))
    color = ['#0B9AB6' if 'Active' in label else '#034362' for label in labels]
    data_sum = sum(values)
    bar_widths = [val / data_sum * 100 for val in values]
    bars = ax.barh(labels, bar_widths, height=0.9, color=color)
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2,
                f'{round(width)}% ', ha='right', va='center', color='white')

    plt.xticks(fontsize=7)
    plt.yticks(fontsize=7)
    plt.title(f'Share of average {spend_period} charges\nby churn and {name}')
    plt.tight_layout()

    plt.savefig(f'static/graphs/churn_by_{name.replace(" ", "_")}_{spend_period}_mean_bar.png')
    plt.close()


def av_by_sociodem_line(sociodem_data, name, data_function, y_tick_width):
    plt.figure(figsize=(6, 4))
    color = ['#0B9AB6', '#0283C5', '#034362']

    sociodem_data[0].plot(kind='line', marker='o', color=color[0], label='Over 65')
    sociodem_data[1].plot(kind='line', marker='o', color=color[1], label='Dependents')
    sociodem_data[2].plot(kind='line', marker='o', color=color[2], label='Partner')

    plt.title(f'Average {name.title()} by Sociodem')
    plt.xlabel('Sociodemographics')
    plt.ylabel(f'Average {name.title()}')
    plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
    y_ticks = np.arange(0, data_function.iloc[-1] + 1, y_tick_width)
    plt.yticks(ticks=y_ticks, labels=[str(int(round(tick))) for tick in y_ticks])
    plt.yticks(fontsize=7)
    plt.legend()

    plt.savefig(f'static/graphs/{name.replace(" ", "_")}_by_sociodem_line.png')
    plt.close()


def total_charges_churn_treemap(data, name, labels, fig1, fig2, title_size):
    total_sum = data.sum()
    total_sum_percentage = data / total_sum * 100

    label_texts = []
    for key, value in zip(total_sum_percentage.index, total_sum_percentage.values):
        label_text = f'Churn: {key[0]}'
        for i, label in enumerate(labels):
            label_text += f'\n{label}: {key[i + 1]}'
        label_text += f'\n{value:.1f}%'
        label_texts.append(label_text)

    sizes = total_sum_percentage.values

    fig, ax = plt.subplots(1, 1, figsize=(fig1, fig2))
    color = ['#034362', '#0e5d83', '#2183b2', '#3d9fce', '#56add7', '#6abae1', '#81c4e5',
             '#97cde8', '#b6dcef', '#8fabb9', '#6c91a4', '#48758c', '#2c556b', '#0B9AB6']

    squarify.plot(sizes=sizes, label=label_texts, ax=ax, alpha=0.8, color=color)
    ax.axis('off')
    plt.title(f'Total Charges Percentage by Churn and {name.title()}', fontsize=title_size)
    plt.tight_layout()

    plt.savefig(f'static/graphs/total_charges_churn_by_{name}_treemap.png')
    plt.close()


def service_churn_spends_heatmap(by_mean, name, ticks, labels, period):
    colors = ["#034362", "#0e5d83", "#0283C5", "#56add7", "#81c4e5", "#f1f5f6"]
    cmap = sns.color_palette(colors, as_cmap=True)

    plt.figure(figsize=(5, 4))
    ax = sns.heatmap(by_mean, annot=True, cmap=cmap, linewidths=.5, fmt=".2f", cbar=False)
    plt.title(f'Av. {period} Charges by Churn and {name.title()}')
    ax.set_xlabel(None)
    plt.ylabel('Churn')
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels, minor=False, fontsize=7, ha='center')

    plt.savefig(f'static/graphs/{name.replace(" ", "_")}_heatmap.png')
    plt.close()
