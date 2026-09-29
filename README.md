# 🚚 Freight Rate Prediction

A machine learning-powered solution for predicting freight rates with **FastAPI**, **Streamlit**, and **Docker** integration.

---

## 📺 Video Explanation

<div align="center">
  <a href="https://www.loom.com" target="_blank">
    <img src="https://brandlogos.net/wp-content/uploads/2023/09/loom-logo_brandlogos.net_vwxqc.png" alt="Loom Logo" width="200">
  </a>
  <p><strong>Watch a comprehensive walkthrough of this project on Loom</strong></p>
  <p><a href="https://www.loom.com" target="_blank">Click here to watch the video explanation</a></p>
</div>

---

## 🎯 Project Overview

This project implements an end-to-end machine learning pipeline for freight rate prediction. It features:

- **Advanced ML Models**: Trained regression models (Random Forest, XGBoost, SVR, Linear Regression)
- **FastAPI Backend**: High-performance REST API for real-time predictions
- **Streamlit Web UI**: Interactive user-friendly interface for freight rate estimation
- **Docker Support**: Complete containerization for seamless deployment
- **Professional Documentation**: Assessment report and model analysis

### Key Capabilities

1. Real-time freight rate predictions
2. Multiple input validation layers
3. Scalable API architecture
4. Interactive web dashboard
5. Docker containerized deployment

---

## 🏗️ Project Structure

```
Freight-Rate-Predictor/
│
├── 📂 app/                          # FastAPI Application
│   ├── main.py                      # Main API entry point
│   └── models.py                    # Pydantic request/response models
│
├── 📂 data/                         # Raw & processed datasets
│   ├── train_test.csv              # Training and testing data
│   ├── validation.csv              # Validation dataset
│   ├── december_chart_inputs.csv   # December predictions input
│   └── validation_predictions_template.csv
│
├── 📂 dataset/                      # Additional dataset files
│
├── 📂 main notebook/                # Jupyter notebooks for model development
│   └── [Model training and analysis]
│
├── 📂 models/                       # Saved ML models
│   └── [Trained model files (.pkl, .joblib)]
│
├── 📂 documents/                    # Documentation
│   ├── Freight_Rate_ML_Assessment.pdf
│   └── Freight_Rate_Prediction_Assessment_Report.odt
│
├── 📂 scorer_results/               # Generated scorer outputs
│   └── candidate_december.png
│
├── 📂 photos/                       # Example screenshots & images
│   ├── home_page.png               # Streamlit home page example
│   └── prediction_result.png       # Prediction result example
│
├── 📄 readme.md                     # This file
├── 📄 dockerfile                    # Docker configuration
├── 📄 requirements.txt              # Python dependencies
├── 📄 streamlit_app.py              # Streamlit web application
├── 📄 score.py                      # Validation and scoring script
└── 📄 validation_predictions.csv    # Prediction output

```

---

## 🎨 Screenshots & Examples

### Home Page - Streamlit Dashboard

The interactive Streamlit interface provides an intuitive way to input shipment details and receive instant predictions.

**Example: Home Page Input Form**
```
[Screenshot showing the Streamlit interface with input fields for:
- Pickup Location
- Delivery Location
- Distance (miles)
- Weight (lb)
- Equipment Type
- Shipment Date
- Prediction Button]
```

The application features:
- Clean, professional UI with gradient styling
- Real-time input validation
- Responsive layout with form and summary side-by-side
- Clear instructions for users

### Prediction Result

Once you submit the form, the system validates your input and returns an estimated freight rate.

**Example: Prediction Result Card**
```
[Screenshot showing:
- Summary card with all submitted details
- Result card displaying: "💰 Estimated Posted Rate: $2,450.75"
- Celebration animation (balloons)]
```

The prediction display includes:
- Input summary review
- Estimated freight rate in currency format
- Clear success indication

---

## 📊 Dataset & Features

The model leverages comprehensive freight load and market information:

