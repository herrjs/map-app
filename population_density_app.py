import streamlit as st
import pandas as pd
pip install folium
import folium

# Sample data (population density by country)
data = pd.DataFrame({
    'Country': ['USA', 'Canada', 'Mexico', 'Brazil', 'India'],
    'Population': [331002651, 38005238, 128932753, 212559417, 1380004385],
    'Area (km²)': [9525067, 9984670, 1964375, 8515767, 3287263]
})

# Calculate population density
data['Population Density (people/km²)'] = data['Population'] / data['Area (km²)']

# Streamlit app
st.title('Population Density Map')

# Dropdown to select a country
selected_country = st.selectbox('Select a country:', data['Country'])

# Filter data for the selected country
selected_data = data[data['Country'] == selected_country]

# Display selected country data
st.write(f'**{selected_country}**')
st.write(f'Population: {selected_data["Population"].values[0]:,}')
st.write(f'Area: {selected_data["Area (km²)"].values[0]:,} km²')
st.write(f'Population Density: {selected_data["Population Density (people/km²)"].values[0]:,.2f} people/km²')

# Create a map using Folium
m = folium.Map(location=[20, 0], zoom_start=2)
folium.Marker([0, 0], tooltip=f'{selected_country}').add_to(m)
st.write(m)
