# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:15:04 2023

@author: busola
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
# Load the dataset, display the ten first lines, store the results in a variable called 'client_0
client_0_bills = pd.read_csv("STEG_BILLING_HISTORY.csv")
# What is the data type of the client_0_bills variable
type(client_0_bills)
# Display the general information of the dataset and try to answer the following questions
# How many rows and columns do we have in this dataset p
# How many categorical features are present in the dataset
# How much memory space does the dataset consume
client_0_bills.info()
# Inspect the dataset for potential missing values
missing_values = client_0_bills.isnull().sum()
# Select your strategy to handle missing values, and tell us why you had made that choice.

# Run a descriptive analysis on numeric features (columns).
# Select the bills records for the client with an id ='train_Client_0', using 2 methods.
# Transform the 'counter_type' feature to a numeric variable using the encoder of your choice.
# Delete the 'counter_statue' feature from the Dataframe