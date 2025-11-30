import pandas as pd
import os
from datetime import datetime

# --- Configuration ---
INPUT_FILE = 'data/sample_raw.csv'
OUTPUT_FILE = 'data/shopify_ready.csv'

def clean_data():
    """
    Main ETL function:
    1. Extract: Load raw data
    2. Transform: Clean and format for Shopify
    3. Load: Save to CSV
    """
    print("🚀 Starting ETL Process...")

    # 1. Check if file exists
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    # 2. Load Data
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"✅ Loaded {len(df)} rows from raw data.")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # 3. Data Cleaning (The Magic)
    
    # -> Drop rows where Product Name is missing
    df = df.dropna(subset=['Product Name'])
    
    # -> Clean Price: Remove '$', strip spaces, convert to float
    # Handling potential string issues with regex
    df['Cost Price'] = df['Cost Price'].astype(str).str.replace('$', '', regex=False).str.strip()
    df['Cost Price'] = pd.to_numeric(df['Cost Price'], errors='coerce').fillna(0.0)

    # -> Standardize Date (Convert various formats to YYYY-MM-DD)
    df['DateAdded'] = pd.to_datetime(df['DateAdded'], errors='coerce').dt.strftime('%Y-%m-%d')

    # -> Generate SKU based on ID (e.g., SUP-101)
    df['SKU'] = 'SUP-' + df['SupplierID'].astype(str)

    # 4. Transform to Shopify Format (Renaming Columns)
    shopify_df = pd.DataFrame()
    shopify_df['Handle'] = df['Product Name'].str.lower().str.replace(' ', '-').str.replace(r'[^\w-]', '', regex=True)
    shopify_df['Title'] = df['Product Name'].str.strip()
    shopify_df['Variant SKU'] = df['SKU']
    shopify_df['Variant Price'] = df['Cost Price']
    shopify_df['Inventory Qty'] = df['Stock Level'].fillna(0).astype(int)
    shopify_df['Option1 Name'] = 'Title'
    shopify_df['Option1 Value'] = 'Default Title'

    # 5. Export
    shopify_df.to_csv(OUTPUT_FILE, index=False)
    print(f"✨ Success! Cleaned data saved to {OUTPUT_FILE}")
    print(f"📊 Sample Output:\n{shopify_df.head(3)}")

if __name__ == "__main__":
    clean_data()
