from flask import Flask, render_template, request
from data_analysis_functions import *
from graphs_generation import *
from functions import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def summary():
    tenure_stat = tenure_summary_statistics()
    tenure_data = tenure()
    tenure_histogram(tenure_data)
    tenure_boxplot(tenure_data)

    monthly_stat = monthly_charges_summary_statistics()
    charges_data = monthly_charges()
    monthly_charges_histogram(charges_data)
    monthly_charges_boxplot(charges_data)

    total_stat = total_charges_summary_statistics()
    total_data = total_charges()
    total_charges_histogram(total_data)
    total_charges_boxplot(total_data)

    churn_stat = churn_statistics()
    churn_data = churn()
    churn_pie(churn_data)

    message = ''
    if request.method == "POST":
        text = request.form.get('conclusions').strip().capitalize()
        source_page = f'Summary page: '
        if text and len(text.strip()) > 1:
            save_conclusions(source_page, text)

    return render_template('summary.html',
                           monthly_stat=monthly_stat,
                           total_stat=total_stat,
                           tenure_stat=tenure_stat,
                           churn_stat=churn_stat,
                           message=message)


@app.route('/churn', methods=['GET', 'POST'])
def churn_page():
    tenure_churn_data = tenure_churn()
    tenure_churn_bar(tenure_churn_data)

    monthly_charges_churn_data = monthly_charges_churn()
    monthly_charges_churn_bar(monthly_charges_churn_data)

    monthly_total_churn_data = monthly_total_charges_churn()
    monthly_total_churn_bar(monthly_total_churn_data)

    total_churn_data = total_charges_churn()
    total_revenue_by_tenure_churn_bar(total_churn_data)

    if request.method == "POST":
        text = request.form.get('conclusions').strip().capitalize()
        source_page = f'{request.path[1:].capitalize()} page: '
        if text and len(text.strip()) > 1:
            save_conclusions(source_page, text)

    return render_template('churn.html')


@app.route('/sociodem', methods=['GET', 'POST'])
def sociodem_page():
    age_group_stat = age_group_statistics()
    age_group_data = age_group()
    age_group_bar(age_group_data)

    partner_stat = partner_statistics()
    partner_data = partner()
    partner_bar(partner_data)

    dependents_stat = dependents_statistics()
    dependents_data = dependents()
    dependents_bar(dependents_data)

    by_age_group = churn_by_age_group_monthly_mean()
    by_age_group_total = churn_by_age_group_total_mean()
    by_partner = churn_by_partner_monthly_mean()
    by_partner_total = churn_by_partner_total_mean()
    by_dependents = churn_by_dependents_monthly_mean()
    by_dependents_total = churn_by_dependents_total_mean()

    churn_by_age_group_monthly_mean_bar(by_age_group)
    churn_by_age_group_total_mean_bar(by_age_group_total)
    churn_by_partner_monthly_mean_bar(by_partner)
    churn_by_partner_total_mean_bar(by_partner_total)
    churn_by_dependents_monthly_mean_bar(by_dependents)
    churn_by_dependents_total_mean_bar(by_dependents_total)

    tenure_by_sociodem = av_tenure_by_sociodem()
    av_tenure_by_sociodem_line(tenure_by_sociodem)

    charges_by_sociodem = av_monthly_charges_by_sociodem()
    av_monthly_charges_by_sociodem_line(charges_by_sociodem)

    total_charges_by_sociodem = av_total_charges_by_sociodem()
    av_total_charges_by_sociodem_line(total_charges_by_sociodem)

    if request.method == "POST":
        text = request.form.get('conclusions').strip().capitalize()
        source_page = f'{request.path[1:].capitalize()} page: '
        if text and len(text.strip()) > 1:
            save_conclusions(source_page, text)

    return render_template('sociodem.html',
                           age_group_stat=age_group_stat,
                           partner_stat=partner_stat,
                           dependents_stat=dependents_stat,
                           by_age_group=by_age_group,
                           by_age_group_total=by_age_group_total,
                           by_dependents=by_dependents,
                           by_dependents_total=by_dependents_total,
                           by_partner=by_partner,
                           by_partner_total=by_partner_total,
                           )


