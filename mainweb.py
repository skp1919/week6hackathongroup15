from flask import Flask, render_template, redirect, url_for, request
from credit_score_form import CreditScoreForm
import requests
import json
import unicodedata

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

# class which is expected in the payload
class QueryIn():
    status_checking_account: str
    duration: float
    credit_history: str
    purpose: str
    credit_amount: float
    savings_account: str
    present_employment_since: str
    installment_rate: float
    personal_status_sex: str
    other_debtors: str
    present_residence_since: float
    property1: str
    age: float
    other_installment_plans: str
    housing: str
    existing_credits: float
    job: str
    liable: float
    telephone: str
    foreign_worker: str

@app.route('/', methods=['GET', 'POST'])
def home():
    form = CreditScoreForm()
    if form.validate_on_submit():
        result = request.form.to_dict(flat=False)
        print(result)
        payload = {
        "status_checking_account": form.status_checking_account.data,
        "duration": form.duration.data,
        "credit_history": form.credit_history.data,
        "purpose": form.purpose.data,
        "credit_amount": form.credit_amount.data,
        "savings_account": form.savings_account.data,
        "present_employment_since": form.present_employment_since.data,
        "installment_rate": form.installment_rate.data,
        "personal_status_sex": form.personal_status_sex.data,
        "other_debtors": form.other_debtors.data,
        "present_residence_since": form.present_residence_since.data,
        "property1": form.property1.data,
        "age": form.age.data,
        "other_installment_plans": form.other_installment_plans.data,
        "housing": form.housing.data,
        "existing_credits": form.existing_credits.data,
        "job": form.job.data,
        "liable": form.liable.data,
        "telephone": form.telephone.data,
        "foreign_worker": form.foreign_worker.data         
        }
        print("payload", payload )
        info = requests.post('http://localhost:8887/predict_credit_score/', json = payload)
        info = json.loads(info.text)
        print(info)
        return render_template('result.html', info=info)
    return render_template('predict.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)