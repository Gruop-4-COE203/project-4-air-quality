"""PYTEST"""
# pylint: disable=duplicate-code
import os
import pandas as pd

DATA_PATH = "data/istanbul_air_quality_clean.csv"

def test_clean_csv_exists():
    """Ensures that the csv file exists"""
    assert os.path.exists(DATA_PATH), "Clean CSV file does not exist."

def test_required_columns_exist():
    """Ensures that the required columns are present"""
    df = pd.read_csv(DATA_PATH)
    required_columns = ["date", "pm25", "pm10"]
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"

def test_date_is_datetime():
    """Ensures that the date is datetime"""
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    assert df["date"].notna().all(), "Some date values could not be converted to datetime."


def test_dataset_not_empty():
    """Ensures that the dataset is not empty"""
    df = pd.read_csv(DATA_PATH)
    assert len(df) > 0, "Dataset is empty after cleaning."
