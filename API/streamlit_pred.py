import streamlit as st
import pandas as pd
from PIL import Image
import joblib

st.set_page_config(layout='wide')

# Bank icon
image1 = Image.open('pdf_images/bank_icon2.png')
image2 = Image.open('pdf_images/bank_icon.png')

st.image(image1, width=1000)
st.sidebar.image(image2, width=100)

# CSV file upload
upload_help = '''
Input thru a CSV file.

The CSV file must be in the Top Bank database format.

The app will return a table wil the main informations from the
customers with an additional churn probability column and the estimaded revenue.
'''

top_bank_db_format = '''
The Top Bank database columns are:

* RowNumber: the number of the columns
* CustomerID: unique identifier of clients
* Surname: client's last name
* CreditScore: clien'ts credit score for the financial market
* Geography: the country of the client
* Gender: the gender of the client
* Age: the client's age
* Tenure: number of years the client is in the bank 
* Balance: the amount that the client has in their account 
* NumOfProducts: the number of products that the client bought 
* HasCrCard: if the client has a credit card 
* IsActiveMember: if the client is active (within the last 12 months) 
* EstimateSalary: estimative of anual salary of clients 
* Exited: if the client is a churn.
'''

ind_cust_pred = '''
Customer infos are added manually.

The app will return a churn probability for a individual customer with the estimated revenue. 

The app assume that the user knows who the customer is
"Customer ID" and ask only for the needed information for the prediction.
'''

# Multiple predictions
st.sidebar.markdown('## MUTIPLE CUSTOMERS PREDICTION.')
multi_button = st.sidebar.checkbox(
    'Multiple Prediction', help=upload_help
    )
if multi_button:
    upload_file = st.sidebar.file_uploader(
        "Choose a CSV file"
        )

    if upload_file is not None:
        df = pd.read_csv(upload_file).drop(
            columns=[
                    'RowNumber', 'Surname', 'Gender', 'Exited',
                    'HasCrCard', 'IsActiveMember', 'Age', 'Tenure',
                    'NumOfProducts'
                    ]
                )
        st.write(df)

# Infos about top bank database format
with st.sidebar.beta_expander("About Top Bank DB format:"):
    st.markdown(top_bank_db_format)

# Unique infos input
st.sidebar.markdown(
    '## INDIVIDUAL CUSTOMER PREDICTION.'
    )

ind_button = st.sidebar.checkbox(
    'Individual Prediction', help=ind_cust_pred
)

if ind_button:
    df_dict = {}
    # df_dict population
    df_dict['CreditScore'] = st.sidebar.slider(
        'Credit Score', 0, 1000, 500
    )

    df_dict['Geography'] = st.sidebar.radio(
        'Country', 
        [
            'Germany',
            'Spain',
            'France'
        ]
    )

    df_dict['Gender'] = st.sidebar.radio(
        'Gender', 
        [
            'Male',
            'Female'
        ]
    )
    df_dict['Age'] = st.sidebar.slider(
        'Age', 18, 99, 30
        )
    df_dict['Tenure'] = st.sidebar.selectbox(
        'Tenure', 
        [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        ]
    )
    df_dict['Balance'] = st.sidebar.number_input('Balance', 0.0)
    df_dict['NumOfProducts'] = st.sidebar.selectbox(
        'Num Of Products', 
        [
            1, 2, 3, 4
        ]
    )
    df_dict['HasCrCard'] = st.sidebar.selectbox(
        'Has Credit Card (0 - No | 1 - Yes)',
        [
            0,
            1
        ]
    )
    df_dict['IsActiveMember'] = st.sidebar.selectbox(
        'Is Active Member (0 - No | 1 - Yes)',
        [
            0,
            1
        ]
    )
    df_dict['EstimatedSalary'] = st.sidebar.number_input('Estimated Salary', 0.0)

    df = pd.DataFrame(df_dict, index = [0])

    df['BalancePerAge'] = round(df['Balance'] / df['Age'], 2)

    model = joblib.load('../models/CBC_model_C3_pipeline.joblib')
    prob = model.predict_proba(df)

    df['ChurnProba'] = [round((p * 100), 2) for i, p in prob.tolist()]

    st.write(f'Estimated Salary: U$ {df["EstimatedSalary"][0]}')
    st.write(f'Estimated Revenue: U$ {df["EstimatedSalary"][0] * 0.15}')
    st.write(f'This customer has a CHURN probability of {round(prob[0][0] * 100, 2)} %')