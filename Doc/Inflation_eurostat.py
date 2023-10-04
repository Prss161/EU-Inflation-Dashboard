import pandas as pd
import os
import eurostat
import shutil

# Define output and source paths
output_path = "data/sorted_data/"
source_path = "data/unsorted_data/"

# Create directories if they don't exist
for path in [output_path, source_path]:
    if not os.path.exists(path):
        print("Making directory", path)
        os.makedirs(path)

# Define a dictionary for European country codes
landcodes_eu = {
    'AT': 'Austria', 'BE': 'Belgium', 'BG': 'Bulgaria', 'CY': 'Cyprus',
    'CZ': 'Czech Republic', 'DE': 'Germany', 'DK': 'Denmark', 'EE': 'Estonia',
    'ES': 'Spain', 'FI': 'Finland', 'FR': 'France', 'EL': 'Greece',
    'HR': 'Croatia', 'HU': 'Hungary', 'IE': 'Ireland', 'IT': 'Italy',
    'LT': 'Lithuania', 'LU': 'Luxembourg', 'LV': 'Latvia', 'MT': 'Malta',
    'NL': 'Netherlands', 'PL': 'Poland', 'PT': 'Portugal', 'RO': 'Romania',
    'SE': 'Sweden', 'SI': 'Slovenia', 'SK': 'Slovakia', 'EU27_2020': 'European Union'
}

# Define the Eurostat code
code = 'PRC_HICP_MANR'

# Get raw data from Eurostat and save it to a CSV file
df = eurostat.get_data_df(code)
df.to_csv(f'{source_path}{code}.csv')

# Filter data for inflation in the European Union
inflation_eu = df.loc[df['coicop'] == 'CP00']
inflation_eu.drop(columns=['freq', 'unit', 'coicop'], inplace=True)

# Select the desired columns for plotting
data = pd.concat([inflation_eu.iloc[:, 0:1], inflation_eu.iloc[:, -120:]], axis=1)
data.rename(columns={'geo\\TIME_PERIOD': 'Country'}, inplace=True)
data.set_index('Country', inplace=True)

# Filter data for European Union member countries
data = data.loc[landcodes_eu]
data.rename(index=landcodes_eu, inplace=True)

# Save the final data to an XLSX file
data.to_excel(f'{output_path}Inflation_in_EU.xlsx', sheet_name='Inflation_data', index=True)

# Removing unsorted data
shutil.rmtree("data/unsorted_data/")
