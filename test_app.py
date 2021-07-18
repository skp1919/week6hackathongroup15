from fastapi.testclient import TestClient
from main import app
import datetime

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        ct = datetime.datetime.now().strftime('%d-%B-%y %H:%M')
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong", "timestamp": ct}


# test to check if Good score is classified correctly
def test_pred_good():
    # defining a sample payload for the testcase
    payload = {
        "status_checking_account": "A11",
        "duration": 6,
        "credit_history": "A34",
        "purpose": "A43",
        "credit_amount": 1169,
        "savings_account": "A65",
        "present_employment_since": "A75",
        "installment_rate": 4,
        "personal_status_sex": "A93",
        "other_debtors": "A101",
        "present_residence_since": 4,
        "property1": "A121",
        "age": 67,
        "other_installment_plans": "A143",
        "housing": "A152",
        "existing_credits": 2,
        "job": "A173",
        "liable": 1,
        "telephone": "A192",
        "foreign_worker": "A201"
    }
    with TestClient(app) as client:
        response = client.post("/predict_credit_score", json=payload)
        ct = datetime.datetime.now().strftime('%d-%B-%y %H:%M')
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"credit_score_class": "Good", "timestamp": ct}
        
# test to check if Bad Score is classified correctly
def test_pred_bad():
    # defining a sample payload for the testcase
    payload = {
        "status_checking_account": "A12",
        "duration": 48,
        "credit_history": "A32",
        "purpose": "A43",
        "credit_amount": 5951,
        "savings_account": "A61",
        "present_employment_since": "A73",
        "installment_rate": 2,
        "personal_status_sex": "A92",
        "other_debtors": "A101",
        "present_residence_since": 2,
        "property1": "A121",
        "age": 22,
        "other_installment_plans": "A143",
        "housing": "A152",
        "existing_credits": 1,
        "job": "A173",
        "liable": 1,
        "telephone": "A191",
        "foreign_worker": "A201"
    }
    with TestClient(app) as client:
        response = client.post("/predict_credit_score", json=payload)
        ct = datetime.datetime.now().strftime('%d-%B-%y %H:%M')
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"credit_score_class": "Bad", "timestamp": ct}