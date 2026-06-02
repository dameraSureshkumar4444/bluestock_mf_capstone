from pathlib import Path
import pandas as pd

fund_master=pd.read_csv(r'01_fund_master.csv')
fund_master.to_csv('data/raw')