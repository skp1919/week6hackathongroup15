import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict
from typing import List
import datetime

# defining the main app
app = FastAPI(title="Credit Score - Loan Predictor", docs_url="/")

# calling the load_model during startup.
# this will train the model and keep it loaded for prediction.
app.add_event_handler("startup", load_model)

# class which is expected in the payload
class QueryIn(BaseModel):
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


# class which is returned in the response
class QueryOut(BaseModel):
    credit_score_class: str
    timestamp: str

# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    ct = datetime.datetime.now().strftime('%d-%B-%y %H:%M')
    return {"ping": "pong", "timestamp": ct}


@app.post("/predict_credit_score", response_model=QueryOut, status_code=200)
# Route to do the prediction using the ML model defined.
# Payload: QueryIn containing the parameters
# Response: QueryOut containing the credit_score_class predicted (200)
def predict_credit_score(query_data: QueryIn):
    ct = datetime.datetime.now().strftime('%d-%B-%y %H:%M')
    output = {"credit_score_class": predict(query_data), "timestamp": ct}
    return output


# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8887
    uvicorn.run("main:app", host="0.0.0.0", port=8887, reload=True)
