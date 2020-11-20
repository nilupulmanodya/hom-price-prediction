from flask import Flask, request, jsonify
import utill
app = Flask(__name__)

@app.route('/get_loacation_names')
def get_loacation_names():
    response = jsonify({
        'locations':utill.get_loacation_names()
    })
    response.headers.add('Access-control-Allow-origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']

    response =jsonify({
        'estimated_price' : utill.estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("starting py flask server for home price prediction..")
    app.run()


