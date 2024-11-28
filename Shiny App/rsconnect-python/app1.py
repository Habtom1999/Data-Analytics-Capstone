from shiny import App, ui, render, Inputs
import pandas as pd
import joblib
import numpy as np
from ipyleaflet import Map, Choropleth, Marker, Popup
from ipywidgets.embed import embed_minimal_html
from branca.colormap import linear
from ipywidgets import HTML
import json
import tempfile
file_path = 'C:/Capstone Project/Module 1/Data-Analytics-Capstone/Shiny App/rsconnect-python/test_predictions_with_best_guess.csv'

# Load data and model
heart_data = pd.read_csv("C:/Capstone Project/Module 1/Data-Analytics-Capstone/Shiny App/rsconnect-python/test_predictions_with_best_guess.csv")
heart_model = joblib.load("heart_disease_model.pkl")
model_columns = joblib.load("heart_model_columns.pkl")
scaler = joblib.load("scaler.pkl")

# Helper functions
def to_str_choices(series):
    return sorted(map(str, series.unique()))

# Ensure input data fields are numeric and handle preprocessing for model input
def ensure_numeric(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    return df

def prepare_input(user_input):
    input_df = pd.DataFrame([user_input])
    input_df = ensure_numeric(input_df, ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    scaled_input_df = input_df.copy()
    scaled_input_df[scaler.feature_names_in_] = scaler.transform(input_df[scaler.feature_names_in_])
    return scaled_input_df
app_ui = ui.page_fluid(
    ui.tags.style("""
        .value-box {
            height: 200px;  /* Adjust height as desired */
        }
        .grid-map-container {
            height: 300px;  /* Set a fixed height for both the grid and map */
        }
    """),

    ui.layout_sidebar(
        ui.sidebar(
            ui.h3("Heart Disease Prediction Dashboard", width=1),

            ui.input_slider("age", "Age:", min=int(heart_data["age"].min()), max=int(heart_data["age"].max()), value=50),
            ui.input_select("sex", "Sex:", choices=to_str_choices(heart_data["sex"])),
            ui.input_select("cp", "Chest Pain Type:", choices=to_str_choices(heart_data["cp"])),
            ui.input_slider("trestbps", "Resting Blood Pressure:", min=int(heart_data["trestbps"].min()), max=int(heart_data["trestbps"].max()), value=120),
            ui.input_slider("chol", "Serum Cholesterol:", min=int(heart_data["chol"].min()), max=int(heart_data["chol"].max()), value=200),
            ui.input_select("fbs", "Fasting Blood Sugar > 120 mg/dl:", choices=to_str_choices(heart_data["fbs"])),
            ui.input_select("restecg", "Resting Electrocardiographic Results:", choices=to_str_choices(heart_data["restecg"])),
            ui.input_slider("thalach", "Maximum Heart Rate Achieved:", min=int(heart_data["thalach"].min()), max=int(heart_data["thalach"].max()), value=150),
            ui.input_select("exang", "Exercise Induced Angina:", choices=to_str_choices(heart_data["exang"])),
            ui.input_slider("oldpeak", "Depression Induced by Exercise:", min=float(heart_data["oldpeak"].min()), max=float(heart_data["oldpeak"].max()), value=1.0),
            ui.input_select("slope", "Slope of Peak Exercise ST Segment:", choices=to_str_choices(heart_data["slope"])),
            ui.input_select("ca", "Number of Major Vessels Colored by Fluoroscopy:", choices=to_str_choices(heart_data["ca"])),
            ui.input_select("thal", "Thalassemia:", choices=to_str_choices(heart_data["thal"]))
        ),
        ui.layout_column_wrap(
            ui.div(
                ui.value_box("", ui.output_text("heart_disease_prediction")),
                class_="value-box"
            ),
            width=1/2
        ),
        ui.layout_column_wrap(
            ui.div(
                ui.h3("Explore Heart Disease Dataset"),  
                ui.output_data_frame("heart_data_grid"),
                class_="fixed-height-container"
            ),
            width=1/2
        )
    )
)
def server(input, output, session):

    # Heart disease prediction
    @output
    @render.text
    def heart_disease_prediction():
        user_input = {
            "age": input.age(),
            "sex": input.sex(),
            "cp": input.cp(),
            "trestbps": input.trestbps(),
            "chol": input.chol(),
            "fbs": input.fbs(),
            "restecg": input.restecg(),
            "thalach": input.thalach(),
            "exang": input.exang(),
            "oldpeak": input.oldpeak(),
            "slope": input.slope(),
            "ca": input.ca(),
            "thal": input.thal()
        }
        input_df = prepare_input(user_input)
        prediction = heart_model.predict(input_df)[0]
        return "Heart Disease Risk: " + ("High" if prediction == 1 else "Low")

    # Data grid output for heart disease data with dropdown filters for each column
    @output
    @render.data_frame
    def heart_data_grid():
        return render.DataGrid(heart_data, filters=True)
# Create the Shiny app
app = App(app_ui, server)


