ML-based-Prediction-and-Analysis-of-Agri-Food-CO2-Emission
```
# ML-based-Prediction-and-Analysis-of-Agri-Food-CO2-Emissions

This project uses **Machine Learning** to predict **CO₂ emissions** in the agriculture and food sector.  
The model is deployed with **Streamlit** for an interactive dashboard where users can input values (in kilotonnes) and get predicted emissions.  

---

## 📌 Features  
- 🧠 **Random Forest Model** trained on agricultural emission data  
- 📊 Supports multiple numeric input features (in **kilotonnes, kt**)  
- ⚡ Streamlit-powered web app with clean UI (no +/– clutter)  
- 💾 Model persistence using `joblib`  

---

## 📂 Project Structure  

```

📦 agri-food-emissions
┣ 📜 co2_model.pkl          # Trained Random Forest model
┣ 📜 features.pkl           # Feature names used in training
┣ 📜 dataset.csv            # Source dataset (replace with actual file)
┣ 📜 app.py                 # Streamlit dashboard
┣ 📜 train_model.ipynb      # Jupyter Notebook for training
┣ 📜 README.md              # Project documentation

````

---

## ⚙️ Installation

```
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
joblib
```

---

## 🚀 Usage

### 1️⃣ Train the Model

Open Jupyter Notebook:

```bash
jupyter notebook train_model.ipynb
```

This will:

* Load and clean dataset
* Train a **Random Forest Regressor**
* Save the model as `co2_model.pkl` and feature names as `features.pkl`

---

### 2️⃣ Run Streamlit Dashboard

```bash
streamlit run app.py
```

Then open your browser at **[http://localhost:8501/](http://localhost:8501/)**

---

## 📊 Example Workflow

1. Enter input values for features (e.g., fertilizer use, crop yield, livestock, etc.)
2. Click **Predict CO₂ Emissions**
3. Get predictions in **kilotonnes (kt)**

---

## 📈 Model Details

* **Algorithm**: Random Forest Regressor
* **Input**: Numeric agricultural features (all in **kt**)
* **Output**: Predicted CO₂ emissions (kt)
* **Evaluation**:

  * Mean Squared Error (MSE)
  * R² Score

---

## 🔮 Future Improvements

* Add visualizations (feature importance, trends)
* Build a forecasting model for future predictions based on different parameter.
* Extend dataset for better accuracy

---

## 📜 License

This project is open-source under the **MIT License**.

```
