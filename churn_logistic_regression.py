from data.clean_data import clean_data
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (confusion_matrix, accuracy_score, precision_score,
                             recall_score, f1_score, roc_curve, auc)


def churn_logistic_regression_model():
    data = clean_data()

    columns_to_remove = [col for col in ['LoyaltyID', 'Customer_ID'] if col in data.columns]

    if columns_to_remove:
        data.drop(['LoyaltyID', 'Customer_ID'], axis=1, inplace=True)

    data['Churn'] = data['Churn'].apply(lambda v: 1 if v == 'Yes' else 0)

    data['Total_Charges'] = pd.to_numeric(data['Total_Charges'], errors='coerce')
    data.dropna(inplace=True)

    dummies = pd.get_dummies(
        data[['Senior_Citizen', 'Partner', 'Dependents', 'Phone_Service', 'Multiple_Lines',
              'Internet_Service', 'Online_Security', 'Online_Backup', 'Device_Protection',
              'Tech_Support', 'Streaming_TV', 'Streaming_Movies', 'Contract', 'Paperless_Billing',
              'Payment_Method']],
        drop_first=True)

    final_data = pd.concat([data['Churn'], data['Tenure'],
                            data['Monthly_Charges'], data['Total_Charges'], dummies],
                           axis=1)

    x = final_data.drop('Churn', axis=1)
    y = final_data['Churn']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    logmodel = LogisticRegression(max_iter=500, solver='lbfgs')
    logmodel_fit = logmodel.fit(x_train, y_train)

    y_pred = logmodel.predict(x_test_scaled)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Confusion Matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig('static/graphs/confusion_matrix.png')

    # ROC Curve
    y_prob = logmodel.predict_proba(x_test_scaled)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='#034362', label=f'ROC curve (area = {roc_auc:0.2f})')
    plt.plot([0, 1], [0, 1], color='grey', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.savefig('static/graphs/roc_curve.png')

    html_content = f"""
        <html>
        <head><title>Churn Prediction Logistic Regression Report</title></head>
        <body>
            <h2>Data Processing</h2>
            <p>The following columns were removed: LoyaltyID, Customer_ID</p>
            <p>The following categorical variables were converted to dummy variables: Senior_Citizen, Partner, Dependents, Phone_Service, Multiple_Lines, Internet_Service, Online_Security, Online_Backup, Device_Protection, Tech_Support, Streaming_TV, Streaming_Movies, Contract, Paperless_Billing, Payment_Method</p>

            <h2>Data Splitting</h2>
            <p>The data was split into training and test sets with the following distribution: 70% training set, 30% test set. Random state was set to 42 to ensure reproducibility.</p>

            <h2>Feature Scaling</h2>
            <p>Features were scaled using the StandardScaler method.</p>

            <h2>Logistic Regression Model</h2>
            <p>The logistic regression model was trained using max_iter=500 and solver='lbfgs'.</p>

            <h2>Model Results</h2>
            <p>Model accuracy on the test set: {accuracy:.2f}</p>
            <p>Precision: {precision:.2f}</p>
            <p>Recall: {recall:.2f}</p>
            <p>F1 Score: {f1:.2f}</p>

            <h2>Confusion Matrix and ROC Curve</h2>
            <img src="static/graphs/confusion_matrix.png" alt="Confusion Matrix">
            <img src="static/graphs/roc_curve.png" alt="ROC Curve">
        </body>
        </html>
        """

    with open('templates/churn_logistic_regression.html', 'w') as file:
        file.write(html_content)
