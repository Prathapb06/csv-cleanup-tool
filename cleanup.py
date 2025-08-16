import pandas as pd

# Load CSV
df = pd.read_csv("input.csv")

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values for string/object columns with "N/A"
for col in df.select_dtypes(include="object"):
    df[col] = df[col].fillna("N/A")

# Fill missing values for numeric columns with a placeholder (optional)
for col in df.select_dtypes(include="number"):
    df[col] = df[col].fillna(-1)

# Save cleaned CSV
df.to_csv("cleaned_output.csv", index=False)

print("✅ CSV cleaned successfully!")
