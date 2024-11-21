from shiny import App, ui, reactive
import joblib
import pandas as pd
import joblib
import os
from shiny import App, ui


# Replace with the absolute path to your model
model_path = r"C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\heart_disease_model.pkl"
scaler_path = r"C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\scaler.pkl"

# Load pre-trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Replace with the absolute path to your model
#model_path = r"C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\heart_disease_model.pkl"
#scaler_path = r"C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\scaler.pkl"

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Load pre-trained model and scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

# Features for the model
feature_names = [
    "Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak",
    "Sex_M", "ChestPainType_ATA", "ChestPainType_NAP", "ChestPainType_TA",
    "RestingECG_Normal", "RestingECG_ST", "ExerciseAngina_Y", "ST_Slope_Flat", "ST_Slope_Up"
]

# Define the app UI

app_ui = ui.page_fluid(
    ui.h2("Heart Disease Test"),
    ui.row(
        ui.column(4, ui.input_numeric("age", "Age:", 20)),
        ui.column(4, ui.input_select("sex", "Sex:", {"M": "Male", "F": "Female"})),
    ),
    ui.row(
        ui.column(4, ui.input_numeric("resting_bp", "Resting Blood Pressure (mm Hg):", 110)),
        ui.column(4, ui.input_numeric("cholesterol", "Serum Cholesterol (mg/dL):", 230)),
    ),
    ui.row(
        ui.column(4, ui.input_select("fasting_bs", "Fasting Blood Sugar > 120 mg/dL:", {1: "True", 0: "False"})),
        ui.column(4, ui.input_numeric("max_hr", "Maximum Heart Rate:", 140)),
    ),
    ui.row(
        ui.column(4, ui.input_numeric("oldpeak", "ST Depression Induced:", 2.2)),
        ui.column(4, ui.input_select("exercise_angina", "Exercise-Induced Angina:", {1: "Yes", 0: "No"})),
    ),
    ui.row(
        ui.column(4, ui.input_select("chest_pain", "Chest Pain Type:", {"TA": "Typical Angina", "ATA": "Atypical Angina", "NAP": "Non-Anginal Pain", "ASY": "Asymptomatic"})),
        ui.column(4, ui.input_select("st_slope", "Slope of ST Segment:", {"Flat": "Flat", "Up": "Upward", "Down": "Downward"})),
    ),
    ui.row(
        ui.column(4, ui.input_numeric("num_vessels", "Number of Vessels Colored by Fluoroscopy:", 0)),
        ui.column(4, ui.input_select("thal", "Thalassemia:", {"Normal": "Normal", "Fixed": "Fixed Defect", "Reversible": "Reversible Defect"})),
    ),
    ui.action_button("predict", "Result"),
    ui.output_text("prediction_result")
)

# Define the server logic
def server(input, output, session):
    @reactive.event(input.predict)
    def make_prediction():
        # Gather input values
        user_data = {
            "Age": input.age(),
            "RestingBP": input.resting_bp(),
            "Cholesterol": input.cholesterol(),
            "FastingBS": int(input.fasting_bs()),
            "MaxHR": input.max_hr(),
            "Oldpeak": input.oldpeak(),
            "Sex_M": 1 if input.sex() == "M" else 0,
            "ChestPainType_ATA": 1 if input.chest_pain() == "ATA" else 0,
            "ChestPainType_NAP": 1 if input.chest_pain() == "NAP" else 0,
            "ChestPainType_TA": 1 if input.chest_pain() == "TA" else 0,
            "RestingECG_Normal": 0,
            "RestingECG_ST": 0,
            "ExerciseAngina_Y": int(input.exercise_angina()),
            "ST_Slope_Flat": 1 if input.st_slope() == "Flat" else 0,
            "ST_Slope_Up": 1 if input.st_slope() == "Up" else 0,
        }
        # Convert to DataFrame
        df = pd.DataFrame([user_data])
        
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
