# Script created: 22-may-2024

# Author: Leonardo Manzato
# OBS: Script generated with help from google AI (Gemini)

#%% Scenario presentation

# You have an inicial file called "Initial values"
# Someone send you everyday a new file with updated values for products called "New values"
# This script will search for product_id in both files and export a new excel with the old and new value
# also add a new column with the % variation of the cost

#%% Importing libraries

import pandas as pd
import numpy as np

#%% Uploading files

old_values = pd.read_excel("Initial values.xlsx")
new_values = pd.read_excel("New values.xlsx")

#%% Merging columns

new_values_columns = new_values[['product_id','cost']]
combined_values = old_values.merge(new_values_columns, on='product_id', how='left')

#%% Updating values

updated_values = combined_values[['product_id','product_name','supplier','cost_y']]
updated_values = updated_values.rename(columns={'cost_y':'cost'})

#%% Inserting the variation %

variation = (((combined_values['cost_y'] - combined_values['cost_x']) * 100) / combined_values['cost_x'])
variation = np.round(variation, decimals=2)
updated_values.insert(4,'variation (%)', variation)

#%% Export updated table to excel

updated_values.to_excel('Initial values updated.xlsx', index = False)
