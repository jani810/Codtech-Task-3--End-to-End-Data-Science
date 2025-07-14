# Codtech-Task-3--End-to-End-Data-Science
- COMPANY: CODTECH IT SOLUTIONS
- NAME: BHUKYA JANI
- INTERN ID: CT04DH2696
- DOMAIN: DATA SCIENCE
- DURATION: 4 WEEKS
- MENTOR: NEELA SANTOSH
- ## 🔍 Overview
This project demonstrates a complete end-to-end data science workflow using the Iris dataset. A machine learning model is trained to classify iris flower species and is deployed using Flask as a web application.

The goal is to predict the species of a flower — Setosa, Versicolor, or Virginica — based on input measurements like sepal length, sepal width, petal length, and petal width.

---

## ⚙️ Technologies Used
- Python  
- Scikit-learn  
- Flask  
- HTML (Frontend)  
- Pickle (Model Serialization)

---

## 🧠 Workflow

### 1️⃣ Data Preprocessing
- Loaded Iris dataset using Scikit-learn
- Scaled features using `StandardScaler`
- Split the dataset into training and test sets

### 2️⃣ Model Training
- Used `RandomForestClassifier`
- Achieved accuracy of ~96–98% on test data
- Saved the trained model using `pickle` for deployment

### 3️⃣ Model Deployment
- Built a Flask web application (`app.py`)
- Developed an HTML interface (`index.html`) for user input
- On form submission, the app returns the predicted flower species using the trained model

---

## 🌐 Web Interface
- Users enter:  
  🌱 Sepal Length  
  🌱 Sepal Width  
  🌸 Petal Length  
  🌸 Petal Width  
- Output: Predicted Iris species
- Interface runs on `http://127.0.0.1:5000`

---

## 📁 Folder Structure

Task-3-Iris-Deployment/
├── app.py # Flask backend application
├── iris_model.pkl # Trained & serialized ML model
├── templates/
│ └── index.html # HTML input form
└── README.md # Project documentation

yaml
Copy
Edit

---

## ✅ How to Run This Project

1. Download all project files into one folder  
2. Install Flask (if not already):
   ```bash
   pip install flask
In the terminal, run the app:

bash
Copy
Edit
python app.py
Open your browser and visit:
http://127.0.0.1:5000

📌 Conclusion
This project is a complete demonstration of deploying a machine learning model using Flask. It includes data preprocessing, model training, serialization, and web deployment — skills essential for a real-world data scientist or ML engineer.

It was built as part of my 4-week internship at CODTECH IT SOLUTIONS, under the guidance of Mentor Neela Santosh, using the classic Iris dataset.
#OUTPUT
![Image](https://github.com/user-attachments/assets/72d1b2d3-f92d-49b1-9170-e1bcad3e9d05)
