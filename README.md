# 💻 Laptop Price Predictor  

A Machine Learning web app built using **Python, Streamlit, and Scikit-learn**, which predicts the price of a laptop based on its specifications such as brand, processor, RAM, storage, GPU, display, and more.  

---

## 🚀 Features  

✅ Predicts laptop prices based on key hardware specs  
✅ Interactive Streamlit web interface  
✅ Trained using advanced ensemble models (Random Forest, XGBoost, Gradient Boosting, etc.)  
✅ Uses One-Hot Encoding and a full preprocessing pipeline  
✅ Automatically handles categorical & numerical features  

---

## 🧠 Tech Stack  

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3 |
| **Frontend** | Streamlit |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Data Handling** | Pandas, NumPy |
| **Model Saving** | Pickle |
| **Version Control** | Git, GitHub |

---

## 🧩 Model Overview  

The app uses a trained ML pipeline (`pipe.pkl`) that includes:  
- **Preprocessing**: One-Hot Encoding for categorical variables  
- **Models**: A weighted **Voting Regressor** combining RandomForest, GradientBoosting, XGBoost, and ExtraTrees  
- **Evaluation Metrics**: R² Score, Mean Absolute Error (MAE)

---

## ⚙️ Installation & Setup  

Follow these steps to run the project locally 👇  

### 1️⃣ Clone this repository  
```bash
git clone https://github.com/CoderNived/Laptop-Price-Prediction.git
cd Laptop-Price-Prediction
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
3️⃣ Activate the environment
Windows

bash
Copy code
venv\Scripts\activate
macOS/Linux

bash
Copy code
source venv/bin/activate
4️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
5️⃣ Run the Streamlit app
bash
Copy code
streamlit run main.py
Now open the link that appears in your terminal (usually http://localhost:8501).

🧠 How It Works
User selects hardware specifications (brand, CPU, RAM, GPU, etc.)

The app processes input using a trained preprocessing pipeline

The pipeline feeds data to the ML ensemble model

The model predicts log(price), which is then exponentiated to get actual ₹ value

🖼️ Demo Preview

📦 Project Structure
graphql
Copy code
Laptop-Price-Prediction/
│
├── main.py                # Streamlit web app
├── pipe.pkl               # Trained ML model pipeline
├── df.pkl                 # DataFrame used during training
├── requirements.txt       # Project dependencies
├── .gitignore
└── README.md
✨ Future Improvements
Add more laptop datasets for better accuracy

Deploy app to Streamlit Cloud / Render

Add GPU-based models (LightGBM, CatBoost)

Integrate price trend visualization

🧑‍💻 Author
👨‍💻 Nived Shenoy
📍 Electronics & Telecommunication Engineering Student
🚀 Aspiring Machine Learning Engineer | Data Science Enthusiast
🌐 GitHub Profile
