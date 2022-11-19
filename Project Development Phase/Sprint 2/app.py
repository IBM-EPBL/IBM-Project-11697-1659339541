from flask import Flask,render_template
import pickle
import numpy as np
import requests

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def hello_world():
	return render_template('checking_url.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in requests.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)[0]

    if prediction==1:
        return render_template('checking_url.html',pred='This website is safe.'.format(prediction))
    else:
        return render_template('checking_url.html',pred='This website is not safe.'.format(prediction))

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
