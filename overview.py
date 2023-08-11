import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Disable the warning for using global figure object
st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data(dataset):
    df = pd.read_csv(dataset)
    df['Fuel_Type'] = df['Fuel_Type'].astype('category')
    return df

def plot_car_name_distribution(data):
    st.subheader('Car Name Distribution Plot')
    car_name_counts = data['Car_Name'].value_counts()
    st.bar_chart(car_name_counts)

def plot_selling_price_by_year(data):
    st.subheader('Selling Price by Year')
    sns.lineplot(x="Year", y="Selling_Price", data=data)
    plt.xlabel('Year')
    plt.ylabel('Selling Price')
    plt.title('Selling Price by Year')
    st.pyplot()

def show_overview():

    data = load_data('app/files/cardata.csv')
    st.subheader("Overview")
    st.dataframe(data.head(15))

    # Plot the frequency of each fuel type
    st.subheader('Frequency of Fuel Types')
    fuel_type_counts = data['Fuel_Type'].value_counts()
    st.bar_chart(fuel_type_counts)

    # Plot the frequency of each transmission type
    st.subheader('Frequency of Transmission Types')
    transmission_counts = data['Transmission'].value_counts(normalize=True)
    st.bar_chart(transmission_counts)

    # Plot the frequency of each seller type
    st.subheader('Frequency of Seller Types')
    seller_type_counts = data['Seller_Type'].value_counts(normalize=True)
    st.bar_chart(seller_type_counts)

    # Add the sns.barplot line for Selling_Price and Year
    st.subheader('Selling Price by Year (Bar Plot)')
    selling_price_by_year = sns.barplot(x='Selling_Price', y='Year', data=data, orient='h')
    plt.xlabel('Selling Price')
    plt.ylabel('Year')
    plt.title('Selling Price by Year')
    st.pyplot(selling_price_by_year.figure)

     # Add the sns.barplot line for Present_Price, Year, and hue by Transmission
    st.subheader('Present Price by Year (Bar Plot)')
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data['Present_Price'], y=data['Year'], data=data, hue=data['Transmission'], orient='h')
    plt.xlabel('Present Price')
    plt.ylabel('Year')
    plt.title('Present Price by Year (Colored by Transmission)')
    st.pyplot()

    # Add the sns.barplot line for Selling_Price, Year, and hue by Transmission
    st.subheader('Selling Price by Year (Colored by Transmission)')
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data['Selling_Price'], y=data['Year'], data=data, hue=data['Transmission'], orient='h')
    plt.xlabel('Selling Price')
    plt.ylabel('Year')
    plt.title('Selling Price by Year (Colored by Transmission)')
    st.pyplot()

    # Plot the distribution of car names
    plot_car_name_distribution(data)

    # Plot the selling price by year
    plot_selling_price_by_year(data)
        
    # Calculate the correlation matrix
    numeric_columns = data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_columns.corr()

    # Plot the correlation heatmap
    st.subheader('Correlation Heatmap')
    sns.heatmap(correlation_matrix, annot=True)
    st.pyplot()


if __name__ == '__main__':
    show_overview()
