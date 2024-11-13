

## Setting Up Python and Installing Packages
Step 1: Install Python 3
Step 2: Verify that you have Python 3
Open a new terminal window (CMD/Powershell, Terminal, xterm, etc), and run the following command: python3 --version
Step 3: Create  Virtual Environment
Run the following command to create a virtual environment
python3 -m venv env
Step 4: Activate the environment
.venv\Scripts\activate
Step 5: Installing packages
The normal way to install a package is to run the command:
pip install <packagename>

Installing JupyterLab and Matplotlib
Run
pip install jupyterlab matplotlib
Installing other packages
Once you have activated your environment, you can install new packages in the same way you installed jupyterlab: pip install <package name>.

If you open a shell and install packages while you are running JupyterLab, you will need to restart your kernel (using the menu or the refresh button in the Notebook interface) to pick up the new packages

JupyterLab
One option (if you want to avoid using a terminal) is to open the directory where you created your virtual environment, and run jupyter-lab from either the bin or Scripts directory, depending on whether you’re on MacOS or Windows, respectively. Windows may open a web browser that says it cannot find the file; copy and paste the URLs (usually httplocalhost:8888/?token=<sometoken>) and paste it in your browser. You should be able to create shortcuts to this jupyter-lab to make it easier to find. Consult your OS and the internet on how to do this correctly.
Windows Terminal
Open your settings tab and create a new profile. Duplicate Powershell, change the name to something descriptive, and the command to %userprofile%\wmvenv\Scripts\python -m jupyterlab. Every time you open a terminal tab with this profile it will start Jupyter Lab and open a tab in a web browser.

Otherwise
Open a terminal
Activate your virtual environment
run jupyter lab
## Data-Analytics-Capstone 

## Heart Disease Prediction 
 By Habtom Woldu 
 North West Missouri State University 
 Email S565467@nwmissouri.edu, habtoma1999@gmail.com

### Abstrat 
The main focues of this study is to predict heart disease based on the clincal data set contianing patient attributes. By analyzing this data set, it can be possible to predict heart disease by developing machine learning model.

### Introduction 

Cardio vascular Disease (VDs) are a group of disorders of the heart and blood vessels. According to the WHO, Heart disease is leading causes of death worldwide, taking an estimated 17.9 million lives each year. There is a massive amount of data in the healthcare industry, and processing this amount of data is a tedious task. A computer-aided system that predicts cardiac disease can save time and money.  Those at highest risk of CVDs and ensuring they receive appropriate treatment can prevent premature deaths.

### Problem Statment 
Identifying individuals at risk of heart disease is crucial for preventing adverse outcomes and improving patient prognosis.leverage a dataset containing various patient health attributes — including age, sex, chest pain type, blood pressure, cholesterol levels, and more — to analyze and predict the likelihood of heart disease
### Goals of the Project
The objective of this project is to leverage a dataset containing various patient health attributes — including age, sex, chest pain type, blood pressure, cholesterol levels, and more — to analyze and predict the likelihood of heart disease. By using data analytics and machine learning techniques, this project will develop a predictive model capable of distinguishing between high-risk and low-risk patients

### Data Set 
This dataset, obtained from Kaggle, contains 11 commonly measured features associated with cardiovascular health and disease risk. It includes key patient health attributes such as age, sex, chest pain type, resting blood pressure, cholesterol levels, fasting blood sugar, resting electrocardiogram (ECG) results, maximum heart rate achieved, exercise-induced angina, oldpeak (ST depression induced by exercise relative to rest), and the ST slope. With around 918 observations, this dataset provides a robust foundation for the development of predictive models.
## Data Source:  https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

## Data Description
 The heart failure prediction data set includes key patient health attributes such as age, sex, chest pain type, resting blood pressure, cholesterol levels, fasting blood sugar, resting electrocardiogram (ECG) results, maximum heart rate achieved, exercise-induced angina, old peak (ST depression induced by exercise relative to rest), and the ST slope. With around 918 observations, this dataset provides a robust foundation for the development of predictive models
