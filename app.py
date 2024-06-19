from flask import Flask, render_template
from functions import *
from graphs_generation import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def statistics():
    tenure_stat = tenure_statistics()
    tenure_data = tenure()
    tenure_histogram(tenure_data)
    tenure_boxplot(tenure_data)

    monthly_stat = monthly_charges_statistics()
    charges_data = monthly_charges()
    monthly_charges_histogram(charges_data)
    monthly_charges_boxplot(charges_data)

    churn_stat = churn_statistics()
    churn_data = churn()
    churn_pie(churn_data)

    return render_template('summary.html',
                           monthly_stat=monthly_stat,
                           tenure_stat=tenure_stat,
                           churn_stat=churn_stat)


@app.route('/churn', methods=['GET'])
def churn_page():
    tenure_churn_data = tenure_churn()
    tenure_churn_bar(tenure_churn_data)

    monthly_charges_churn_data = monthly_charges_churn()
    monthly_charges_churn_bar(monthly_charges_churn_data)

    return render_template('churn.html')


@app.route('/sociodem', methods=['GET'])
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

    return render_template('sociodem.html',
                           age_group_stat=age_group_stat,
                           partner_stat=partner_stat,
                           dependents_stat=dependents_stat)


@app.route('/services', methods=['GET'])
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

    return render_template('services.html',
                           phone_stat=phone_stat,
                           internet_stat=internet_stat,
                           streaming_tv_stat=streaming_tv_stat)


if __name__ == '__main__':
    app.run(debug=True)