from shiny import App, ui, render
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load data from CSV
data = pd.read_csv("C:/Capstone Project/Module 1/Data-Analytics-Capstone/Shiny App/rsconnect-python/test_predictions_with_best_guess.csv")
print(data.columns)

# Define features and target
features = [
    'Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
    'Sex_M', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA',
    'RestingECG_Normal', 'RestingECG_ST', 'ExerciseAngina_Y',
    'ST_Slope_Flat', 'ST_Slope_Up'
]
X = data[features]
y = data['HeartDisease_Prediction']  # Assuming 'HeartDisease_Prediction' is the target column

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train a model (Logistic Regression)
model = LogisticRegression()
model.fit(X_scaled, y)

# Save the scaler and model columns for later use
scaler_data = scaler
model_columns = features

# Define UI
app_ui = ui.page_fluid(
    ui.input_numeric("age", "Age", value=30),
    ui.input_numeric("restingbp", "Resting Blood Pressure", value=120),
    ui.input_numeric("cholesterol", "Cholesterol", value=200),
    ui.input_numeric("fastingbs", "Fasting Blood Sugar", value=0),
    ui.input_numeric("maxhr", "Maximum Heart Rate Achieved", value=150),
    ui.input_numeric("oldpeak", "Oldpeak", value=1.0),
    ui.input_select("sex", "Sex", choices=["Male", "Female"], selected="Male"),
    ui.input_select(
        "chestpaintype",
        "Chest Pain Type",
        choices=["ATA", "NAP", "TA"],
        selected="ATA"
    ),
    ui.input_select(
        "restingecg",
        "Resting ECG",
        choices=["Normal", "ST", "LVH"],
        selected="Normal"
    ),
    ui.input_select(
        "exerciseangina",
        "Exercise Induced Angina",
        choices=["Yes", "No"],
        selected="No"
    ),
    ui.input_select(
        "st_slope",
        "ST Slope",
        choices=["Flat", "Up", "Down"],
        selected="Flat"
    ),
    ui.input_action_button("submit", "Predict"),
    ui.output_text("prediction")
)

# Define Server logic
def server(input, output, session):
    @output
    @render.text
    def prediction():
        if input.submit():
            # Prepare the input data
            input_data = {
                'Age': input.age(),
                'RestingBP': input.restingbp(),
                'Cholesterol': input.cholesterol(),
                'FastingBS': input.fastingbs(),
                'MaxHR': input.maxhr(),
                'Oldpeak': input.oldpeak(),
                'Sex_M': 1 if input.sex() == "Male" else 0,
                'ChestPainType_ATA': 1 if input.chestpaintype() == "ATA" else 0,
                'ChestPainType_NAP': 1 if input.chestpaintype() == "NAP" else 0,
                'ChestPainType_TA': 1 if input.chestpaintype() == "TA" else 0,
                'RestingECG_Normal': 1 if input.restingecg() == "Normal" else 0,
                'RestingECG_ST': 1 if input.restingecg() == "ST" else 0,
                'ExerciseAngina_Y': 1 if input.exerciseangina() == "Yes" else 0,
                'ST_Slope_Flat': 1 if input.st_slope() == "Flat" else 0,
                'ST_Slope_Up': 1 if input.st_slope() == "Up" else 0
            }

            # Ensure all expected columns are present
            df = pd.DataFrame([input_data])
            df_scaled = scaler_data.transform(df)
            prediction = model.predict(df_scaled)
            return f"Heart Disease Prediction: {'Yes' if prediction[0] == 1 else 'No'}"

app = App(app_ui, server)
