# 🛒 E-Commerce Data ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📖 Overview
This project is an automated ETL (Extract, Transform, Load) tool designed to solve a common pain point for e-commerce sellers: **converting messy supplier inventory lists into clean, Shopify-import-ready formats.**

Instead of spending hours manually fixing Excel files, this script automates the cleaning process in seconds.

## 🚀 Features
- **Auto-Cleaning:** Removes currency symbols (`$`), trims whitespace, and handles missing values.
- **Smart Formatting:** Standardizes mixed date formats to `YYYY-MM-DD`.
- **Shopify Ready:** Automatically maps columns to Shopify's strict import schema (Handle, SKU, Price, Inventory).
- **Error Handling:** robustly manages bad data rows without crashing.

## 🛠️ Project Structure
```text
├── data/
│   ├── sample_raw.csv       # Messy input file (Supplier format)
│   └── shopify_ready.csv    # Clean output file (Generated)
├── main.py                  # Core ETL logic
└── requirements.txt         # Dependencies

💻 Quick Start
1. Clone the repository
Bash

git clone [https://github.com/natecheung/ecommerce-etl-pipeline.git](https://github.com/natecheung/ecommerce-etl-pipeline.git)
cd ecommerce-etl-pipeline
2. Install dependencies
Bash

pip install -r requirements.txt
3. Run the script
Bash

python main.py
📊 Transformation Logic
The script performs the following transformations:

Price: $15.50 -> 15.50 (Float)

Date: 12-01-2023 / 2023/10/01 -> 2023-10-01

SKU Generation: 101 -> SUP-101
