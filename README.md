## Data Immersion & Wrangling Project

### Objective
To acquire, clean, and prepare raw data for analysis.

### Dataset Overview
The dataset was explored to understand column meanings,
data types, and business relevance.

### Data Quality Assessment
- Missing values
- Duplicate records
- Inconsistent formats

### Data Cleaning & Transformation
- Removed duplicates
- Handled missing values
- Standardized formats
- Feature engineering

### Deliverables
- Cleaned dataset
- Data dictionary
- Python cleaning script

### Tools Used
- Python
- Pandas

### How to Run the Project
1. Place raw_data.csv inside the data folder
2. Run the cleaning script:
   python scripts/data_cleaning.py
3. Cleaned data will be saved to data/cleaned_data.csv

### Project Structure
data-wrangling-project
│
├── data
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── scripts
│   └── data_cleaning.py
├── data_dictionary.xlsx
└── README.md