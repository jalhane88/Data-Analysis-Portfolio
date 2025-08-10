
import pandas as pd
import numpy as np

def initial_report(df):
    """
    Generates a comprehensive initial EDA report for a pandas DataFrame.
    """
    print("--- Initial Data Report ---")

    # --- Basic Structure ---
    print("\n--- Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\n--- Data Types & Non-Null Counts ---")
    df.info()

    # --- Data Glimpse ---
    print("\n--- First 5 Rows (Head) ---")
    print(df.head())

    # --- Data Integrity ---
    print("\n--- Missing Values (%) ---")
    missing_values = round(df.isnull().sum() / len(df) * 100, 2)
    print(missing_values[missing_values > 0]) # Only show columns with missing values

    print("\n--- Duplicate Rows ---")
    print(f"Number of duplicate rows: {df.duplicated().sum()}")

    # --- Statistical & Cardinality Summary ---
    print("\n--- Numerical Data Summary ---")
    print(df.describe())

    # Check if there are object columns before trying to describe them
    if df.select_dtypes(include='object').shape[1] > 0:
        print("\n--- Categorical Data Summary ---")
        print(df.describe(include='object'))

    print("\n--- Unique Values Per Column ---")
    print(df.nunique())

    print("\n--- End of Report ---")
