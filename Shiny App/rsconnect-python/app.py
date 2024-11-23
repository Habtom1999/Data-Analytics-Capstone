from shiny import App, ui, reactive
import joblib
import pandas as pd
import joblib
import os
from shiny import App, ui



# Replace with the absolute paths to your model and scaler
model_path = "C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\heart_disease_model.pkl"
scaler_path = "C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\scaler.pkl"


# Load pre-trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Features for the model
feature_names = [
    "Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak",
    "Sex_M", "ChestPainType_AT", "ChestPainType_NAP", "ChestPainType_TA", "ChestPainType_Asy",
    "RestingECG_Normal", "RestingECG_ST", "RestingECG_LVH",
    "ExerciseAngina_Y", "ExerciseAngina_N",
    "ST_Slope_Down", "ST_Slope_Flat", "ST_Slope_Up"
]

# Define the app UI
app_ui = ui.page_fluid(
    ui.h2("Heart Disease Test"),
    ui.row(
        ui.column(4, ui.input_numeric("Age", "Age:", 20)),
        ui.column(4, ui.input_select("Sex", "Sex:", {"M": "Male", "F": "Female"})),  # Dictionary for "Sex"
    ),
    ui.row(
        ui.column(4, ui.input_numeric("RestingBP", "Resting Blood Pressure (mm Hg):", 110)),
        ui.column(4, ui.input_numeric("Cholesterol", "Serum Cholesterol (mg/dL):", 230)),
    ),
    ui.row(
        ui.column(4, ui.input_select("FastingBS", "Fasting Blood Sugar > 120 mg/dL:", {1: "True", 0: "False"})),  # Dictionary for "FastingBS"
        ui.column(4, ui.input_numeric("MaxHR", "Maximum Heart Rate:", 140)),
    ),
    ui.row(
        ui.column(4, ui.input_numeric("Oldpeak", "ST Depression Induced:", 2.2)),
        ui.column(4, ui.input_select("ExerciseAngina", "Exercise-Induced Angina:", {"Y": "Yes", "N": "No"})),  # Dictionary for "ExerciseAngina"
    ),
    ui.row(
        ui.column(4, ui.input_select("ChestPainType", "Chest Pain Type:", {  # Dictionary for "ChestPainType"
            "AT": "Atypical Angina", 
            "NAP": "Non-Anginal Pain", 
            "TA": "Typical Angina", 
            "Asy": "Asymptomatic"})),
        ui.column(4, ui.input_select("RestingECG", "Resting ECG Results:", {  # Dictionary for "RestingECG"
            "Normal": "Normal", 
            "ST": "ST-T Wave Abnormality", 
            "LVH": "Left Ventricular Hypertrophy"})),
    ),
    ui.row(
        ui.column(4, ui.input_select("St_slope", "Slope of ST Segment:", {  # Dictionary for "St_slope"
            "Flat": "Flat", 
            "Up": "Upward", 
            "Down": "Downward"})),
    ),
    ui.input_action_button("predict", "Predict"),
    ui.output_text("prediction_result")
)

# Define the server logic
def server(input, output, session):
    @reactive.event(input.predict)
    def make_prediction():
        # Map input values to model features
        user_data = {
            "Age": input.Age(),
            "RestingBP": input.RestingBP(),
            "Cholesterol": input.Cholesterol(),
            "FastingBS": int(input.FastingBS()),
            "MaxHR": input.MaxHR(),
            "Oldpeak": input.Oldpeak(),
            "Sex_M": 1 if input.Sex() == "M" else 0,
            "ChestPainType_AT": 1 if input.ChestPainType() == "AT" else 0,
            "ChestPainType_NAP": 1 if input.ChestPainType() == "NAP" else 0,
            "ChestPainType_TA": 1 if input.ChestPainType() == "TA" else 0,
            "ChestPainType_Asy": 1 if input.ChestPainType() == "Asy" else 0,
            "RestingECG_Normal": 1 if input.RestingECG() == "Normal" else 0,
            "RestingECG_ST": 1 if input.RestingECG() == "ST" else 0,
            "RestingECG_LVH": 1 if input.RestingECG() == "LVH" else 0,
            "ExerciseAngina_Y": 1 if input.ExerciseAngina() == "Y" else 0,
            "ExerciseAngina_N": 1 if input.ExerciseAngina() == "N" else 0,
            "ST_Slope_Down": 1 if input.St_slope() == "Down" else 0,
            "ST_Slope_Flat": 1 if input.St_slope() == "Flat" else 0,
            "ST_Slope_Up": 1 if input.St_slope() == "Up" else 0,
        }

        # Convert to DataFrame
        df = pd.DataFrame([user_data], columns=feature_names)

        # Scale features
        df_scaled = scaler.transform(df)

        # Make prediction
        prediction = model.predict(df_scaled)
        return "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"

    # Output the result
    @output
    @reactive.render_text
    def prediction_result():
        return make_prediction()

# Create the app
app = App(app_ui, server)
