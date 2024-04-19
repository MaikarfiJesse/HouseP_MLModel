from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['bedrooms']
    val2 = request.form['bathrooms']
    val3 = request.form['floors']
    val4 = request.form['yr_built']
    
    arr = np.array([val1, val2, val3, val4], dtype=np.float64)
        
    pred = model.predict(arr.reshape(1, -1))

    return render_template('index.html', data=int(pred[0]))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5004)
