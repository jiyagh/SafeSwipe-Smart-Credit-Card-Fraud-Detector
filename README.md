# SafeSwipe - Smart Credit Card Fraud Detector 🛡️

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

SafeSwipe is an intelligent AI-powered credit card fraud detection system that helps identify potentially fraudulent transactions in real-time. Built with advanced CNN+LSTM neural networks, it provides accurate fraud predictions with detailed risk assessments.

[![Watch the video](https://raw.githubusercontent.com/jiyagh/SafeSwipe-Smart-Credit-Card-Fraud-Detector/main/thumbnail.png)](https://raw.githubusercontent.com/jiyagh/SafeSwipe-Smart-Credit-Card-Fraud-Detector/main/Safeswipe.mp4)




## 🌟 Features

- **🔍 Real-time Fraud Detection**: Instantly analyze transactions for suspicious patterns
- **🧠 LSTM Neural Network**: Advanced deep learning model for accurate predictions  
- **📊 User-Friendly Interface**: Clean web interface for easy transaction input
- **⚡ Fast Processing**: Quick fraud probability assessment
- **📈 Risk Explanation**: Detailed breakdown of fraud indicators
- **🛡️ High Accuracy**: Trained on comprehensive fraud datasets

## 🚀 What It Does

- ✅ **Predicts** whether a credit card transaction is fraudulent
- 🔍 **Analyzes** transaction patterns using trained LSTM model (`fraud_model.h5`)
- 📊 **Accepts** user-friendly inputs (amount, time, location, merchant type)
- 🧠 **Outputs** fraud probability percentage with detailed risk explanation
- 📱 **Provides** responsive web interface for easy access

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Flask** | Web framework and API server |
| **TensorFlow/Keras** | LSTM neural network implementation |
| **Scikit-learn** | Data preprocessing and scaling |
| **NumPy** | Numerical computations |
| **joblib** | Model serialization |
| **HTML/CSS/JavaScript** | Frontend user interface |

## 📋 Prerequisites

Before running SafeSwipe, ensure you have:

- Python 3.8 or higher installed
- pip package manager
- Git (for cloning the repository)
- At least 4GB RAM (recommended for model loading)

## 💻 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/SafeSwipe-Smart-Credit-Card-Fraud-Detector.git
cd SafeSwipe-Smart-Credit-Card-Fraud-Detector
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install flask tensorflow scikit-learn numpy joblib
```

### Step 4: Verify Model Files
Ensure these files are in your project directory:
- `fraud_model.h5` (LSTM model)
- `scaler.pkl` (Data scaler)

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Access the Web Interface
Open your browser and navigate to:
```
http://localhost:5000
```

## 🎯 Usage

1. **Enter Transaction Details**:
   - Transaction amount
   - Time of transaction
   - Location/region
   - Merchant category

2. **Get Instant Results**:
   - Fraud probability percentage
   - Risk level assessment
   - Detailed explanation of factors

3. **Review Analysis**:
   - Key risk indicators
   - Recommended actions
   - Transaction approval/denial suggestion

## 📁 Project Structure

```
SafeSwipe/
├── app.py                 # Main Flask application
├── fraud_model.h5         # Trained LSTM model
├── scaler.pkl          # Data preprocessing scaler
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Main interface
│   └── result.html       # Results page
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables (Optional)
```bash
export FLASK_ENV=development  # For development mode
export FLASK_DEBUG=1          # Enable debug mode
```

### Model Configuration
The LSTM model expects normalized input features. The preprocessing pipeline handles:
- Amount scaling
- Time encoding
- Location vectorization
- Merchant category encoding

## 📊 Model Performance

- **Accuracy**: ~95%+ on test dataset
- **Precision**: High precision to minimize false positives
- **Recall**: Optimized to catch actual fraud cases
- **F1-Score**: Balanced performance metric


## 🔒 Security Considerations

- Input validation and sanitization
- No sensitive data logging
- Secure model file handling
- Rate limiting recommendations for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

**Jiya Goyal**
- GitHub: [@jiyagh](https://github.com/jiyagh)
- Email: goyal.kira@gmail.com

## 🙏 Acknowledgments

- Credit card fraud datasets used for training
- TensorFlow and Keras communities
- Flask framework contributors
- Financial fraud detection research papers

## 📈 Future Enhancements

- [ ] Real-time transaction monitoring dashboard
- [ ] Integration with banking APIs
- [ ] Mobile application development
- [ ] Advanced ensemble models
- [ ] Explainable AI features
- [ ] Multi-language support

---

⭐ **If you find SafeSwipe useful, please give it a star on GitHub!**

Made with ❤️ and lots of ☕ by [Jiya Goyal](https://github.com/jiyagh)
