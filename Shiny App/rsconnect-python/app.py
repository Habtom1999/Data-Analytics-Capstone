from shiny import App, ui, reactive
import pandas as pd
import joblib
import os
# Define base directory
base_dir = os.path.abspath("C:/Capstone Project/Module 1/Data-Analytics-Capstone/Shiny App/rsconnect-python")

# Define file paths
heart_csv_path = os.path.join(base_dir, "C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\rsconnect-python\test_predictions_with_best_guess.csv")
model_path = os.path.join(base_dir, "heart_disease_model.pkl")
scaler_path = os.path.join(base_dir, "scaler.pkl")

# Verify file paths
print("Heart CSV Path:", heart_csv_path)
print("Model Path:", model_path)
print("Scaler Path:", scaler_path)

# Load model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Features expected by the model
FEATURE_NAMES = [
    "Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak",
    "Sex_M", "ChestPainType_AT", "ChestPainType_NAP", "ChestPainType_TA", "ChestPainType_Asy",
    "RestingECG_Normal", "RestingECG_ST", "RestingECG_LVH",
    "ExerciseAngina_Y", "ST_Slope_Down", "ST_Slope_Flat", "ST_Slope_Up"
]

# Define the UI
app_ui = ui.page_fluid(
    ui.h2("Heart Disease Prediction App"),
    ui.row(
        ui.column(6, ui.input_numeric("age", "Age:", value=50, min=0, max=120)),
        ui.column(6, ui.input_select("sex", "Sex:", {"M": "Male", "F": "Female"})),
    ),
    ui.row(
        ui.column(6, ui.input_numeric("resting_bp", "Resting Blood Pressure (mm Hg):", value=120)),
        ui.column(6, ui.input_numeric("cholesterol", "Cholesterol (mg/dL):", value=200)),
    ),
    ui.row(
        ui.column(6, ui.input_select("fasting_bs", "Fasting Blood Sugar > 120 mg/dL:", {1: "Yes", 0: "No"})),
        ui.column(6, ui.input_numeric("max_hr", "Max Heart Rate:", value=150)),
    ),
    ui.row(
        ui.column(6, ui.input_numeric("oldpeak", "ST Depression Induced:", value=1.0)),
        ui.column(6, ui.input_select("exercise_angina", "Exercise-Induced Angina:", {"Y": "Yes", "N": "No"})),
    ),
    ui.row(
        ui.column(6, ui.input_select("chest_pain_type", "Chest Pain Type:", {
            "AT": "Atypical Angina",
            "NAP": "Non-Anginal Pain",
            "TA": "Typical Angina",
            "Asy": "Asymptomatic"
        })),
        ui.column(6, ui.input_select("resting_ecg", "Resting ECG Results:", {
            "Normal": "Normal",
            "ST": "ST-T Wave Abnormality",
            "LVH": "Left Ventricular Hypertrophy"
        })),
    ),
    ui.row(
        ui.column(6, ui.input_select("st_slope", "ST Slope:", {
            "Flat": "Flat",
            "Up": "Up",
            "Down": "Down"
        })),
    ),
    ui.input_action_button("predict", "Predict"),
    ui.output_text("prediction_result")
)

# Define server logic
def server(input, output, session):
    @reactive.event(input.predict)
    def make_prediction():
        # Prepare user inputs
        user_data = {
            "Age": input.age(),
            "RestingBP": input.resting_bp(),
            "Cholesterol": input.cholesterol(),
            "FastingBS": int(input.fasting_bs()),
            "MaxHR": input.max_hr(),
            "Oldpeak": input.oldpeak(),
            "Sex_M": 1 if input.sex() == "M" else 0,
            "ChestPainType_AT": 1 if input.chest_pain_type() == "AT" else 0,
            "ChestPainType_NAP": 1 if input.chest_pain_type() == "NAP" else 0,
            "ChestPainType_TA": 1 if input.chest_pain_type() == "TA" else 0,
            "ChestPainType_Asy": 1 if input.chest_pain_type() == "Asy" else 0,
            "RestingECG_Normal": 1 if input.resting_ecg() == "Normal" else 0,
            "RestingECG_ST": 1 if input.resting_ecg() == "ST" else 0,
            "RestingECG_LVH": 1 if input.resting_ecg() == "LVH" else 0,
            "ExerciseAngina_Y": 1 if input.exercise_angina() == "Y" else 0,
            "ST_Slope_Down": 1 if input.st_slope() == "Down" else 0,
            "ST_Slope_Flat": 1 if input.st_slope() == "Flat" else 0,
            "ST_Slope_Up": 1 if input.st_slope() == "Up" else 0,
        }

        # Convert user data to a DataFrame
        df = pd.DataFrame([user_data], columns=FEATURE_NAMES)

        # Scale the input features
        df_scaled = scaler.transform(df)

        # Make a prediction
        prediction = model.predict(df_scaled)[0]
        return "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    @output
    @reactive.render_text
    def prediction_result():
        return make_prediction()

# Create the app
app = App(app_ui, server)
