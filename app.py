import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# ----------- PAGE CONFIG ----------- #
st.set_page_config(page_title="Income Classifier", layout="wide")

# ----------- DARK THEME STYLE ----------- #
st.markdown("""
    <style>
        body {
            color: #fff;
            background-color: #0e1117;
        }
        .css-1v3fvcr, .stMarkdown, .stTextInput, .stSelectbox, .stFileUploader {
            color: #fff !important;
            background-color: #262730 !important;
        }
        .stButton > button {
            color: #fff;
            background-color: #5c5f66;
        }
    </style>
""", unsafe_allow_html=True)

# ----------- TITLE ----------- #
st.markdown("<h1 style='color:#00ADB5;'>💰 Income Classification App</h1>", unsafe_allow_html=True)
st.markdown("Upload your dataset and choose a model to classify income levels.")

# ----------- FILE UPLOAD ----------- #
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("📊 Initial Data")
    st.dataframe(data.head(), use_container_width=True)

    # ----------- DATA CLEANING ----------- #
    with st.expander("🔧 Data Cleaning & Preprocessing"):
        data["workclass"].replace({"?": "other"}, inplace=True)
        data["occupation"].replace({"?": "other"}, inplace=True)
        data = data[~data["workclass"].isin(["Without-pay", "Never-worked"])]
        data = data[(data['age'] >= 17) & (data['age'] <= 75)]
        data = data[(data['educational-num'] >= 5) & (data['educational-num'] <= 16)]

        if "education" in data.columns:
            data.drop(columns=["education"], inplace=True)

        encoder = LabelEncoder()
        categorical_col = ["workclass", 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country']
        for col in categorical_col:
            if col in data.columns:
                data[col] = encoder.fit_transform(data[col].astype(str))

        st.success("✅ Data cleaned and encoded successfully.")

    # ----------- MODEL SELECTION ----------- #
    if "income" not in data.columns:
        st.error("❌ The dataset must contain an 'income' column.")
    else:
        x = data.drop(columns=["income"])
        y = data["income"]
        X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        st.subheader("⚙️ Model Training")

        col1, col2 = st.columns(2)
        with col1:
            model_choice = st.selectbox("Choose a Model", [
                "Logistic Regression", "Random Forest", "KNN", "SVM", "Gradient Boosting"
            ])
        with col2:
            train_button = st.button("🚀 Train Model")

        if train_button:
            if model_choice == "Logistic Regression":
                model = LogisticRegression()
            elif model_choice == "Random Forest":
                model = RandomForestClassifier()
            elif model_choice == "KNN":
                model = KNeighborsClassifier()
            elif model_choice == "SVM":
                model = SVC()
            else:
                model = GradientBoostingClassifier()

            model.fit(X_train, Y_train)
            Y_pred = model.predict(X_test)

            st.success(f"✅ Model trained. Accuracy: {accuracy_score(Y_test, Y_pred):.2f}")
            st.subheader("📋 Classification Report")
            st.code(classification_report(Y_test, Y_pred), language="text")
