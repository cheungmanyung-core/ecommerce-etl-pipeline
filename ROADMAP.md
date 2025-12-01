# 🗺️ Project Roadmap

This document outlines the development plan and future milestones for the E-Commerce ETL Pipeline.

## 📍 Q1 2026 Priorities: Stability & Flexibility
- [ ] **Encoding Support:** Add auto-detection for various CSV encodings (e.g., `GBK`, `Latin-1`, `UTF-16`) to support global supplier data.
- [ ] **Advanced Logging:** Implement a dedicated `logs/` directory to track detailed error reports and transformation statistics.
- [ ] **Unit Tests:** Add `pytest` coverage for core data cleaning functions (`clean_price`, `generate_sku`).

## 📍 Q2 2026 Priorities: Usability & GUI
- [ ] **Config File:** Move hardcoded paths to a `config.yaml` file for easier user configuration.
- [ ] **Web Interface:** Develop a lightweight frontend using **Streamlit** to allow non-technical users to drag-and-drop files via browser.
- [ ] **Direct Export:** Integrate Google Sheets API to push cleaned data directly to the cloud.

## 🚀 Future Ideas (Backlog)
- AI-powered category mapping using OpenAI API.
- Docker support for easy deployment.
- CI/CD pipeline integration via GitHub Actions.
