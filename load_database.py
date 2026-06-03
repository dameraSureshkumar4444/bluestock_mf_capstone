import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///c:\Users\Damerasureshkumar\OneDrive\Desktop\bluestock_mf_capstone\data\db\bluestock_mf.db")

# Load CSV files
dim_fund = pd.read_csv(r"c:\Users\Damerasureshkumar\OneDrive\Desktop\bluestock_mf_capstone\data\processed\merged.csv")

fact_nav = pd.read_csv(r"c:\Users\Damerasureshkumar\OneDrive\Desktop\bluestock_mf_capstone\data\processed\02_nav_history_cleaned.csv")

fact_transactions = pd.read_csv(r"c:\Users\Damerasureshkumar\OneDrive\Desktop\bluestock_mf_capstone\data\processed\transaction_cleaned.csv")

fact_performance = pd.read_csv(r"c:\Users\Damerasureshkumar\OneDrive\Desktop\bluestock_mf_capstone\data\processed\clean_performance.csv")
# Load into SQLite
dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

fact_nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

fact_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)
print("All tables loaded successfully!")
