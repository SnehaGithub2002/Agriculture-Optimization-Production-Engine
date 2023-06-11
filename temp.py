# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Sneha")
import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load

st.title('AGRICULTURE OPTIMIZATION PRODUCTION ENGINE')

st.sidebar.header('User Input Parameters')

def user_report():
    N = st.sidebar.slider('NITROZEN',0,140,1)
    P = st.sidebar.slider('PHOSPHORUS',5,145,1)
    K= st.sidebar.slider('POTASSIUM',5,205,1)
    temperature = st.sidebar.slider("Temperature",9,44,1)
    humidity = st.sidebar.slider('Humidity',14,100,1)
    ph = st.sidebar.slider('PH Value',4,10,1)
    rainfall= st.sidebar.slider('Rainfall',20,299,1)
    
    
    user_report_data = {
             'NITROZEN':N,
            'PHOSPHORUS':P,
            'POTASSIUM':K,
            'TEMPERATURE':temperature,
            'HUMIITY':humidity,
           'PH_VALUE':ph,
           'RAINFALL':rainfall}
    report_data = pd.DataFrame(user_report_data,index = [0])
    return report_data
   
    
    
     
df = user_report()
st.header('User Input parameters')
st.write(df)


# load the model from disk
loaded_model = load(open('C:/Users/SUBHASH/Excelr python/PROJECTS/AGRICULTURE_OPTIMIZATION-main/filename', 'rb'))


#prediction_proba = loaded_model.predict_proba(df)

st.subheader('Predicted Result')
st.button("predict")
   
prediction = loaded_model.predict(df)
st.success("The Suggested Crop for given climatic condition is {}".format(prediction))
st.write(prediction)
