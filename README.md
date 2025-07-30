
# 💰 Income Classification Web App

<div align="center">
  <h3>🚀 AI-Powered Income Prediction for Smart Insights</h3>
  
  [![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0+-red.svg)](https://streamlit.io/)
  [![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2.2+-orange.svg)](https://scikit-learn.org/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **🎯 Multi-Model Classification | 📊 Real-Time Results | 🌐 Beautiful Web UI**
</div>

---

## 🌟 Overview

Welcome to the **Income Classification Web App** – a smart machine learning-powered tool that classifies individual income levels based on demographic and employment data. Users can upload their dataset and instantly see the model's predictions with full performance metrics.

---

## ✨ Features

- 🧠 **Multiple ML Models**: Choose from Logistic Regression, Random Forest, KNN, SVM, and Gradient Boosting
- 📊 **Live Results**: Accuracy score and classification report shown in real-time
- 🔧 **Data Preprocessing**: Built-in handling of missing values and categorical encoding
- 🎨 **Dark-Themed UI**: Stylish and user-friendly interface with custom CSS
- 📂 **CSV Upload**: Upload your own datasets for custom analysis

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/income-classifier.git
cd income-classifier
```

### 2️⃣ Create and Activate Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📂 Project Structure

```
income-classifier/
├── app.py                  # Main Streamlit web app
├── requirements.txt        # Dependencies
├── README.md               # Documentation (this file)
└── sample_dataset.csv      # Example input file (optional)
```

---

## 📋 Requirements

```
pandas
numpy
scikit-learn
streamlit
```

---

## 🛠️ How It Works

### 📂 Upload CSV

- The file must contain a target column named `income`.

### 🔧 Preprocessing Includes:

- Replacing unknown values in `workclass` and `occupation`
- Dropping unnecessary columns
- Label encoding of categorical variables
- Filtering invalid entries (e.g., unreasonable age or education)

### ⚙️ Model Training Options

- Logistic Regression
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine
- Gradient Boosting

### 📈 Output

- Accuracy Score
- Classification Report (Precision, Recall, F1-Score)

---

## 🎥 Demo Preview

> Upload a well-structured dataset and classify income levels within seconds using your preferred machine learning algorithm!

---

## 🐛 Troubleshooting

**Issue**: `ModuleNotFoundError`  
💡 **Solution**: Ensure your virtual environment is activated and run:  
```bash
pip install -r requirements.txt
```

**Issue**: App not launching  
💡 **Solution**: Use a different port  
```bash
streamlit run app.py --server.port 8502
```

---

## 🤝 Contributing

We welcome your ideas!

1. 🍴 Fork the repo
2. 🌿 Create your feature branch
3. 💾 Commit and push
4. 🔄 Open a Pull Request

---

## 📞 Contact

- 📧 Email:pranilg24104@gmail.com



<div align="center">
  
### 🌟 Star this repo if you like it! 🌟  
**Made with ❤️ using Streamlit and Scikit-learn**

</div>
