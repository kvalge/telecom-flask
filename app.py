from flask import Flask, render_template
from functions import *
from graphs_generation import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def statistics():
    tenure_stat = tenure_statistics()
    monthly_stat = monthly_charges_statistics()
    tenure_data = tenure()
    charges_data = monthly_charges()
    churn_stat = churn_statistics()
    churn_data = churn()

    tenure_histogram(tenure_data)
    tenure_boxplot(tenure_data)
    monthly_charges_histogram(charges_data)
    monthly_charges_boxplot(charges_data)
    churn_pie(churn_data)

    return render_template('summary.html',
                           monthly_stat=monthly_stat,
                           tenure_stat=tenure_stat,
                           churn_stat=churn_stat)


@app.route('/churn', methods=['GET'])
def churn_page():
    tenure_churn_data = tenure_churn()
    tenure_churn_bar(tenure_churn_data)
    return render_template('churn.html')


@app.route('/sociodem', methods=['GET'])
def sociodem_page():
    return render_template('sociodem.html')


@app.route('/services', methods=['GET'])
def services_page():
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True)
