import streamlit as st
import pandas as pd
from PIL import Image
import joblib
import base64
import time

# CSV file upload
upload_help = '''
Input thru a CSV file.

The CSV file must be in the Top Bank database format.

The app will return a table wil the main informations from the
customers with an additional churn probability column and the estimaded revenue.
'''

# dataset format
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

# individual custoemrs prediction
ind_cust_pred = '''
Customer infos are added manually.

The app will return a churn probability for a individual customer with the estimated revenue. 
'''

# set a thrashhold for probabilityes
thrashold_help = '''
Churn probability thrashold
'''

# prediction button
pred_button_help = '''
Click here to run the prediction.
'''

today = time.strftime('%d%m%Y-%H%M%S')
st.set_page_config(layout='wide')

def csv_download_link(data):
    '''create a link to download a filtered csv file'''
    csv = data.to_csv(index=False)
    file_name = f'german_rent_houses_{time}.csv'
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Download CSV file</a>'
    st.markdown(href, unsafe_allow_html=True)

image1 = Image.open('../app_images/bank_icon2.png')

image2 = Image.open('../app_images/bank_icon.png')

# infos and instructions
txt_inst = '''
This APP was buld as part of a learning project. It was made in order to deploy a churn predition model and to train the use of the streamlit framework.

You can find all the information about the project [HERE](https://github.com/felipedmnq/churn-prediction).
'''

st.image(image1, width=1000)

st.sidebar.image(image2, width=100)

# github badge
link = '[![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)]'\
    '(https://github.com/felipedmnq/churn-prediction)'
st.sidebar.write(link, unsafe_allow_html=True)

# Multiple predictions
st.sidebar.markdown('## MUTIPLE CUSTOMERS PREDICTION.')
multi_button = st.sidebar.checkbox(
    'Multiple Prediction', help=upload_help
    )
if multi_button:
    upload_file = st.sidebar.file_uploader(
        "Choose a CSV file"
        )
    threshold = st.sidebar.slider(
        'Thrashold', 50, 100, 75, help=thrashold_help
        )

    if upload_file is not None:
        df = pd.read_csv(upload_file)
        df_f = df
        df = df.drop(columns = ['RowNumber', 'CustomerId', 'Surname', 'Exited'])

        df['BalancePerAge'] = round(df['Balance'] / df['Age'], 2)
        
        model = joblib.load('../models/CBC_model_C3_pipeline.joblib')

        prob = model.predict_proba(df)

        df_f['ChurnProba'] = [round((p * 100), 2) for i, p in prob.tolist()]

        df = df_f.drop(
            columns=[
                    'RowNumber', 'Surname', 'Exited','Gender', 'HasCrCard', 'IsActiveMember', 'Age', 'Tenure', 'NumOfProducts'
                    ]
                )
        
        df = df[df['ChurnProba']>=threshold]
        st.write(f'Customers with {threshold}% or more of CHURN probability: {df.shape[0]}')
        st.write(f'Total Estimated Revenue: U$ {round(df["EstimatedSalary"].sum() * 0.15, 2)}')
        st.write(df)

        # Report Download


        # csv file download
        st.markdown('### :floppy_disk: CSV file Download')
        download_csv = st.button('Export to CSV')
        if download_csv:
            csv_download_link((df))
        

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
    customer_id = st.sidebar.text_input('Customer ID (name or identification number)', 'Customer ID')
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

    pred_button = st.sidebar.button(
        'Churn Prediction', help=pred_button_help
    )

    if pred_button:
        df = pd.DataFrame(df_dict, index = [0])

        df['BalancePerAge'] = round(df['Balance'] / df['Age'], 2)

        model = joblib.load('../models/CBC_model_C3_pipeline.joblib')
        prob = model.predict_proba(df)

        df['ChurnProba'] = [round((p * 100), 2) for i, p in prob.tolist()]

        st.write(f'Customer: {customer_id}')
        st.write(f'Estimated Salary: U$ {df["EstimatedSalary"][0]}')
        st.write(f'Estimated Revenue: U$ {df["EstimatedSalary"][0] * 0.15}')
        st.write(f'This customer has a CHURN probability of {round(prob[0][1] * 100, 2)} %')

        low = Image.open('app_images/gauge1.png')
        medium = Image.open('app_images/gauge2.png')
        high = Image.open('app_images/gauge3.png')
        v_high = Image.open('app_images/gauge4.png')

        if (prob[0][1] * 100) < 40:
            st.image(low, width=500)
        elif 40 <= (prob[0][1] * 100) < 70:
            st.image(medium, width=500)
        elif 70 <= (prob[0][1] * 100) < 85:
            st.image(high, width=500)
        else:
            st.image(v_high, width=500)
  

st.sidebar.markdown('### PROJECT INFOS.')
st.sidebar.markdown(txt_inst)


