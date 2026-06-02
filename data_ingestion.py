from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")

csv_files = list(RAW_PATH.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 100)
    print("FILE:", file.name)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nDtypes:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print("ERROR:", e)