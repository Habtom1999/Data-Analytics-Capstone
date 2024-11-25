# Import necessary modules
from shiny import App, ui, render, Inputs
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import logging
import os
print(os.path.abspath("C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\rsconnect-python\heart.csv"))


# Add logs in key areas to identify where it stalls
logging.basicConfig(level=logging.DEBUG)
logging.debug("Starting the app...")



# Load dataset and models
heart_data = pd.read_csv(r"C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\rsconnect-python\heart.csv")  # Replace with your cleaned dataset
best_model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

# Dynamically extract feature names from the trained model if supported
model_feature_names = best_model.feature_names_in_ if hasattr(best_model, "feature_names_in_") else None

# Helper functions
def ensure_numeric(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    return df

def prepare_input(user_input):
    # Convert user input to a DataFrame
    input_df = pd.DataFrame([user_input])

    # Dynamically align columns using model's expected features
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_feature_names, fill_value=0)

    # Scale the data if a scaler is provided
    if model_feature_names is not None and scaler:
        input_df[model_feature_names] = scaler.transform(input_df[model_feature_names])

    return input_df

# Define UI layout
app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.h3("Heart Failure Prediction Dashboard"),
            ui.input_slider("Age", "Age:", min=heart_data["Age"].min(), max=heart_data["Age"].max(), value=50),
            ui.input_slider("RestingBP", "Resting Blood Pressure:", min=heart_data["RestingBP"].min(), max=heart_data["RestingBP"].max(), value=120),
            ui.input_slider("Cholesterol", "Cholesterol:", min=heart_data["Cholesterol"].min(), max=heart_data["Cholesterol"].max(), value=200),
            ui.input_slider("FastingBS", "Fasting Blood Sugar:", min=heart_data["FastingBS"].min(), max=heart_data["FastingBS"].max(), value=0),
            ui.input_slider("MaxHR", "Maximum Heart Rate Achieved:", min=heart_data["MaxHR"].min(), max=heart_data["MaxHR"].max(), value=150),
            ui.input_slider("Oldpeak", "ST Depression:", min=heart_data["Oldpeak"].min(), max=heart_data["Oldpeak"].max(), value=1.0),
            ui.input_select("Sex", "Sex:", choices=["M", "F"]),
            ui.input_select("ChestPainType", "Chest Pain Type:", choices=["ATA", "NAP", "TA", "Asy"]),
            ui.input_select("RestingECG", "Resting ECG:", choices=["Normal", "ST"]),
            ui.input_select("ExerciseAngina", "Exercise Induced Angina:", choices=["Y", "N"]),
            ui.input_select("ST_Slope", "ST Slope:", choices=["Up", "Flat", "Down"])
        ),
        ui.layout_column_wrap(
            ui.div(ui.value_box("", ui.output_text("prediction_result")), class_="value-box"),
            ui.div(ui.h3("Explore Dataset"), ui.output_data_frame("heart_data_grid")),
            width=1/2
        )
    )
)

# Define the server function
def server(input, output, session):

    # Prediction calculation
    @output
    @render.text
    def prediction_result():
        user_input = {
            "Age": input.Age(),
            "RestingBP": input.RestingBP(),
            "Cholesterol": input.Cholesterol(),
            "FastingBS": input.FastingBS(),
            "MaxHR": input.MaxHR(),
            "Oldpeak": input.Oldpeak(),
            "Sex_M": 1 if input.Sex() == "M" else 0,
            "ChestPainType_ATA": 1 if input.ChestPainType() == "ATA" else 0,
            "ChestPainType_NAP": 1 if input.ChestPainType() == "NAP" else 0,
            "ChestPainType_TA": 1 if input.ChestPainType() == "TA" else 0,
            "ChestPainType_Asy": 1 if input.ChestPainType() == "Asy" else 0,
            "RestingECG_Normal": 1 if input.RestingECG() == "Normal" else 0,
            "RestingECG_ST": 1 if input.RestingECG() == "ST" else 0,
            "ExerciseAngina_Y": 1 if input.ExerciseAngina() == "Y" else 0,
            "ST_Slope_Up": 1 if input.ST_Slope() == "Up" else 0,
            "ST_Slope_Flat": 1 if input.ST_Slope() == "Flat" else 0,
            "ST_Slope_Down": 1 if input.ST_Slope() == "Down" else 0,
        }
        input_df = prepare_input(user_input)
        prediction = best_model.predict(input_df)[0]
        return "High Risk" if prediction == 1 else "Low Risk"

    # Data grid output for heart failure data
    @output
    @render.data_frame
    def heart_data_grid():
        return heart_data

# Create the Shiny app
app = App(app_ui, server)
