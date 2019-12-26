import numpy as np 
import sklearn
import pickle
from sklearn.neural_network import MLPClassifier
from flask import Flask, request, jsonify

def predict_output(num1,num2):

    output = {'output_prediction':0}
    x_input = np.array([num1,num2]).reshape(1,2)
    filename = 'model.pkl'
    m1 = pickle.load(open(filename, 'rb'))
    output['output_prediction'] = m1.predict(x_input)[0]
    print(output)
    return output

app = Flask(__name__)

@app.route("/")
def index():
    return "Previsão!"

@app.route("/prediction", methods = ['GET'])
def calc_Predict():
    body = request.get_data()
    header = request.headers

    try:
            num1 = int(request.args['x1'])
            num2 = int(request.args['x2'])

            
            if (num1 != None) and (num2 != None) and ((num1 == 0) or (num1 == 1)) and ((num2 == 0) or (num2 == 1)):
                res= predict_output(num1,num2)
            else:
                    res = {
                            'success': False,
                            'message': 'Dado digitado não está correto'}
    except:
            res = {
                    'success': False,
                    'message': 'Unknown error'
            }

    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, port=5000 )