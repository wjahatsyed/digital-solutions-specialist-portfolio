from flask import Flask, render_template, jsonify
from predictive_model import generate_prediction

app = Flask(__name__)

@app.route('/')
def index():
    """Home route to render the dashboard."""
    return render_template('index.html')

@app.route('/predict')
def predict():
    """API route to fetch predictive analytics."""
    prediction = generate_prediction()
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
