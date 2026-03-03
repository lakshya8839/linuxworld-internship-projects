# titanic_streamlit_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Page configuration
st.set_page_config(page_title="Titanic Survival Predictor", layout="wide")

st.title("🚢 Titanic Survival Prediction App")
st.markdown("Explore data and predict survival on the Titanic.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("titanic (1).csv")

df = load_data()

# Show data
if st.checkbox("Show Raw Dataset"):
    st.dataframe(df)

# Data info
st.subheader("📊 Dataset Summary")
st.write(df.describe())

# Gender vs Survival
st.subheader("🧍 Gender vs Survival")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x="Sex", hue="Survived", ax=ax1)
st.pyplot(fig1)

# Class vs Survival
st.subheader("🏷️ Passenger Class vs Survival")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x="Pclass", hue="Survived", ax=ax2)
st.pyplot(fig2)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Encode categorical variables
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Feature selection
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = df[features]
y = df['Survived']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Accuracy
st.subheader("✅ Model Accuracy")
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
st.write(f"Accuracy: **{acc:.2f}**")

# Predict from user input
st.subheader("🎯 Predict Your Survival")

col1, col2, col3 = st.columns(3)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.radio("Sex", ['male', 'female'])
with col2:
    age = st.slider("Age", 0, 80, 25)
    sibsp = st.slider("Siblings/Spouses Aboard", 0, 8, 0)
with col3:
    parch = st.slider("Parents/Children Aboard", 0, 6, 0)
    fare = st.number_input("Fare", 0.0, 500.0, 50.0)
    embarked = st.selectbox("Port of Embarkation", ['S', 'C', 'Q'])

# Encoding
sex_val = 0 if sex == 'male' else 1
embarked_val = {'S': 0, 'C': 1, 'Q': 2}[embarked]

input_data = pd.DataFrame([[pclass, sex_val, age, sibsp, parch, fare, embarked_val]], columns=features)

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "Survived" if prediction == 1 else "Did Not Survive"
    st.success(f"Prediction: {result}")
