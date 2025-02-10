# **Medical Insurance Premium Prediction**  

## **Project Overview**  
This project builds a **Machine Learning model** to predict **medical insurance premiums** based on factors like age, BMI, smoking status, and region. The dataset is analyzed, visualized, and used to train a regression model.

---

## **Dataset**  
The dataset is loaded from `insurance.csv` and contains the following features:  
- `age`: Age of the individual  
- `sex`: Gender (`male` or `female`)  
- `bmi`: Body Mass Index (BMI)  
- `children`: Number of dependent children  
- `smoker`: Whether the individual smokes (`yes` or `no`)  
- `region`: Residential region (`northeast`, `northwest`, `southeast`, `southwest`)  
- `charges`: Medical insurance premium cost  

---

## **Steps in the Notebook**  

### **1️⃣ Data Preprocessing**  
- **Checking for missing values**:
  ```python
  print(data.isnull().sum())
  ```
- **Basic statistics**:
  ```python
  data.describe().T
  ```

### **2️⃣ Data Visualization**  
- **Histograms for Age, BMI, and Children count**:
  ```python
  sns.histplot(data['age'])
  sns.histplot(data['bmi'])
  sns.histplot(data['children'])
  ```
- **Categorical count plots** for `sex`, `smoker`, and `region`:
  ```python
  sns.countplot(x=data['smoker'], hue=data['sex'])
  ```

### **3️⃣ Machine Learning Model**  
- **Splitting data into training and testing sets**:
  ```python
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```
- **Training a Random Forest Regressor**:
  ```python
  from sklearn.ensemble import RandomForestRegressor
  model = RandomForestRegressor(n_estimators=100, random_state=42)
  model.fit(X_train, y_train)
  ```
- **Making Predictions**:
  ```python
  predictions = model.predict(X_test)
  ```

---

## **Results & Insights**  
- The dataset has no missing values.  
- Smoking significantly impacts insurance charges.  
- The trained model predicts premiums based on user inputs with reasonable accuracy.

---

## **Next Steps**  
✅ Hyperparameter tuning for better accuracy  
✅ Deploying the model using **Streamlit**  
✅ Comparing with other regression models   🚀
