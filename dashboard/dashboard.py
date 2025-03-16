import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("dashboard/main_data.csv")
print(data.head())
print(data.columns)
