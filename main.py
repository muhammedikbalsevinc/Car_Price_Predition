import streamlit as st
import pandas as pd
import overview
from overview import show_overview
import price_prediction

# Disable the warning for using global figure object
st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data(dataset):
    df = pd.read_csv(dataset)
    df['Fuel_Type'] = df['Fuel_Type'].astype('category')
    return df

def main():
    st.title("Car Price Prediction")
    st.subheader("Welcome to Car Price Prediction App!")

    # Menu
    menu = ["Home", "Overview", "Price Prediction"]
    choices = st.sidebar.selectbox("Select Activity", menu)

    if choices == "Home":
        show_home_page()

    if choices == "Overview":
        show_overview()

    if choices == "Price Prediction":
        price_prediction.price_prediction()

def show_home_page():
    st.subheader("Home Page")

    # Add some key statistics or insights about the car dataset
    data = load_data('app/files/cardata.csv')
    st.write(f"Total number of cars: {len(data)}")
    #st.write(f"Average selling price: ${data['Selling_Price'].mean():.2f}")
    st.write(f"Most common fuel type: {data['Fuel_Type'].value_counts().idxmax()}")
    st.write(f"Most common transmission type: {data['Transmission'].value_counts().idxmax()}")

    # Additional information about fuel types, transmission types, and seller types
    st.subheader("This inforamation will the help user to understand the Prediction")
    st.write("Fuel Types as assigned integers:")
    st.write("- CNG: 0")
    st.write("- Diesel: 1")
    st.write("- Petrol: 2")


    st.write("Transmission Types as assigned integers:")
    st.write("- Automatic: 0")
    st.write("- Manual: 1")
    
    st.write("Seller Types as assigned integers:")
    st.write("- Dealer: 0")
    st.write("- Individual: 1")

if __name__ == '__main__':
    main()
