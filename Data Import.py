import numpy as np
import pandas as pd

# Use a raw string for the file path to avoid escape character issues (or double backslashes).
df = pd.read_csv(r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Data\heart.csv')

# Display the first 10 rows of the DataFrame
print(df.head(10))

# Display information about the DataFrame
df.info()

# Display descriptive statistics for the DataFrame
print(df.describe())
print(df.columns)


# Display descriptive statistics for the DataFrame
print(df.describe())
print(df.columns)


