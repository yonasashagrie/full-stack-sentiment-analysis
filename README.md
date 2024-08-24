# full-stack-sentiment-analysis
## Overview
This project is a full-stack sentiment analysis system designed to classify text into positive, neutral, or negative sentiment. The project includes data preprocessing, model training, and deployment .

## Project Structure
sentiment-analysis/
│
├── data1.csv                        # Contains raw datasets
│
│
├── new_p.ipynb                   # Jupyter notebooks for experimentation evaluate machine learning models and save
│
├── best_models/                         # Directory to save trained models
│   ├── logistic_regression.pkl  # Serialized logistic regression model
│   ├── svc.py    # Serialized svc  model
│   ├── random_forest.py    # Serialized random_forest model
│   ├── knn.py    # Serialized knn model
│   ├── decision_tree.py    # Serialized decision_tree model
│   └── templates/               # Directory for HTML templates
│       └── index.html           # Main HTML page for user input and displaying results
│
├── full stuck/                      # Directory to save trained models
│    ├── best_model/           # Serialized logistic regression model(selected best performance model)
         └── logistic_regression.pkl       # Serialized logistic regression model
     ├── templates/               # Directory for HTML templates
│       └── index.html           # Main HTML page for user input and displaying results  
     ├── app.py                   # Flask app for serving the sentiment analysis model
     ├── clean_function.app       # Scripts for cleaning and preprocessing the data
     ├──requirements.txt             # List of Python dependencies
     
├── .pred/                       # Virtual environment directory (usually not checked into version control)
│   ├── Scripts/                 # Executables and scripts for the virtual environment
│   └── ...                      # Other virtual environment files


