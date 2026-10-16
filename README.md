#  End-to-End Diabetes Risk Prediction System

An end-to-end Machine Learning pipeline and Clinical Decision Support System (CDSS) for diabetes risk prediction, powered by a lightweight SQLite ETL architecture and an optimized Random Forest classifier.

Developed for the **Intelligent Decision Support Systems (AIS431)** course at **Nile University**.

---

##  Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Dataset & ETL Pipeline](#-dataset--etl-pipeline)
- [Machine Learning & Model Evaluation](#-machine-learning--model-evaluation)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Deployment & Usage](#-deployment--usage)
- [Project Team & Acknowledgments](#-project-team--acknowledgments)

---

## 🚀 Project Overview

Early detection of diabetes significantly reduces long-term health complications and clinical management costs. Many small clinics, however, lack large-scale data infrastructure or struggle with fragmented data sources. 

This project addresses this challenge by delivering a lightweight, low-resource decision support pipeline that:
1. Cleans and transforms raw healthcare records into a structured SQLite data warehouse using a **Star Schema** design.
2. Trains and tunes a high-performance **Random Forest Classifier** achieving **95% accuracy**.
3. Deploys an interactive **Streamlit Clinical UI** for real-time patient risk evaluation and probability assessment.

---

## Key Features

- **Automated Data Processing**: Normalizes raw health attributes and builds relational dimension and fact tables.
- **SQL Analytics & EDA**: Enables structured relational queries for clinical trend discovery (e.g., correlation between $HbA1c$ levels and glucose levels).
- **Hyperparameter Optimization**: Model tuned using `GridSearchCV` to maximize precision, recall, and overall robustness.
- **Interactive Clinical Decision Support**: Web-based app providing real-time risk scores based on patient input metrics.

---

## System Architecture

```
┌─────────────────┐     ┌───────────────────┐     ┌───────────────────────┐
│ Raw Patient CSV │ ──> │   Pandas ETL      │ ──> │ SQLite Data Warehouse │
└─────────────────┘     └───────────────────┘     └───────────────────────┘
                                                             │
                                                             ▼
┌─────────────────┐     ┌───────────────────┐     ┌───────────────────────┐
│ Streamlit UI    │ <── │ Random Forest     │ <── │ SQL Query & Model     │
│ Decision Tool   │     │ Classifier (0.95) │     │ Feature Extraction    │
└─────────────────┘     └───────────────────┘     └───────────────────────┘
```

---

##  Dataset & ETL Pipeline

The dataset consists of patient demographic information, lifestyle factors, and physiological measurements.

### Data Warehouse Design (Star Schema)

The SQLite database (`diabetes_dw.sqlite`) organizes records into the following schema:

* **`FACT_DIABETES`**: Stores continuous metabolic values (`bmi`, `hbA1c_level`, `blood_glucose_level`) and the ground-truth target variable (`diabetes`).
* **`DIM_PATIENT`**: Stores patient demographic details (`gender`, `age`).
* **`DIM_HEALTH`**: Stores binary medical history indicators (`hypertension`, `heart_disease`).
* **`DIM_SMOKING`**: Stores encoded smoking classifications (`smoking_history`).

---

## 📈 Machine Learning & Model Evaluation

A **Random Forest Classifier** was trained using physiological markers and clinical histories to predict diabetic status.

### Performance Comparison

| Metric | Baseline Random Forest | Tuned Random Forest (GridSearchCV) |
| :--- | :---: | :---: |
| **Accuracy** | 0.85 | **0.95** |
| **Precision** | 0.83 | **0.96** |
| **Recall** | 0.81 | **0.95** |
| **F1-Score** | 0.82 | **0.95** |

### Top Predictive Features
1. **$HbA1c$ Level**: Key indicator of long-term blood sugar regulation.
2. **Blood Glucose Level**: Immediate physiological glucose reading.
3. **BMI (Body Mass Index)**: Indicator of metabolic risk factors.

---

## 📁 Repository Structure

```text
.
├── data/
│   ├── raw_diabetes_data.csv       # Raw patient input data
│   └── diabetes_dw.sqlite          # Generated SQLite Data Warehouse
├── notebooks/
│   ├── 01_etl_and_schema.ipynb    # Data cleaning & SQLite Star Schema population
│   ├── 02_eda_analysis.ipynb      # SQL queries & data visual explorations
│   └── 03_model_training.ipynb    # Random Forest training & optimization
├── models/
│   └── random_forest_model.pkl    # Serialized trained model
├── app.py                          # Streamlit application main entry point
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## ⚙️ Getting Started

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/diabetes-risk-prediction.git
   cd diabetes-risk-prediction
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Deployment & Usage

Launch the interactive Streamlit application to run model inferences locally:

```bash
streamlit run app.py
```

Once running, navigate to `http://localhost:8501` in your browser, enter patient clinical parameters in the sidebar, and view the real-time diabetes risk report.

---

## 👥 Project Team & Acknowledgments

* **Ahmed Hamdy Mahmoud**
* **Ammar Yasser Sabbah**
* **Salma Essam Mahdy**
* **Sara Aboalyazeed Ibrahim**
* **Yomna Walid Ismail**

**Course Supervisor:** Dr. Shahira Mahmood Heikal  
**Institution:** Nile University — Faculty of Information Technology and Computer Science  
**Course:** Intelligent Decision Support Systems