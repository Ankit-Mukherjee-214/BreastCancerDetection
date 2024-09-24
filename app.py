from flask import Flask, request, render_template
import pandas
import numpy as np
import pickle

# passing the model
model = pickle.load(open("breast_cancer_model.pkl", "rb"))

# Creation of the flask app
app = Flask(__name__)
#providing the path of the index.html 
@app.route('/')
def index ():
    return render_template("index.html")

#providing the path for prediction 
@app.route('/predict', methods = ['POST'])
def predic() : 
    features = request.form['feature']
    features_lst = features.split(',')
    np_features = np.asarray(features_lst,dtype=np.float32)
    pred = model.predict(np_features.reshape(1,-1))

    output = ["Malignant tumour. Chances of having breast cancer. Take care of yourself" if pred[0]==1 else "Benign tumour. No chances of cancer. Please enjoy your life!!! "]

    return render_template ('index.html', message = output)

# python main 
if __name__ == "__main__" :
    app.run(debug=True)