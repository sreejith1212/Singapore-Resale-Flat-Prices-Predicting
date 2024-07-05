import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

    
def selling_price_predict(town, flat_type, floor_area_sqm, flat_model, lease_commence_date, sale_year, storey):

    with open("E:/GUVI Main Boot\project singapore flat resale price\Singapore-Resale-Flat-Prices-Predicting\prediction_resale_price_model.pkl", "rb") as file:
        selling_price_prediction_model = pickle.load(file)
    with open("E:\GUVI Main Boot\project singapore flat resale price\Singapore-Resale-Flat-Prices-Predicting\label_encoders.pkl", "rb") as file:
        label_encoder_data = pickle.load(file)
    
    encoded_town = label_encoder_data["town"].transform([town])[0]
    encoded_flat_type = label_encoder_data["flat_type"].transform([flat_type])[0]
    encoded_flat_model = label_encoder_data["flat_model"].transform([flat_model])[0]

    data = np.array([[encoded_town, encoded_flat_type, floor_area_sqm, encoded_flat_model, lease_commence_date, sale_year, storey]])

    input_predict_selling_price = selling_price_prediction_model.predict(data)
    input_predict_selling_price = np.exp(input_predict_selling_price)

    return input_predict_selling_price

if __name__ == "__main__":

    # set app page layout type
    st.set_page_config(layout="wide")

    # create sidebar
    with st.sidebar:        
        page = option_menu(
                            menu_title='Flat Resale Price',
                            options=['Home', 'Predict Selling Price', 'Flat Resale Insights'],
                            icons=['gear', 'map', 'bar-chart-line'], 
                            menu_icon="pin-map-fill",
                            default_index=0 ,
                            styles={"container": {"padding": "5!important"},
                                    "icon": {"color": "brown", "font-size": "23px"}, 
                                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "lightblue", "display": "flex", 
                                                 "align-items": "center"},
                                    "nav-link-selected": {"background-color": "grey"},}  
        )


if page == "Home":

    st.header("Singapore Resale Flat Prices Predicting", divider = "rainbow")
    st.write("")

    st.subheader(":orange[Application Properties :]")
    st.subheader(":one: :grey[_Beneficial for both potential buyers and sellers in the Singapore housing market_.]")
    st.subheader(":two: :grey[_Buyers can use the application to estimate resale prices and make informed decisions, while sellers can get an idea of their flat's potential market value_.]")
            
if page == "Predict Selling Price":

    col1, col2, col3 = st.columns([1,2,1])
    col2.header(':green[Predict Flat Resale Price] 💰')
    container_upload = st.container(height=600, border=False)
    for i in range(3):
        container_upload.write("")
    with container_upload.form(key = "sell"):
        col14, col15, col16 = st.columns(3)
        						
        town = col14. selectbox(label="Preferred Town 🏟️", options=['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                                                                                    'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
                                                                                                    'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                                                                                    'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
                                                                                                    'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
                                                                                                    'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
                                                                                                    'PUNGGOL'])
        flat_type = col15.selectbox(label="Flat Type 💺", options=['1 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE',
                                                                      'MULTI GENERATION', 'MULTI-GENERATION'])
        floor_area_sqm = col14.number_input(label="Floor Area (sqm) 🌐")
        flat_model = col15.selectbox(label="Flat Model 📧", options=['IMPROVED', 'NEW GENERATION', 'MODEL A', 'STANDARD', 'SIMPLIFIED',
                                                                    'MODEL A-MAISONETTE', 'APARTMENT', 'MAISONETTE', 'TERRACE',
                                                                    '2-ROOM', 'IMPROVED-MAISONETTE', 'MULTI GENERATION',
                                                                    'PREMIUM APARTMENT', 'Improved', 'New Generation', 'Model A',
                                                                    'Standard', 'Apartment', 'Simplified', 'Model A-Maisonette',
                                                                    'Maisonette', 'Multi Generation', 'Adjoined flat',
                                                                    'Premium Apartment', 'Terrace', 'Improved-Maisonette',
                                                                    'Premium Maisonette', '2-room', 'Model A2', 'DBSS', 'Type S1',
                                                                    'Type S2', 'Premium Apartment Loft', '3Gen'])
        storey = col14.number_input(label="Storey 🌃", value=0)
        lease_commence_date = col16.selectbox(label="Lease Commence Date 📱", options=tuple(range(1950, 2025)))
        sale_year = col15.selectbox(label="Sale Year 🌆", options=tuple(range(1990, 2025)))
        upload_data = col14.form_submit_button(label="Predict Selling Price", help="Click to Predict Item Selling Price!", type = "primary")
    
    col4, col5, col6 = st.columns(3)
    if upload_data:
        try:
            prediction_1 = selling_price_predict(town, flat_type, np.log(floor_area_sqm), flat_model, lease_commence_date, sale_year, storey)
            col4.success(f"Predicted Resale Price : S$ {round(prediction_1[0])} 💰")
        except:
            col4.error("Enter valid values 🚨")
    
if page == "Flat Resale Insights":

    st.header("Singapore Resale Flat Prices Insights", divider = "rainbow")
    st.write("")

            