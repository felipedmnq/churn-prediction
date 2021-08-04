import joblib
import pandas as pd

class Churn:

    def __init__(self):
        self.pipeline = joblib.load('../models/CBC_model_C3_pipeline.joblib')

    
    def data_cleaning(self, df1):
        df1 = self.drop(columns = ['RowNumber', 'CustomerId', 'Surname', 'Exited'], inplace=True)
        
        return df1


    def feature_eng(self, df1):
        # Balance per age
        df1['BalancePerAge'] = round(df1['Balance'] / df1['Age'], 2)
        df1 = df1.drop(columns = ['RowNumber', 'CustomerId', 'Surname', 'Exited'], inplace=True)

        return df1


    def prediction(self, df1):

        df1['ChurnProbability'] = [round((p * 100), 2) for i, p in self.pipeline.predict_proba(df1).tolist()]

        return df1

