import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
regressor1 = pickle.load(open('rf_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = regressor1.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Customer Life Time Value is  {}'.format(round(output)))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = lr.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)