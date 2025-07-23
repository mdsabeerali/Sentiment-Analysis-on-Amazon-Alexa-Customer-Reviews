import os
folders = [
    "Data",
    "Models",
    "templates"
]
files = {
    "Data": ["Predictions.csv", "SentimentBulk.csv", "amazon_alexa.tsv"],
    "Models": ["countVectorizer.pkl", "model_dt.pkl", "model_rf.pkl", "model_xgb.pkl", "scaler.pkl"],
    "templates": ["index.html", "layout.html", "style.css"],
    "": ["Data Exploration & Modelling.ipynb", "README.md", "Sentiment-Analysis.zip", "api.py", "main.py", "requirements.txt", "install_requirements.py"]
}
for folder in folders:
    os.makedirs(folder, exist_ok=True)
for folder, file_list in files.items():
    for file in file_list:
        file_path = os.path.join(folder, file)
        with open(file_path, 'w') as f:
            pass  