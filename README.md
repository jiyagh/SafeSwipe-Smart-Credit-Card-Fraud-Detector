# SafeSwipe-Smart-Credit-Card-Fraud-Detector
SafeSwipe is an AI-based credit card fraud detection system which helps detect fraudulent payments.

---

## 📌 What It Does

- ✅ Predicts whether a transaction is fraudulent
- 🔍 Uses a trained **LSTM model** (`fraud_model.h5`)
- 📊 Accepts user-friendly inputs (amount, time of day, location, merchant)
- 🧠 Outputs fraud probability + risk explanation

---

## 🧠 Tech Used

- **Python 3**
- **Flask** for web server
- **TensorFlow / Keras** for the LSTM model
- **Scikit-learn + joblib** for data scaling
- **NumPy** for array operations
- **HTML/CSS** for frontend

---
## 💻 How to Run Locally

### ✅ Step 1: Clone the Repository
bash
git clone https://github.com/your-username/SafeSwipe.git
cd SafeSwipe

### ✅ Step 2: Create a Virtual Environment
python -m venv venv
source venv/bin/activate     # For macOS/Linux
venv\Scripts\activate        # For Windows


### ✅ Step 3:Install Required Libraries
pip install flask tensorflow scikit-learn numpy joblib


### ✅ Step 4:Run the App:
python app.py


### ✅ Step 5:Go to your browser and open:
http://localhost:5000

---
🙋‍♀️ Author
Made with ❤️ by Jiya Goyal
If you find this useful, drop a ⭐ on the repo!
