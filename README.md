

🌱 Smart Irrigation System
_A machine learning-based crop recommendation and yield prediction system._  

📖 Overview 
Our team developed a machine learning-based crop recommendation system and yield prediction model with a target accuracy of 90%. The system suggests the best crops based on soil properties and climatic conditions. Farmers can access the recommendations through a web-based interface.  

🚀 Features  
✅ Crop Recommendation – Suggests suitable crops based on soil and weather conditions.  
✅ Yield Prediction – Predicts expected yield based on input parameters.  
✅ Machine Learning Models – Uses TensorFlow, Keras, and Random Forest for predictions.  
✅ Web-Based Interface – User-friendly web app for easy access.  
✅ Database Support – Uses **MySQL** for data storage.  

⚙️ Tech Stack
- Frontend: HTML, CSS, JavaScript  
- Backend: Flask (Python)  
- Machine Learning: TensorFlow, Keras, Scikit-Learn  
- Database: MySQL  
- Deployment: Flask/Heroku  

📂 Project Structure  
```
Smart-Irrigation-System/
│── WEBAPP/                # Web Application
│   ├── templates/         # HTML Templates
│   ├── app.py             # Flask Backend
│   ├── classifier.pkl     # ML Model for Crop Recommendation
│   ├── knn_model.pkl      # ML Model for Yield Prediction
│   ├── random_forest_model.pkl # Another ML Model
│── Crop_Recommendation_using_ML.ipynb  # Jupyter Notebook for Model Training
│── crop_yield_prediction.ipynb  # Jupyter Notebook for Yield Prediction Model
│── dataset.csv            # Dataset for training ML models
│── requirements.txt       # Python dependencies
│── README.md              # Project Documentation
```

Installation & Setup  
1️⃣ Clone the Repository
```sh
git clone https://github.com/sneha089/Smart-Irrigation-System.git
cd Smart-Irrigation-System
```
2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
3️⃣ Run the Web App
```sh
python WEBAPP/app.py
```
4️⃣ Open in Browser
Go to: `http://127.0.0.1:5000/`  

Future Improvements  
- 🟢 Add real-time weather API integration  
- 🟢 Improve model accuracy with more datasets  
- 🟢 Develop a mobile-friendly UI  