@app.route('/services', methods=['GET', 'POST'])
def services_page():
    phone_stat = phone_statistics()
    phone_data = phone()
    phone_bar(phone_data)

    internet_stat = internet_statistics()
    internet_data = internet()
    internet_bar(internet_data)

    streaming_tv_stat = streaming_tv_statistics()
    streaming_tv_data = streaming_tv()
    streaming_tv_bar(streaming_tv_data)

    by_phone = churn_by_phone_monthly_mean()
    by_phone_total = churn_by_phone_total_mean()
    by_internet = churn_by_internet_monthly_mean()
    by_internet_total = churn_by_internet_total_mean()
    by_streaming_tv = churn_by_streaming_tv_monthly_mean()
    by_streaming_tv_total = churn_by_streaming_tv_total_mean()

    phone_churn_monthly_heatmap(churn_by_phone_monthly_mean_data())
    phone_churn_total_heatmap(churn_by_phone_total_mean_data())
    internet_churn_monthly_heatmap(churn_by_internet_monthly_mean_data())
    internet_churn_total_heatmap(churn_by_internet_total_mean_data())
    streaming_tv_churn_monthly_heatmap(churn_by_streaming_tv_monthly_mean_data())
    streaming_tv_churn_total_heatmap(churn_by_streaming_tv_total_mean_data())

    if request.method == "POST":
        text = request.form.get('conclusions').strip().capitalize()
        source_page = f'{request.path[1:].capitalize()} page: '
        if text and len(text.strip()) > 1:
            save_conclusions(source_page, text)

    return render_template('services.html',
                           phone_stat=phone_stat,
                           internet_stat=internet_stat,
                           streaming_tv_stat=streaming_tv_stat,
                           by_phone=by_phone,
                           by_phone_total=by_phone_total,
                           by_internet=by_internet,
                           by_internet_total=by_internet_total,
                           by_streaming_tv=by_streaming_tv,
                           by_streaming_tv_total=by_streaming_tv_total)


@app.route('/profitability', methods=['GET', 'POST'])
def profitability_page():
    total_charges_churn_by_sociodem_treemap(total_charges_churn_by_sociodem())
    total_charges_churn_by_services_treemap(total_charges_churn_by_services())
    total_charges_churn_by_sociodem_and_services_treemap(total_charges_churn_by_sociodem_and_services())

    if request.method == "POST":
        text = request.form.get('conclusions').strip().capitalize()
        source_page = f'{request.path[1:].capitalize()} page: '
        if text and len(text.strip()) > 1:
            save_conclusions(source_page, text)

    return render_template('profitability.html')


@app.route('/tests', methods=['GET', 'POST'])
def tests_page():
    if request.method == "POST":
        text = request.form.get('conclusions').strip().capitalize()
        source_page = f'{request.path[1:].capitalize()} page: '
        if text and len(text.strip()) > 1:
            save_conclusions(source_page, text)

    return render_template('tests.html')


@app.route('/models', methods=['GET', 'POST'])
def models_page():
    tenure_model_summary()
    monthly_charges_model_summary()
    total_charges_model_summary()

    if request.method == "POST":
        text = request.form.get('conclusions').strip().capitalize()
        source_page = f'{request.path[1:].capitalize()} page: '
        if text and len(text.strip()) > 1:
            save_conclusions(source_page, text)

    return render_template('models.html')


@app.route('/conclusions', methods=['GET', 'POST'])
def conclusions_page(conclusion_to_update=None):
    conclusions = get_conclusions()
    message = ''

    if len(conclusions) == 0:
        message = "No conclusions saved yet."

    if request.method == "POST":
        if conclusion_to_update:
            text = request.form.get('conclusions')
            if text and len(text.strip()) > 1:
                delete(conclusion_to_update[0][0])
                text = text.strip().capitalize()
                page_name = conclusion_to_update[0][1].strip().split(':', 1)
                source_page = f'{page_name[0].capitalize()}: '
                save_conclusions(source_page, text)

                conclusions = get_conclusions()

                return render_template('conclusions.html',
                                       conclusions=conclusions)

    return render_template('conclusions.html',
                           conclusions=conclusions,
                           message=message,
                           conclusion_to_update=conclusion_to_update)


@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    updated_conclusions = []

    try:
        with open('data_insight/conclusions.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split('-', 1)
                if parts[0] != id:
                    updated_conclusions.append(parts[1])
    except FileNotFoundError:
        print("File not found!")

    clear_file('data_insight/conclusions.txt')

    for conclusion in updated_conclusions:
        save_conclusions(None, conclusion)

    return conclusions_page(None)


@app.route('/edit/<id>', methods=['POST'])
def edit(id):
    conclusion_to_update = []

    try:
        with open('data_insight/conclusions.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split('-', 1)
                if parts[0] == id:
                    conclusion_to_update.append([parts[0], parts[1]])
                    break
    except FileNotFoundError:
        print("File not found!")

    return conclusions_page(conclusion_to_update)


if __name__ == '__main__':
    app.run(debug=True)
