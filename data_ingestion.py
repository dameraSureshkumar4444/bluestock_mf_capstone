from pathlib import Path
import pandas as pd

raw_dir = Path("data/raw")

for file in raw_dir.glob("*.csv"):

    print("=" * 80)
    print("File:", file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())