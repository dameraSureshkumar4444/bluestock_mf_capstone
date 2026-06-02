import requests
import pandas as pd
from pathlib import Path

# Create output folder
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

# Scheme codes
schemes = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        # NAV history
        nav_df = pd.DataFrame(data["data"])

        # Add metadata
        nav_df["scheme_code"] = scheme_code
        nav_df["scheme_name"] = scheme_name

        output_file = output_dir / f"{scheme_name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"✓ Saved: {output_file}")

        print(nav_df.head())
        print("-" * 80)

    except Exception as e:
        print(f"✗ Error fetching {scheme_name}: {e}")