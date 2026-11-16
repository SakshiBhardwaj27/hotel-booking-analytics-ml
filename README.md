# Hotel Booking Analytics & Cancellation Prediction

A beginner-friendly portfolio project combining **Python EDA, business KPI analysis, financial-field exploration, and supervised machine learning** to study hotel booking outcomes and cancellation risk.

## Business questions
1. How do booking outcomes vary across channels, cities, room types, and customer/booking segments?
2. What do the dataset's financial fields show, and what can/cannot be concluded about revenue and profitability?
3. Can booking-time attributes help distinguish cancelled bookings from confirmed bookings?

## Dataset
- **Records:** 30,000
- **Columns:** 26
- **Booking statuses:** Confirmed 21,963; Cancelled 5,779; Failed 2,258
- **Cancellation rate:** 19.26% of all records
- **Missing check-in dates:** 5,468 (18.23%)
- **Cancelled records missing check-in date:** 4,712 (81.54% of cancelled records)

The dataset is included in `data/Hotels_Booking_Data.csv`. Treat each row as one booking record; the source does not provide a unique booking ID.

## Repository structure
```text
hotel-booking-analytics-ml/
├── data/
│   ├── Hotels_Booking_Data.csv
│   └── hotel_bookings_cleaned.csv       # created by Notebook 1
├── notebooks/
│   ├── 01_Data_Understanding_and_Cleaning.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   └── 03_Cancellation_Prediction.ipynb
├── reports/
│   ├── Hotel_Booking_Analysis_Report.pdf
│   ├── Original_Analysis_Notebook.ipynb
│   └── Original_Business_Report.pdf
├── visuals/
├── models/
├── src/
│   ├── preprocessing.py
│   └── evaluation.py
├── requirements.txt
└── README.md
```

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook, Joblib, ReportLab.

## Notebook guide
| Notebook | What it covers |
|---|---|
| `01_Data_Understanding_and_Cleaning.ipynb` | Schema, data types, missing values, duplicate checks, date/financial consistency, defensible cleaning |
| `02_Exploratory_Data_Analysis.ipynb` | Booking KPIs, channel/room/city comparisons, recorded financial amounts, coupon/payment behaviour, monthly trends |
| `03_Cancellation_Prediction.ipynb` | Binary target definition, leakage-aware features, preprocessing pipeline, Logistic Regression, Decision Tree, Random Forest, evaluation and feature importance |

## Key data-quality finding
There are 5,468 missing check-in dates. Of 5,779 cancelled records, 4,712 (81.54%) have no check-in date. This means lead-time and stay-duration analyses based on check-in/check-out dates use a selected subset and must not be generalized to all bookings. Missing stay durations are not filled with a median.

## Financial interpretation
The source satisfies `selling_price ≈ costprice + markup` (maximum absolute arithmetic difference: 0.00000000). However, the data dictionary does not define whether these amounts represent quoted, charged, settled, or recognized amounts. The project therefore reports recorded financial fields separately and does **not** label their totals as net revenue or profit. Confirm definitions with the data owner before making accounting claims.

## Machine learning framing
- Target: `Cancelled = 1`, `Confirmed = 0`.
- `Failed` records are excluded because failed and cancelled are different outcomes.
- Excludes identifiers, booking status, refund fields, ambiguous travel/check-in fields, and financial fields with unclear capture timing.
- Uses booking-time fields such as city, star rating, room type, rooms booked, stay type, booking channel, booking value, payment method, channel, cashback, coupon fields, and weekend-check-in flag.
- Uses a stratified train/test split and Scikit-learn pipelines so imputers, scaling, and encoding are fitted on training data only.
- Reports accuracy, precision, recall, F1, ROC-AUC, confusion matrix, and Random Forest feature importance.

A random stratified split is a baseline estimate. For deployment, prefer evaluation on a later time period and verify all inputs are truly available at prediction time.

## Run locally
1. Install Python 3.10 or newer.
2. Download/clone this repository.
3. Open a terminal in the project root.
4. Create and activate a virtual environment (recommended).
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Start Jupyter:
   ```bash
   jupyter notebook
   ```
7. Run notebooks in this order:
   - `notebooks/01_Data_Understanding_and_Cleaning.ipynb`
   - `notebooks/02_Exploratory_Data_Analysis.ipynb`
   - `notebooks/03_Cancellation_Prediction.ipynb`

Run each notebook from top to bottom. Notebook 1 creates `data/hotel_bookings_cleaned.csv`; Notebook 2 and Notebook 3 use it when available.

## Baseline model results

The notebooks were executed in this build. On the stratified held-out test set, the Random Forest had:
- Accuracy: **0.634**
- Precision: **0.340**
- Recall: **0.804**
- F1-score: **0.478**
- ROC-AUC: **0.744**

The model comparison is available in `visuals/model_comparison.csv`. The selected Random Forest has relatively high cancellation recall but low cancellation precision: it catches many cancelled bookings but also flags a substantial number of confirmed bookings. Threshold tuning and cost-based evaluation would be needed before operational use. These are baseline results from a random stratified split, not proof of future or production performance.

## Business recommendations — interpretation, not causal proof
Use segment-level differences as prompts for further investigation. Possible experiments include clearer cancellation reminders, segment-specific customer communication, and controlled tests of coupon or refund-policy changes. Do not assume that changing a channel, coupon, or policy will reduce cancellations without an experiment.

## Limitations
- The source dataset does not include a formal data dictionary or currency definition.
- Missing check-in/check-out dates are strongly associated with cancellation status.
- The meaning of `travel_date` is not documented; it is not used as a model feature.
- `customer_id` and `property_id` are identifiers and are not treated as numeric predictors.
- The dataset is a supplied snapshot; findings may not generalize to other hotels or periods.
- No causal impact or deployed business outcome is claimed.

## Resume-ready project description
**Hotel Booking Analytics & Cancellation Prediction | Python, Pandas, Seaborn, Scikit-learn**
- Analyzed 30,000 hotel booking records to evaluate booking outcomes, cancellation patterns, channel and city performance, and recorded financial metrics.
- Built data-quality checks and business KPIs, documenting missing-date bias and financial-field definition limitations.
- Developed a leakage-aware cancellation classification workflow using Logistic Regression, Decision Tree, and Random Forest with preprocessing pipelines and precision, recall, F1, and ROC-AUC evaluation.

*Update the resume bullets with actual model metrics only after running Notebook 3 and reviewing the saved model comparison.*
