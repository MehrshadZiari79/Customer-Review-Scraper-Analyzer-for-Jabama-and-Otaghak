import pandas as pd
import re

# This script cleans the 'comment' column in the dataset by:
# 1. Dropping rows with NaN values in the 'comment' column.
# 2. Removing comments shorter than 5 characters.
# 3. Removing any rows containing English letters, as the analysis is focused on Persian text only.

# Load the merged CSV file
df = pd.read_csv("merged_comments.csv")

# Remove rows with NaN values in the 'comment' column
df = df.dropna(subset=['comment'])

# Remove comments with fewer than 5 characters
df = df[df['comment'].str.len() >= 5]

# Remove rows with English letters in the 'comment' column
df = df[~df['comment'].str.contains(r'[a-zA-Z]', regex=True)]

# Save the cleaned data to a new CSV file
df.to_csv("cleaned_cms.csv", index=False)

print("Data cleaned and saved ")
