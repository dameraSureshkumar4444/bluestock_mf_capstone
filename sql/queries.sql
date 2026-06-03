-- Query 1: Top 5 Funds by AUM

SELECT
amfi_code,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

---

-- Query 2: Average NAV of All Funds

SELECT
ROUND(AVG(nav),2) AS average_nav
FROM fact_nav;

---

-- Query 3: Monthly Average NAV

SELECT
strftime('%Y-%m', date) AS month,
ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

---

-- Query 4: Transactions by State

SELECT
state,
COUNT(*) AS total_transactions,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

---

-- Query 5: Funds with Expense Ratio Less Than 1%

SELECT
amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

---

-- Query 6: Top 10 Funds by 3-Year Return

SELECT
amfi_code,
return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

---

-- Query 7: Funds with Highest Sharpe Ratio

SELECT
amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

---

-- Query 8: Transaction Count by Type

SELECT
transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

---

-- Query 9: Investor Count by KYC Status

SELECT
kyc_status,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

---

-- Query 10: Compare Fund Return vs Benchmark

SELECT
amfi_code,
return_3yr_pct,
benchmark_3yr_pct,
(return_3yr_pct - benchmark_3yr_pct) AS excess_return
FROM fact_performance
ORDER BY excess_return DESC;
