from shiny import App, ui, reactive
import pandas as pd
import joblib
import os
import seaborn as sns
from flask import Flask
from flask import Flask, render_template, send_file, request
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Initialize the Flask app
app = Flask(__name__)

# Path to the predictions CSV file
predictions_file_path = r"C:\Capstone Project\Module 1\Data-Analytics-Capstone\Shiny App\rsconnect-python\test_predictions_with_best_guess.csv"

# Route for the homepage
@app.route("/")
def home():
    # Load predictions data
    if os.path.exists(predictions_file_path):
        predictions_df = pd.read_csv(predictions_file_path)

        # Convert DataFrame to an HTML table
        table_html = predictions_df.to_html(classes="table table-striped", index=False)

        return f"<h1>Heart Disease Predictions</h1>{table_html}"
    else:
        return "<h1>Error: Predictions file not found!</h1>"

# Route for visualization
@app.route("/visualization")
def visualization():
    if os.path.exists(predictions_file_path):
        predictions_df = pd.read_csv(predictions_file_path)

        # Create a plot
        sns.countplot(x='HeartDisease_Prediction', data=predictions_df)
        plt.title("Distribution of Heart Disease Predictions")
        plt.xlabel("Prediction (0 = No Heart Disease, 1 = Heart Disease)")
        plt.ylabel("Count")

        # Save the plot to a file
        plot_file_path = "static/prediction_distribution.png"
        plt.savefig(plot_file_path)
        plt.close()

        return f"<h1>Prediction Distribution</h1><img src='/static/prediction_distribution.png' alt='Distribution Plot'>"
    else:
        return "<h1>Error: Predictions file not found!</h1>"

# Route for downloading the predictions file
@app.route("/download")
def download_file():
    if os.path.exists(predictions_file_path):
        return send_file(predictions_file_path, as_attachment=True)
    else:
        return "<h1>Error: Predictions file not found!</h1>"

# Route for submitting new patient data for prediction
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Retrieve user input from form
        age = request.form.get('age')
        cholesterol = request.form.get('cholesterol')
        # Add more fields as necessary

        # Here you would load the model and scaler, process the input, and return predictions
        # For simplicity, we'll return the received input
        return f"<h1>Prediction Result</h1><p>Age: {age}, Cholesterol: {cholesterol}</p>"

    return '''
        <h1>Enter Patient Data for Prediction</h1>
        <form method="post">
            Age: <input type="text" name="age"><br>
            Cholesterol: <input type="text" name="cholesterol"><br>
            <input type="submit" value="Predict">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
