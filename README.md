# Air Quality Analysis Project: Dongsi Station

## Live Dashboard

https://pepriandika-codingcamp-da.streamlit.app/

## Project Overview

This project, submitted for the "Learn Data Analysis with Python" course from Dicoding, focuses on analyzing air quality data, from the Dongsi station. 
## Course Submission

This analysis serves as a course submission for "Learn Data Analysis with Python" offered by Dicoding. It demonstrates the application of data analysis techniques and visualization skills learned in the course.

## Table of Contents

- [Introduction](#introduction)
- [Data Source](#data-source)
- [Libraries Used](#libraries-used)
- [Key Insights](#key-insights)
- [How to Run the Dashboard](#how-to-run-the-dashboard)
- [About Me](#about-me)

## Introduction

The goal of this project is to analyze air quality data,

## Data Source

The dataset used in this project includes air quality measurements from the Dongsi station.

## Libraries Used

- Streamlit
- Pandas
- Matplotlib
- NumPy
- math

## Key Insights

- Annual trends show that PM2.5 levels tend to rise during winter and decrease in summer, indicating a seasonal impact on air quality.
- Wind direction plays a crucial role in pollutant dispersion. Pollution levels tend to be higher when wind speeds are low, while stronger winds help disperse and reduce pollutant concentrations.
- The safest time for outdoor activities is usually from midday to late afternoon when air pollution levels are relatively lower compared to early morning or nighttime.
- Rainfall significantly reduces air pollution levels, particularly PM2.5 and PM10, as rain helps cleanse the atmosphere by washing away pollutants.
## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Create and Activate a Python Environment**:

   - If using Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
     ```
     conda create --name airquality-ds python=3.9
     conda activate airquality-ds
     ```
   - If using venv (standard Python environment tool):
     ```
     python -m venv airquality-ds
     source airquality-ds/bin/activate  # On Windows use `airquality-ds\Scripts\activate`
     ```

2. **Install Required Packages**:

   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install -r requirements.txt
     ```

### Run the Streamlit App

1. **Navigate to the Project Directory** where `app.py` is located.

2. **Run the Streamlit App**:

   ```
   streamlit run app.py
   ```

### Additional Files

- The dataset used for this analysis is included in the project repository.
- A detailed Python notebook (`Submission_Data_Analis.ipynb`) containing the data analysis and visualizations is also provided.

---

## About Me

- **Name**: Pepri Andika
- **Dicoding ID**: pepriandika

