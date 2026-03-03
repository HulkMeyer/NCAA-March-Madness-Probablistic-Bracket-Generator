# 🏀 NCAA March Madness: Probabilistic Simulation Platform
**Graduate Capstone Project | Master of Science in Data Science**

## 📺 Project Walkthrough
[![Watch the Walkthrough]("Web_Application\Bracket\Static\Coverimage.png")]https://youtu.be/iHggG7wIH3A
*Click the image above to view the full system demonstration, including the Flask UI and simulation engine.*

---

## 📝 Executive Summary
This platform is a comprehensive data science solution designed to predict and simulate the NCAA March Madness tournament. Moving beyond binary win/loss predictions, this project utilizes **probabilistic modeling** to account for "Cinderella" variance and team consistency. The system features a modular data pipeline, GPU-accelerated model training, and a Flask-based web deployment.

---

## 🏗️ Technical Architecture

### 🛠️ Data Engineering & Extraction
* **High-Volume Pipeline:** Automated the ingestion and normalization of **200+ raw CSV files** (2012–2025).
* **Feature Engineering:** Developed custom metrics including **Luck Ratings**, **Coach Tournament Performance**, and **NBA Prospect Density**.
* **Database Logic:** Engineered a **SQLite** backend to manage 80+ team features for real-time inference.

### 🧠 Machine Learning Suite
* **Multi-Model Benchmarking:** Built and compared **XGBoost (CUDA-accelerated)**, **Deep Neural Networks (PyTorch)**, and **Random Forest Regressors**.
* **Recursive Simulation Engine:** Developed a custom tournament engine that simulates 68 teams through the "First Four" to the "National Championship," incorporating seed-based consistency multipliers.

### 🌐 Full-Stack Deployment
* **Flask Web App:** Integrated a professional bio, research portfolio, and real-time head-to-head game simulator.
* **Model Explainability:** Utilized **Permutation Importance** to identify the top 18 predictors of tournament success (e.g., `NetRtg`, `Bench_BPR`).

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* NVIDIA GPU (Optional, for CUDA acceleration)

### Installation
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/HulkMeyer/March_Madness_ML_Platform.git](https://github.com/HulkMeyer/March_Madness_ML_Platform.git)
   cd March_Madness_ML_Platform

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the App:**
   ```bash
   python web_app/run.py

4. **Access the UI:**
   Navigate to http://127.0.0.1:5000/

## 📊 Tech Stack

### 💻 Core Languages & Frameworks
* **Python 3.10+: Primary engine for data processing and model inference.**

* **Pandas & NumPy: High-speed data manipulation and matrix operations.**

* **Scikit-Learn: Preprocessing, scaling, and Random Forest modeling.**

* **PyTorch: Deep Neural Network and Linear Activation architectures.**

* **XGBoost: Gradient Boosted Decision Trees for regressive analysis.**

## ⚡ High-Performance Computing
* **CUDA 12.x: Leveraged for GPU-accelerated model training and matrix computations.**

* **CuPy: NumPy-compatible array library for GPU-based calculations.**

## 🌐 Web & Deployment
* **Flask: Backend micro-framework handling UI, routing, and simulation API.**

* **SQLAlchemy: ORM used to interface with the tournament database.**

* **Bootstrap 5: Responsive CSS framework for the front-end dashboard.**

## 🛠️ Development Tools
* **PyCharm: IDE used for modular code construction.**

* **SQLite: Lightweight relational database for team statistics.**

* **GitHub: Version control and project documentation.**

🤝 Connect with Me
Colt Meyer, MSOL, MSDS | Strategic Data Professional | U.S. Army Captain
---
