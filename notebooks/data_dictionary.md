# Data Dictionary

## Table: dim_fund

| Column | Data Type |
|----------|----------|
| amfi_code | BIGINT |
| fund_house | TEXT |
| scheme_name | TEXT |
| category | TEXT |
| sub_category | TEXT |
| plan | TEXT |
| launch_date | TEXT |
| benchmark | TEXT |
| expense_ratio_pct | FLOAT |
| exit_load_pct | FLOAT |
| min_sip_amount | BIGINT |
| min_lumpsum_amount | BIGINT |
| fund_manager | TEXT |
| risk_category | TEXT |
| sebi_category_code | TEXT |
| _merge | TEXT |


## Table: fact_nav

| Column | Data Type |
|----------|----------|
| amfi_code | BIGINT |
| date | TEXT |
| nav | FLOAT |


## Table: fact_transactions

| Column | Data Type |
|----------|----------|
| investor_id | TEXT |
| transaction_date | TEXT |
| amfi_code | BIGINT |
| transaction_type | TEXT |
| amount_inr | BIGINT |
| state | TEXT |
| city | TEXT |
| city_tier | TEXT |
| age_group | TEXT |
| gender | TEXT |
| annual_income_lakh | FLOAT |
| payment_mode | TEXT |
| kyc_status | TEXT |


## Table: fact_performance

| Column | Data Type |
|----------|----------|
| amfi_code | BIGINT |
| scheme_name | TEXT |
| fund_house | TEXT |
| category | TEXT |
| plan | TEXT |
| return_1yr_pct | FLOAT |
| return_3yr_pct | FLOAT |
| return_5yr_pct | FLOAT |
| benchmark_3yr_pct | FLOAT |
| alpha | FLOAT |
| beta | FLOAT |
| sharpe_ratio | FLOAT |
| sortino_ratio | FLOAT |
| std_dev_ann_pct | FLOAT |
| max_drawdown_pct | FLOAT |
| aum_crore | BIGINT |
| expense_ratio_pct | FLOAT |
| morningstar_rating | BIGINT |
| risk_grade | TEXT |


