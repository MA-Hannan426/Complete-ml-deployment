# 🍷 End-to-End Wine Quality Prediction & ML Deployment Pipeline

An end-to-end machine learning project that builds, evaluates, and deploys a wine-quality prediction model through a modular and configurable ML pipeline.

The project demonstrates a complete machine learning workflow — from data ingestion and schema validation to model training, evaluation, serialization, and serving predictions through a Flask web application.

---

## 🚀 Project Overview

Predicting wine quality is a regression problem where physicochemical properties of wine are used to estimate its quality score.

This project implements a reproducible ML workflow using a modular architecture rather than keeping the entire process inside a single notebook.

The pipeline automatically handles:

* Data ingestion
* Data extraction
* Data validation
* Train/test splitting
* Model training
* Model evaluation
* Model serialization
* Prediction serving through Flask

The trained model can then be accessed through a web interface where users enter wine characteristics and receive a predicted quality score.

---

## 🎯 Objectives

The primary objectives of this project are to:

* Build a complete end-to-end machine learning pipeline.
* Separate data processing, model training, and evaluation into modular components.
* Use configuration files to manage pipeline parameters and paths.
* Validate incoming dataset structure and data types.
* Train a regression model for wine-quality prediction.
* Evaluate model performance using standard regression metrics.
* Serialize the trained model for inference.
* Expose the trained model through a Flask web application.

---

## 🧠 Machine Learning Workflow

```text
                    ┌──────────────────────┐
                    │   Wine Quality Data   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Ingestion     │
                    │ Download + Extract   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Validation    │
                    │ Schema + Data Types  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Transformation  │
                    │ Train/Test Split     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Model Training    │
                    │      ElasticNet      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Model Evaluation   │
                    │ RMSE / MAE / R²      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Saved Model (.joblib)│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Flask Web App      │
                    │     Prediction       │
                    └──────────────────────┘
```

---

## 📊 Dataset

The project uses the **Red Wine Quality dataset**, containing physicochemical measurements of red wine samples and their corresponding quality scores.

### Input Features

| Feature                | Description                  |
| ---------------------- | ---------------------------- |
| `fixed acidity`        | Fixed acidity of the wine    |
| `volatile acidity`     | Volatile acidity             |
| `citric acid`          | Citric acid concentration    |
| `residual sugar`       | Residual sugar concentration |
| `chlorides`            | Chloride concentration       |
| `free sulfur dioxide`  | Free sulfur dioxide level    |
| `total sulfur dioxide` | Total sulfur dioxide level   |
| `density`              | Density of the wine          |
| `pH`                   | Acidity/basicity level       |
| `sulphates`            | Sulphate concentration       |
| `alcohol`              | Alcohol percentage           |

### Target

```text
quality
```

The target represents the wine-quality score.

---

## 🏗️ Project Architecture

The project follows a modular pipeline architecture:

```text
src/
└── mlproject/
    ├── components/
    │   ├── data_ingestion.py
    │   ├── data_validation.py
    │   ├── data_transformation.py
    │   ├── model_trainer.py
    │   └── model_evaluation.py
    │
    ├── config/
    │   └── configuration.py
    │
    ├── constants/
    │
    ├── entity/
    │   └── config_entity.py
    │
    ├── pipeline/
    │   ├── stage_01_data_ingestion.py
    │   ├── stage_02_data_validation.py
    │   ├── stage_03_data_transformation.py
    │   ├── stage_04_model_trainer.py
    │   ├── stage_05_model_evaluation.py
    │   └── prediction.py
    │
    └── utils/
        └── common.py
```

---

## ⚙️ Pipeline Components

### 1. Data Ingestion

The ingestion component:

* Downloads the dataset from the configured source.
* Stores the compressed dataset locally.
* Extracts the dataset into the artifacts directory.
* Avoids downloading the dataset again when it already exists.

---

### 2. Data Validation

The validation stage verifies:

* Expected columns are present.
* Dataset columns conform to the defined schema.
* Feature data types match the expected types.

Validation results are stored in:

```text
artifacts/data_validation/status.txt
```

---

### 3. Data Transformation

The transformation stage prepares the dataset for model training.

The current implementation performs a train/test split and stores:

```text
artifacts/data_transformation/train.csv
artifacts/data_transformation/test.csv
```

The project intentionally keeps transformation modular so additional preprocessing techniques can be introduced later.

---

### 4. Model Training

The project uses an **ElasticNet regression model**.

Current parameters:

```yaml
Elasticnet:
  alpha: 0.2
  l1_ratio: 0.1
```

The trained model is serialized using `joblib` and stored at:

```text
artifacts/model_trainer/model.joblib
```

---

### 5. Model Evaluation

The model is evaluated using:

* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)
* R² Score

Current recorded evaluation:

| Metric |  Score |
| ------ | -----: |
| RMSE   | 0.7550 |
| MAE    | 0.5905 |
| R²     | 0.2579 |

> These metrics represent the currently stored evaluation artifact in the repository.

---

## 🌐 Web Application

The trained model is exposed through a Flask web application.

Users can enter the wine's physicochemical properties through a browser-based form.

The application then:

```text
User Input
    ↓
Flask Request
    ↓
Prediction Pipeline
    ↓
Serialized ElasticNet Model
    ↓
Predicted Wine Quality
```

The application runs on:

```text
http://localhost:8080
```

---

## 🛠️ Technology Stack

### Programming

* Python

### Data Science

* Pandas
* NumPy
* Scikit-learn

### Machine Learning

* ElasticNet Regression
* Train/Test Split
* RMSE
* MAE
* R²

### Deployment

* Flask
* Joblib

### Configuration

* YAML
* Python dataclasses

### Development

* Jupyter Notebook
* Logging
* Modular Python package structure

---

## 📁 Repository Structure

```text
Complete-ml-deployment/
│
├── artifacts/
│   ├── data_ingestion/
│   ├── data_transformation/
│   ├── data_validation/
│   ├── model_evaluation/
│   └── model_trainer/
│
├── config/
│   └── config.yaml
│
├── research/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── Experiment.ipynb
│
├── src/
│   └── mlproject/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
│
├── static/
├── templates/
│
├── app.py
├── main.py
├── params.yaml
├── schema.yaml
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/MA-Hannan426/Complete-ml-deployment.git
cd Complete-ml-deployment
```

### 2. Create a virtual environment

Using Conda:

```bash
conda create -n mlproject python=3.8 -y
conda activate mlproject
```

Or using Python's built-in virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
---


## Workflows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity 
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py

# How to run?
### STEPS:


```bash
conda create -n mlproj python=3.8 -y 
```

```bash
conda activate mlproj
```


```bash
pip install -r requirements.txt
```

```bash
python app.py
```

```bash
Now open up your local host 0.0.0.0:8080
```

