import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout='wide')

# Bank icon
image1 = Image.open('pdf_images/bank_icon2.png')
image2 = Image.open('pdf_images/bank_icon.png')

st.image(image1, width=1000)
st.sidebar.image(image2, width=100)

# CSV file upload
upload_help = '''The CSV file must be in the top bank database format'''

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

upload_file = st.sidebar.file_uploader("Choose a CSV file", help=upload_help)

# Infos about top bank database format
with st.sidebar.beta_expander("About Top Bank DB format:"):
    st.markdown(top_bank_db_format)

if upload_file is not None:
  df = pd.read_csv(upload_file).drop(columns=['RowNumber', 'Surname', 'Gender', 'Exited',
                                              'HasCrCard', 'IsActiveMember', 'Age', 'Tenure',
                                              'NumOfProducts'])
  st.write(df)

# Unique infos input