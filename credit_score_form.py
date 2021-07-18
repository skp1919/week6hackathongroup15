from wtforms import StringField, SubmitField, SelectField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class CreditScoreForm(FlaskForm):
    status_checking_account = SelectField(
        'Status of Existing Checking Account',
        choices=[('A11', '< 0 DM'), ('A12', '0 to 200 DM'), ('A13', '>= 200 DM / Salary assignments for at least 1 year'), ('A14', 'No Checking Account')]
    )
    duration = IntegerField('Duration (in months)')
    credit_history = SelectField(
        'Credit History',
        choices=[('A30', 'No credits taken/ All credits paid back duly'), ('A31', 'All credits at this bank paid back duly'), ('A32', 'Existing credits paid back duly till now'), ('A33', 'Delay in paying off in the past'), ('A34', 'Critical account/ Other credits existing not at this bank')]
    )
    purpose = SelectField(
        'Purpose',
        choices=[('A40', 'New Car'), ('A41', 'Used Car'), ('A42', 'furniture/equipment'), ('A43', 'radio/television'),  ('A44', 'domestic appliances'), ('A45', 'repairs'), ('A46', 'education'), ('A47', 'vacation'), ('A48', 'retraining'), ('A49', 'business'), ('A410', 'others')]
    )
    credit_amount = IntegerField('Credit amount')
    savings_account = SelectField(
        'Savings account/Bonds',
        choices=[('A61', '< 100 DM'), ('A62', '100 to 500 DM'), ('A63', '500 to 1000 DM'),  ('A63', '>= 1000 DM'), ('A65', 'Unknown/ No savings account')]
    )
    present_employment_since = SelectField(
        'Present employment since',
        choices=[('A71', 'Unemployed'), ('A72', '< 1 year'), ('A73', '1 to 4 years'), ('A74', '4 to 7 years'), ('A75', '>= 7 years')]
    )
    installment_rate = IntegerField('Installment rate in percentage of disposable income')
    personal_status_sex = SelectField(
        'Personal Status - Sex',
        choices=[('A91', 'Male: Divorced/Separated'), ('A92', 'Female : divorced/separated/married'), ('A93', 'male : single'), ('A94', 'male : married/widowed'), ('A95', 'female : single')]
    )
    other_debtors = SelectField(
        'Other debtors / guarantors',
        choices=[('A101', 'None'), ('A102', 'co-applicant'), ('A103', 'guarantor')]
    )
    present_residence_since = IntegerField('Present residence since')
    property1 = SelectField(
        'Property',
        choices=[('A121', 'real estate'), ('A122', 'if not A121 : building society savings agreement/ life insurance'), ('A123', 'if not A121/A122 : car or other, not in attribute Savings accounts/bonds'), ('A124', 'unknown / no property')]
    )
    age = IntegerField('Age')
    other_installment_plans = SelectField(
        'Other installment plans ',
        choices=[('A141', 'bank'), ('A142', 'stores'), ('A143', 'None')]
    )
    housing = SelectField(
        'Housing',
        choices=[('A151', 'Rent'), ('A152', 'Own'), ('A153', 'For free')]
    )
    existing_credits = IntegerField('Number of existing credits at this bank')
    job = SelectField(
        'Job',
        choices=[('A171', 'unemployed/ unskilled  - non-resident'), ('A172', 'unskilled - resident'), ('A173', 'skilled employee / official'), ('A174', 'management/ self-employed/highly qualified employee/ officer')]
    )
    liable = IntegerField('Number of people being liable to provide maintenance for')
    telephone = SelectField(
        'Telephone',
        choices=[('A191', 'None'), ('A192', 'yes, registered under the customers name')]
    )
    foreign_worker = SelectField(
        'Foreign worker',
        choices=[('A201', 'yes'), ('A202', 'no')]
    )
    submit = SubmitField('Predict')