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

# Define the total number of records you want to sample
total_samples = 2000

# Group the DataFrame by relevant columns
grouped = df.groupby(['Year', 'LocationAbbr', 'LocationDesc'])

# Check the number of groups and how many records are in each group
print(f"Total groups: {len(grouped)}")
print("Records in each group:")
print(grouped.size())

# Sample a fixed number of records from each group
sampled_df = grouped.apply(lambda x: x.sample(min(len(x), total_samples // len(grouped)), random_state=1)).reset_index(drop=True)

# If the total sampled records exceed 2000, trim it
if len(sampled_df) > total_samples:
    sampled_df = sampled_df.sample(n=total_samples, random_state=1)

# Display the sampled DataFrame
print(sampled_df.head(10))
print(sampled_df.info())

# Save the new sampled DataFrame to a CSV file
# Save the new sampled DataFrame to a CSV file
output_file_path = r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Sampled_Heart_Disease_Data_v2.csv'
sampled_df.to_csv(output_file_path, index=False)

print(f"Sampled dataset saved to {output_file_path}")




import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Rates_and_Trends_in_Heart_Disease.csv')

# Display the first few rows and column info


# Group the DataFrame by relevant columns
grouped = df.groupby(['Year', 'LocationAbbr', 'LocationDesc'])

# Check the number of groups and how many records are in each group
print("Total groups available for sampling:")
print(grouped.size())

# Inspect the contents of the first few groups
for name, group in grouped:
    print(f"Group Name: {name}, Number of Records: {len(group)}")
    if len(group) > 0:
        print(group.head())
    break  # Check only the first group for brevity

# Sample a fixed number of records from each group
desired_samples_per_group = 5  # Sample a reasonable number of records

# Sample from each group
sampled_df = grouped.apply(lambda x: x.sample(n=min(len(x), desired_samples_per_group), random_state=1)).reset_index(drop=True)

# Check if we have enough samples
print(f"Total records after sampling: {len(sampled_df)}")

# If necessary, trim to exactly 2000 records (if there are enough)
if len(sampled_df) > 2000:
    sampled_df = sampled_df.sample(n=2000, random_state=1)

# Display the sampled DataFrame
print(sampled_df.head(10))
print(sampled_df.info())

# Save the new sampled DataFrame to a CSV file
output_file_path = r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Sampled_Heart_Disease_Data_v2.csv'
sampled_df.to_csv(output_file_path, index=False)

#output_file_path = r'C:\Users\YourUsername\Desktop\Sampled_Heart_Disease_Data_v2.csv'

print(f"Sampled dataset saved to {output_file_path}")
# Load the dataset
df = pd.read_csv(r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Rates_and_Trends_in_Heart_Disease.csv')
import numpy as np
import pandas as pd

# Filter for the desired years
years_to_include = [2015, 2016, 2017, 2018, 2019, 2020]
df_filtered = df[df['Year'].isin(years_to_include)]

# Group by Year, LocationAbbr, and LocationDesc
grouped = df_filtered.groupby(['Year', 'LocationAbbr', 'LocationDesc'])

# Check the number of groups and how many records are in each group
print("Total groups available for sampling:")
print(grouped.size())

# Sample a fixed number of records from each group
desired_samples_per_group = 5  # Adjust this if necessary

# Sample from each group with a maximum of `desired_samples_per_group` per group
sampled_df = grouped.apply(lambda x: x.sample(n=min(len(x), desired_samples_per_group), random_state=1)).reset_index(drop=True)

# Check if we have enough samples
print(f"Total records after sampling: {len(sampled_df)}")

# Trim to exactly 2000 records if there are enough
if len(sampled_df) > 2000:
    sampled_df = sampled_df.sample(n=2000, random_state=1)

# Display the sampled DataFrame
print(sampled_df.head(10))
print(sampled_df.info())

# Save the new sampled DataFrame to a CSV file
output_file_path = r'C:\Capstone Project\Module 1\Data-Analytics-Capstone\Sampled_Heart_Disease_Data_v2.csv'
sampled_df.to_csv(output_file_path, index=False)

print(f"Sampled dataset saved to {output_file_path}")