| Feature | Description | Type |
|---------|-------------|------|
| `load_id` | Unique identifier for each load | Categorical |
| `pickup` | Pickup location | Categorical |
| `delivery` | Delivery location | Categorical |
| `pickup_lat` | Pickup latitude | Numerical |
| `pickup_lon` | Pickup longitude | Numerical |
| `delivery_lat` | Delivery latitude | Numerical |
| `delivery_lon` | Delivery longitude | Numerical |
| `distance` | Freight distance (miles) | Numerical |
| `equipment` | Equipment type (Dry Van, Reefer, Flatbed) | Categorical |
| `weight` | Load weight (lbs) | Numerical |
| `date` | Load date | Temporal |
| `market_index` | Market-related numerical signal | Numerical |
| `quote_signal` | Quote-related signal | Numerical |
| `posted_rate` | **Target: Freight rate** | Numerical |

---

## 🤖 Modeling Approach

The solution employs multiple regression algorithms:

### Algorithms Evaluated
- **Linear Regression**: Baseline linear model
- **Support Vector Regression (SVR)**: Kernel-based regression
- **Random Forest Regressor**: Ensemble tree-based model
- **XGBoost Regressor**: Gradient boosting model

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score (Coefficient of Determination)

The final model was selected based on validation performance, generalization capability, and suitability for freight rate prediction tasks.

---

## 🔄 Prediction Workflow

```
┌─────────────────────────────────────────────────────────┐
│                  TRAINING PHASE                         │
├─────────────────────────────────────────────────────────┤
│  Training Data → Preprocessing → Feature Engineering   │
│                      ↓                                  │
│            Train Multiple ML Models                     │
│                      ↓                                  │
│      Validate & Compare Model Performance              │
│                      ↓                                  │
│           Select Final Best Model                      │
└─────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────┐
│                  PREDICTION PHASE                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Validation Data  ────────►  Model Prediction  ◄────────────│
│                          ↓                   ▲               │
│                  Predicted Rates ───────────┘               │
│                                                              │
│  December Inputs  ────────►  Model Prediction               │
│                          ↓                                  │
│           Predicted December Rates                          │
│                          ↓                                  │
│              Scorer Validation & Scoring                    │
│                          ↓                                  │
│           Generated December Prediction Chart              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- pip (Python package manager)

### Option 1: Local Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/tyhan-data/Freight-Rate-Predictor.git
cd Freight-Rate-Predictor
```

#### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```

The application will be available at `http://localhost:8501`

#### 5. Run the FastAPI Server (in a separate terminal)
```bash
# Ensure virtual environment is activated
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Option 2: Docker Installation

#### 1. Build the Docker Image
```bash
docker build -t freight-rate-api:latest .
```

#### 2. Run the Docker Container
```bash
docker run -p 8000:8000 freight-rate-api:latest
```

The API will be available at `http://localhost:8000`

#### 3. Access API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

#### 4. Example API Request
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pickup": "Oklahoma City",
    "delivery": "Hartford",
    "distance": 1450,
    "equipment": "Dry Van",
    "weight": 25000,
    "year": 2025,
    "month": 12,
    "day": 15
  }'
