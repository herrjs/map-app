pip install streamlit geopandas matplotlib pandas

import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

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

# Load a world map shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge population density data with world map data
merged = world.set_index('name').join(data.set_index('Country'))

# Create a simple choropleth map
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
merged.boundary.plot(ax=ax, linewidth=0.8, color='k')
merged.plot(column='Population Density (people/km²)', cmap='coolwarm', linewidth=0.8, ax=ax, legend=True)
ax.set_title(f'Population Density Map for {selected_country}')
st.pyplot(fig)
