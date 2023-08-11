import streamlit as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image
import pickle

@st.cache(allow_output_mutation=True)
def load_model():
    model = pickle.load(open('app/files/model_lr.sav', 'rb'))
    return model

st.title('Car Price Prediction')
st.sidebar.header('Car Data')
# Additional information about fuel types, transmission types, and seller types
st.subheader("Information For User:")
st.write("Fuel Types:")
st.write("- CNG: 0")
st.write("- Diesel: 1")
st.write("- Petrol: 2")

st.write("Transmission Types:")
st.write("- Manual: 1")
st.write("- Automatic: 0")

st.write("Seller Types:")
st.write("- Dealer: 0")
st.write("- Individual: 1")


def user_report():
    present_price_range = st.sidebar.slider('Present_Price(Euro)', 320, 92600, 1)
    fuel_type = st.sidebar.slider('Fuel Type', 0, 2, 0)
    seller_type = st.sidebar.slider('Seller Type', 0, 1, 0)
    transmission = st.sidebar.slider('Transmission', 0, 1, 0)

    user_report_data = {
        'Present_Price(Euro)': present_price_range,
        'Fuel_Type': fuel_type,
        'Seller_Type': seller_type,
        'Transmission': transmission,
    }

    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

def price_prediction():
    model = load_model()  # Load the model using the cached function
    user_data = user_report()
    predicted_selling_price = model.predict(user_data)
    
    # Display the image conditionally
    if st.sidebar.button('Predict'):
        image = Image.open('app/files/car_image.jpg')
        st.image(image, 'SP')

    st.subheader('Estimated Selling Price (Euro)')
    st.subheader('$' + str(np.round(predicted_selling_price[0], 2)))
    


if __name__ == '__main__':
    price_prediction()
