from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the crop recommendation model (KNN)
with open('classifier.pkl', 'rb') as f:
    knn = pickle.load(f)

# Load the crop yield prediction model (Random Forest)
with open('random_forest_model.pkl', 'rb') as file:
    dtr = pickle.load(file)

# Define crop recommendation prediction function
def predict_crop(N, P, k, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, k, temperature, humidity, ph, rainfall]])
    pred = knn.predict(features)[0]
    
    crop_dict = {
        1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut",
        6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon",
        11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil",
        16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
        21: "Chickpea", 22: "Coffee"
    }
    return crop_dict.get(pred, "Sorry, we are not able to recommend a proper crop for this environment")

# Define crop yield prediction function
def predict_yield(Area, Item, Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp):
    features = np.array([[Area, Item, Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp]])
    pred = dtr.predict(features)[0]
    return pred

# Route to the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for crop recommendation for farmers
@app.route('/crop_recommendation', methods=['GET', 'POST'])
def crop_recommendation():
    if request.method == 'POST':
        N = float(request.form['N'])
        P = float(request.form['P'])
        k = float(request.form['k'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        
        result = predict_crop(N, P, k, temperature, humidity, ph, rainfall)
        return render_template('crop_recommendation_result.html', result=result)
    
    return render_template('crop_recommendation.html')

# Route for crop yield prediction for investors
@app.route('/yield_prediction', methods=['GET', 'POST'])
def yield_prediction():
    if request.method == 'POST':
        Area = float(request.form['Area'])
        Item = int(request.form['Item'])
        Year = int(request.form['Year'])
        average_rain_fall_mm_per_year = float(request.form['average_rain_fall_mm_per_year'])
        pesticides_tonnes = float(request.form['pesticides_tonnes'])
        avg_temp = float(request.form['avg_temp'])
        
        result = predict_yield(Area, Item, Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp)
        return render_template('yield_prediction_result.html', result=result)
    
    return render_template('yield_prediction.html')

if __name__ == '__main__':
    app.run(debug=True)
