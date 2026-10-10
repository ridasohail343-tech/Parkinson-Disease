# Parkinson's Disease Prediction Using Machine Learning

## Overview
This project uses Machine Learning to classify voice measurements into Parkinson's and healthy control groups using the Parkinson's dataset.

## Algorithms
- Logistic Regression
- Random Forest Classifier

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle

## Dataset
The dataset contains voice features such as pitch, jitter, shimmer, and other measurements. The `status` column is the target:
- `0`: Healthy control group
- `1`: Parkinson's group

Dataset: [UCI Parkinson's Dataset](https://archive.ics.uci.edu/dataset/174/parkinsons)

## Project Files
- `main.py` — Data preprocessing and model training
- `parkinsons_model.pkl` — Saved Random Forest model
- `scaler.pkl` — Saved feature scaler, if used
- `parkinsons.csv` — Dataset

## How to Run
1. Clone or download this repository.
2. Install dependencies:

   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```

3. Run the project:

   ```bash
   python main.py
   ```

## Disclaimer
This project is for educational purposes only. It is not a medical diagnostic tool and should not be used to diagnose or rule out Parkinson's disease.