# Advanced Process Control Systems Project
📌 Project Overview

The goal of this project is to apply machine learning techniques to the Tennessee Eastman Process (TEP) dataset, a widely recognized simulation benchmark for process control and fault detection in the chemical industry.

By combining unsupervised and supervised learning approaches, this work explores how to uncover hidden patterns, detect faults, and build predictive models for chemical plant operations.

📊 Dataset

Source: Tennessee Eastman Process (TEP) simulation dataset
Features: Time-series measurements of key chemical plant variables (temperature, pressure, flow rates, compositions, etc.)

Applications:

Fault detection
Soft-sensor development
Predictive maintenance

🔬 Methodology
1. Exploratory Data Analysis (EDA)
Data preprocessing (scaling, feature selection, handling categorical variables)
Visualization using PaCMAP and PCA
Time-series analysis of key process variables
2. Unsupervised Learning
PaCMAP: Preserves local and global data structure for visualization
PCA: Dimensionality reduction while retaining maximum variance
HDBSCAN: Density-based clustering for operational states
K-Means: Centroid-based clustering for fault detection
3. Supervised Learning
Random Forest (RF): Robust ensemble method for interpretability
Support Vector Machines (SVM): Fault classification and regression tasks

📈 Expected Outcomes

Identification of stable operational regimes and fault occurrences

Comparative performance analysis of ANN, DNN, RF, and SVM models

Insights into critical fault contributors (e.g., purge rate XMEAS10)
