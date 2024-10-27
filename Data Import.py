import numpy as np
import pandas as pd

# Use a raw string for the file path to avoid escape character issues (or double backslashes).
df = pd.read_csv(r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Rates_and_Trends_in_Heart_Disease.csv')

# Display the first 10 rows of the DataFrame
print(df.head(10))

# Display information about the DataFrame
df.info()

# Display descriptive statistics for the DataFrame
print(df.describe())
print(df.columns)


# Load the dataset
df = pd.read_csv(r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Rates_and_Trends_in_Heart_Disease.csv')

# Display the first 10 rows of the DataFrame
print(df.head(10))
print(df.head())


# Display information about the DataFrame
df.info()

# Display descriptive statistics for the DataFrame
print(df.describe())
print(df.columns)


# Define the number of records to sample from each group

# Define the number of records to sample from each group
total_samples = 2000

grouped = df.groupby(['Year', 'LocationAbbr', 'LocationDesc'])
# Calculate how many samples to take from each group
samples_per_group = total_samples // len(grouped)

# Sample from each group and combine them into a new DataFrame
sampled_df = grouped.apply(lambda x: x.sample(min(len(x), samples_per_group))).reset_index(drop=True)

# If necessary, trim the sampled DataFrame to exactly 2000 records
if len(sampled_df) > total_samples:
    sampled_df = sampled_df.sample(n=total_samples)

# Display the sampled DataFrame
print(sampled_df.head(10))
print(sampled_df.info())

# Save the new sampled DataFrame to a CSV file
output_file_path = r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Sampled_Heart_Disease_Data.csv'
sampled_df.to_csv(output_file_path, index=False)

print(f"Sampled dataset saved to {output_file_path}")




import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Rates_and_Trends_in_Heart_Disease.csv')

# Display the first 10 rows of the DataFrame
print(df.head(10))

# Display information about the DataFrame
df.info()

# Display descriptive statistics for the DataFrame
print(df.describe())
print(df.columns)