```

#### Docker Hub Repository
Pre-built Docker images are available at:
```
https://hub.docker.com/r/tyhan55/freight-rate-api
```

Pull the image:
```bash
docker pull tyhan55/freight-rate-api:latest
docker run -p 8000:8000 tyhan55/freight-rate-api:latest
```

---

## 🌐 Live Deployments

### Streamlit Web Application
**Interactive Freight Rate Prediction UI**
- **URL**: https://freight-rate-predictor.streamlit.app/
- **Features**: User-friendly interface, real-time validation, instant predictions
- **Access**: No installation required, works in any browser

### Docker Container
**FastAPI Backend Service**
- **Repository**: https://hub.docker.com/r/tyhan55/freight-rate-api
- **Image**: `tyhan55/freight-rate-api:latest`
- **Port**: 8000
- **API Documentation**: `/docs` (Swagger), `/redoc` (ReDoc)

---

## 📝 Usage Instructions

### Using the Streamlit Web App

1. **Navigate to** https://freight-rate-predictor.streamlit.app/
2. **Fill in the shipment details**:
   - Pickup Location (e.g., "Oklahoma City")
   - Delivery Location (e.g., "Hartford")
   - Distance in miles (1–10,000)
   - Weight in pounds (1–100,000)
   - Equipment type (Dry Van, Reefer, Flatbed)
   - Shipment date
3. **Click "Predict Freight Rate"**
4. **Review the estimated rate** in the result card

### Input Validation Rules

- **Locations**: 2–50 characters, capitalized (e.g., "New York"), must be different
- **Distance**: 1–10,000 miles
- **Weight**: 1–100,000 lbs
- **Equipment**: Select from available options
- **Date**: Full date with year, month, day

### Using the FastAPI Backend

#### Request Format
```json
POST /predict
{
  "pickup": "string",
  "delivery": "string",
  "distance": 0,
  "equipment": "string",
  "weight": 0,
  "year": 0,
  "month": 0,
  "day": 0
}
```

#### Response Format
```json
{
  "posted_rate": 0.00,
  "status": "success"
}
```

---

## 🔧 Running the Scorer

Validate predictions against the assessment criteria:

```bash
python score.py --predictions validation_predictions.csv --december-predictions data/december_chart_inputs.csv
```

### Output Files
- **Validation Report**: `scorer_results/validation_report.txt`
- **December Chart**: `scorer_results/candidate_december.png`

---

## 📋 Assessment Documentation

### Documents Included

The `documents/` directory contains:

1. **Freight_Rate_ML_Assessment.pdf**
   - Original assessment requirements
   - Dataset specifications
   - Evaluation criteria
   - Deliverables checklist

2. **Freight_Rate_Prediction_Assessment_Report.odt**
   - Comprehensive project report
   - Model performance analysis
   - Data preprocessing approach
   - Validation results
   - December prediction chart
   - Technical methodology

### Key Information Assessed

✅ **Model Accuracy**: Evaluated using MAE, MSE, and R² metrics
✅ **Data Handling**: Comprehensive preprocessing and feature engineering
✅ **Prediction Quality**: Validated against test and validation datasets
✅ **Code Quality**: Clean, well-structured, reproducible code
✅ **Documentation**: Professional README and technical report
✅ **Deployment**: Streamlit UI + FastAPI backend + Docker support

---

## 📂 Output Files

### Prediction Outputs

```
validation_predictions.csv          # Validation set predictions
```

Structure:
```
load_id,predicted_rate
1001,2450.75
1002,3120.50
...
```

### Scorer Results

```
scorer_results/
├── validation_report.txt           # Validation metrics and performance
└── candidate_december.png          # December prediction visualization chart
```

---

## 🔁 Reproducibility

To reproduce the complete solution:

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore the training notebook**
   - Open `main notebook/` folder
   - Run model development and analysis notebooks

3. **Train and validate models**
   - Execute model training steps
   - Generate predictions for validation set

4. **Save predictions**
   - Export predictions as `validation_predictions.csv`
   - Include load_id and predicted_rate columns

5. **Run the scorer**
   ```bash
   python score.py --predictions validation_predictions.csv --december-predictions data/december_chart_inputs.csv
   ```

6. **Verify outputs**
   - Check `validation_predictions.csv`
   - Review `scorer_results/candidate_december.png`
   - Validate metrics in scorer report

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend API** | FastAPI, Uvicorn |
| **Web UI** | Streamlit |
| **ML Framework** | scikit-learn, XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Containerization** | Docker |
| **Server** | Python 3.11 (slim) |
| **API Validation** | Pydantic |

---

## ⚙️ API Endpoints

### Health Check
```
GET /
```
Returns service status.

### Predictions
```
POST /predict
```
Submits freight data and returns estimated rate.

### Interactive Documentation
```
GET /docs              # Swagger UI
GET /redoc             # ReDoc documentation
```

---

## 🤝 Project Information

- **Author**: MAT (Project Creator)
- **Status**: Active & Upgraded (FastAPI + Docker)
- **Last Updated**: 2025
- **Python Version**: 3.8+

### Recent Updates

- ✅ Upgraded with FastAPI backend
- ✅ Added Docker containerization
- ✅ Enhanced Streamlit UI with professional styling
- ✅ Comprehensive README with documentation
- ✅ Multi-deployment options (Local, Docker, Cloud)

---

## 📞 Support & Links

- **Live Demo**: https://freight-rate-predictor.streamlit.app/
- **Docker Hub**: https://hub.docker.com/r/tyhan55/freight-rate-api
- **GitHub Repository**: https://github.com/tyhan-data/Freight-Rate-Predictor
- **Video Explanation**: https://www.loom.com

---

## 📄 License & Attribution

This project implements machine learning techniques for freight rate prediction as per the assessment requirements. All code and documentation are provided as part of the project deliverables.

---

**Built with ❤️ using FastAPI, Streamlit, and Docker**
