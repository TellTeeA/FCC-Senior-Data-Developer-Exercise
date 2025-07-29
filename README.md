# FCC Senior Data Developer Technical Exercise

##  Project Overview
A data pipeline and analytics solution built to simulate processing and reporting for a fictional Dice Game app using 2024 user data.

---

##  Data Model
Structured using a **Star Schema**, consisting of:

- `dim_user`
- `dim_plan`
- `dim_payment_method`
- `dim_channel`
- `dim_status`
- `fact_user_play_session`

All output files are stored as CSVs in `/processed_data/`.

---

##  Tools Used
- Python 3.12
- pandas
- VS Code

---

##  Scripts
| Script File                    | Description                              |
|-------------------------------|------------------------------------------|
| `step1_load_and_preview.py`   | Load and preview source data             |
| `step2a_create_dimension_tables.py` | Build all dimension tables         |
| `step2b_create_fact_table.py` | Build and join the fact table            |
| `step3_validate_data.py`      | Run data validation & QA checks          |
| `step4_generate_insights.py`  | Generate business metrics & trends       |

---

##  Business Insights (2024)

- **BROWSER Sessions:** 941  
- **MOBILE Sessions:** 931  
- **Revenue by Type:**
  - ONETIME: $1,124.25
  - ANNUALLY: $659.34
  - MONTHLY: $147.26
- **Total Gross Revenue:** $1,930.85

Projected 2025 Revenue (10% YoY growth): $2,123.94

---

##  Submission
All code and data files have been uploaded to this public repo as required.
