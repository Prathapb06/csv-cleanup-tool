# CSV Cleanup Tool

Python script to clean messy CSV files:
- Removes duplicate rows
- Fills missing values
- Saves a cleaned CSV file

## Sample Input (first few rows)

| Name    | Email             | Age |
|---------|-----------------|-----|
| Alice   | alice@example.com | 25  |
| Bob     | bob@example.com   |     |
| Alice   | alice@example.com | 25  |


## How to Use
1. Install dependencies: `pip install pandas`
2. Place your CSV file as `input.csv`
3. Run the script: `python cleanup.py`
4. Output will be saved as `cleaned_output.csv`

## Skills Demonstrated
- Python, Pandas
- Data Cleaning & Automation
- File Handling
