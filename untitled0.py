# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:51:36 2021

@author: HP
"""

import streamlit as st
import pickle
import numpy as np
data1=r'C:\Users\HP\Desktop\New folder (3)\8th SEM PRJ\car data.csv'
output=open('data.pkl','wb')
example=pickle.dump(data1,output)
output.close()
example=open('data.pkl','rb')
example_data=pickle.load(example)
print(example_data)
def predict_price(Car_Name,Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner):
    input=np.array([[Car_Name,Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]]).astype(np.float64)
    prediction=example_data.predict(input)
    return float(prediction)


def main():
    st.title("Car Price Prediction")
    html_temp='''
    <div style="background-color:#025246 ; padding:10px">
    <h2 style="color;white ;text-align:center">Car Price Prediction ML App </h2>
    </div>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
    
    Car_Name=st.text_input("What is the name of the old car?","Type Here")
    Year=st.text_input("In which year was the car sold?","Type Here")
    Selling_Price=st.text_input("At what price the car was sold?","In Lakhs")
    Present_Price=st.text_input("What is the present price of the car?","In Lakhs")
    Kms_Driven=st.text_input("How many kilometers the car was drove around before selling?","In kilometers")
    Fuel_Type=st.text_input("What is the type of fuel used in car?","Type the name")
    Seller_Type=st.text_input("What was the type of seller of car?","Type Here")
    Transmission=st.text_input("Was the car manually driven or automatically driven?","Type 1 for manually driven and 0 for automatic")
    Owner=st.text_input("How many people other than the seller were present at the time of selling of car?","Type Here")
    
    
    if st.buttom("Predict"):
        output=predict_price(Car_Name,Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner)
        st.success("The selling price of the vehicle will be {} lakhs".format(round(output,2)))
    
    
    if _name_=='_main_':
        main()

