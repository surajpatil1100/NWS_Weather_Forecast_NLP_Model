from flask import Flask, render_template
import json

app = Flask(__name__)

def load_forecast_data():
    with open('forecast_data.json', 'r') as infile:
        data = json.load(infile)
    return data

@app.route('/')
def index():
    data = load_forecast_data()
    summary = data.get("summary", "No summary available")
    positive_forecast = data.get("positive_forecast", "No positive forecast available")
    return render_template('index.html', summary=summary, positive_forecast=positive_forecast)

if __name__ == '__main__':
    app.run(debug=True)
