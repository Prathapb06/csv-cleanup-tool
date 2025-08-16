import pandas as pd

# Load CSV
df = pd.read_csv("input.csv")

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values with a default value
df.fillna("N/A", inplace=True)

# Save cleaned CSV
df.to_csv("cleaned_output.csv", index=False)

print("✅ CSV cleaned successfully!")
