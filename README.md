# NWS_Weather_Forecast_NLP_Model
This model uses API from NWS website to get input data. Text processing task done by NLTK and spacy NLP libraries to get data as well summarizes it to get understandable weather forecast and also sentiment analysis to get most positive data at end Flask is used for web interface where output is visible   

## Weather Forecast Summarization and Web Display

This project fetches weather forecast data, processes it to extract a summary and positive forecast, and displays the results on a web application using Flask. The web interface shows the positive forecast in large bold letters, the summary in medium font, and a background image related to weather with a small image of Minnesota.

## Features
- Fetches weather forecast data from the National Weather Service (NWS) API.
- Cleans and processes the forecast data.
- Performs Natural Language Processing (NLP) operations, including sentiment analysis and text summarization.
- Displays the processed data on a visually appealing web interface using Flask.

## Requirements

- Python 3.10 or higher
- Required Python libraries:
  - Flask
  - requests
  - pandas
  - nltk
  - spacy
  - JSON

You can install the required libraries using pip:

```bash
pip install flask requests pandas nltk spacy

git clone https://github.com/your-repo/weather-forecast-app.git
cd weather-forecast-app

