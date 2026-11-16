from pathlib import Path
import pandas as pd

def load_hotel_data(csv_path):
    """Load hotel booking records and standardize column labels/date fields."""
    data = pd.read_csv(csv_path)
    data.columns = (data.columns.str.strip().str.lower()
                    .str.replace(" ", "_", regex=False)
                    .str.replace("?", "", regex=False))
    for column in ["booking_date", "check_in_date", "check_out_date", "travel_date"]:
        if column in data.columns:
            data[column] = pd.to_datetime(data[column], errors="coerce")
    if "booking_status" in data.columns:
        data["booking_status"] = data["booking_status"].astype(str).str.strip().str.title()
    if "coupon_used" in data.columns:
        data["coupon_used"] = (data["coupon_used"].astype(str).str.strip().str.lower()
                               .map({"yes": "Yes", "no": "No"}).fillna("Unknown"))
    return data
