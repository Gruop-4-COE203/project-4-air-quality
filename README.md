# 🌆 Istanbul Air Quality Intelligence Pipeline

### *From Raw Web Data to Tested Visual Insights*

> A complete, end-to-end Python data pipeline designed to transform  
> **raw web data** into **clean, validated, and visual insights** —  
> with a strong focus on **reliability**, **error handling**, and **testing**.

---

## ✨ Project Overview

This project analyzes **air quality data (PM2.5 & PM10)** for **Istanbul** using a modern data pipeline approach.

Rather than focusing only on results, the project emphasizes:
- 🛡️ Defensive programming
- 🧪 Automated testing
- 🧱 Modular design
- 📊 Clear and interactive visualizations


---

## 🚀 Key Features

- 🌐 Real-world data collection from the web  
- 🧹 Data cleaning with validation & safety checks  
- 📈 Exploratory data analysis  
- 🎨 Static & interactive visualizations  
- 🧪 Automated testing with **pytest**  
- 🛡️ Robust error handling using `try/except`

---

## 🧱 Pipeline Architecture

```text
Web Source
    ↓
Data Collection
    ↓
Data Cleaning
    ↓
Data Analysis
    ↓
Visualization
    ↓
Automated Testing (pytest)
```

---

## 📁 Project Structure

```text
project-4-air-quality/
│
├── data/
│   ├── istanbul_air_quality_raw.csv
│   └── istanbul_air_quality_clean.csv
│
├── data_collection.py
├── data_cleaning.py
├── data_analysis.py
├── data_visualization.py
├── web_visualization.py
│
├── test/
│   └── test_data_pipeline.py
└── README.md
```

---

## ⚙️ Installation

Install all required dependencies with:

```bash
pip install -r requirements.txt
```

### Main Libraries Used
- `pandas`
- `numpy`
- `requests`
- `beautifulsoup4`
- `matplotlib`
- `plotly`
- `pytest`

---

## 🔄 Step-by-Step Workflow

### 🌐 1. Data Collection
**File:** `data_collection.py`

- Fetches air quality data from an online source
- Handles network, HTTP, and timeout errors

📤 Output:
```text
istanbul_air_quality_raw.csv
```

---

### 🧹 2. Data Cleaning
**File:** `data_cleaning.py`

- Removes invalid records
- Converts date values safely
- Fills missing pollution values
- Produces a clean dataset ready for analysis

📤 Output:
```text
istanbul_air_quality_clean.csv
```

---

### 📊 3. Data Analysis
**File:** `data_analysis.py`

- Loads cleaned data
- Performs structural checks
- Displays dataset summaries
- Prevents silent data corruption

---

### 🎨 4. Visualization
**Files:**  
- `data_visualization.py`  
- `web_visualization.py`

- Time-series plots of PM2.5 & PM10 levels
- Interactive visualizations with Plotly
- Runtime and dependency validation included

---

## 🧪 Automated Testing

**Framework:** `pytest`

The project includes automated tests to ensure data quality and reliability.

### ✔️ Tests Covered
- Clean dataset existence
- Required column validation
- Datetime conversion correctness
- Non-empty dataset assurance

Run all tests with:

```bash
pytest
```

---

## 🛡️ Error Handling Strategy

This project follows a **two-layer safety model**:

### 🔹 Runtime Protection
Implemented using `try/except` blocks to handle unexpected failures.

### 🔹 Output Validation
Implemented using `pytest` to verify correctness of results.

> Together, they ensure the pipeline is both **safe to run** and **safe to trust**.

---

## 🧑‍🏫 How to Run This Project (Instructor Guide)

### 📌 Prerequisites
- **Python 3.9 or newer**
- **pip** (Python package manager)

Check Python version:
```bash
python --version
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ▶️ Run the Project

1️⃣ (Optional) Collect raw data  
```bash
python data_collection.py
```

2️⃣ Clean and prepare the dataset  
```bash
python data_cleaning.py
```

3️⃣ Run data analysis  
```bash
python data_analysis.py
```

4️⃣ Generate visualizations  
```bash
python data_visualization.py
python web_visualization.py
```

---

### 🧪 Run Tests

```bash
pytest
```

If all tests pass successfully, the data pipeline has been executed correctly.

---

## 🧹 Pylint
Pylint was successfully executed on the project, and the final score obtained is:

**Pylint Score: 9.17 / 10**

All warnings related to **project-owned and modifiable source files** were addressed.

Some remaining warnings originate from files that are **not under our responsibility and cannot be modified**, including:
- Test-related files used solely for validation purposes
- Third-party or dependency-related files
- Framework or externally maintained components

These files are intentionally left unchanged, as modifying them is outside the scope and responsibility of this project.
