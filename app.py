# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load models
model = load_model('fraud_model.h5')
scaler = joblib.load('scaler.pkl')

def convert_simple_to_features(data):
    """Convert user-friendly inputs to ML features"""
    # Create mapping logic
    features = np.zeros(30)  # Assuming 30 features total
    
    # Amount (last feature)
    features[-1] = data['amount']
    
    # Time simulation (convert time_of_day to seconds)
    time_mapping = {
        'morning': 28800,    # 8 AM
        'afternoon': 43200,  # 12 PM  
        'evening': 64800,    # 6 PM
        'night': 79200       # 10 PM
    }
    features[0] = time_mapping.get(data['time_of_day'], 43200)
    
    # Risk factors simulation for PCA components
    risk_multiplier = 1.0
    
    if data['location'] == 'international':
        risk_multiplier += 0.5
    if data['merchant'] == 'unknown':
        risk_multiplier += 0.3
    if data['amount'] > 50000:
        risk_multiplier += 0.4
        
    # Simulate PCA components based on risk
    for i in range(1, 29):  # V1 to V28
        features[i] = np.random.normal(0, risk_multiplier)
    
    return features.reshape(1, -1)

@app.route('/')
def home():
    return render_template('index.html')  # Your HTML file

@app.route('/predict_simple', methods=['POST'])
def predict_simple():
    try:
        data = request.json
        features = convert_simple_to_features(data)
        
        # Scale and predict
        features_scaled = scaler.transform(features)
        features_reshaped = features_scaled.reshape(1, -1, 1)
        prediction = model.predict(features_reshaped)[0][0]
        
        return jsonify({
            'probability': float(prediction),
            'is_fraud': bool(prediction > 0.5),
            'risk_factors': analyze_risk_factors(data)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict_advanced', methods=['POST'])
def predict_advanced():
    try:
        data = request.json
        features = np.array([[
            data['adv_time'], data['v1'], data['v2'], data['v3'], 
            data['v4'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, data['adv_amount']
        ]])
        
        features_scaled = scaler.transform(features)
        features_reshaped = features_scaled.reshape(1, -1, 1)
        prediction = model.predict(features_reshaped)[0][0]
        
        return jsonify({
            'probability': float(prediction),
            'is_fraud': bool(prediction > 0.5)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def analyze_risk_factors(data):
    """Analyze what made transaction risky"""
    factors = []
    
    if data['amount'] > 50000:
        factors.append("High transaction amount")
    if data['location'] == 'international':
        factors.append("International transaction") 
    if data['time_of_day'] == 'night':
        factors.append("Unusual time (night)")
    if data['merchant'] == 'unknown':
        factors.append("Unknown merchant type")
        
    return factors

if __name__ == '__main__':
    app.run(debug=True)