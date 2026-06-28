from flask import Flask, request, render_template, flash, redirect, url_for
import joblib
import json

app = Flask(__name__)

model=joblib.load("model/rt.lb")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/project',methods=['GET','POST'])
def predict():

    if request.method=="POST":

        brand_name=request.form['brand_name']             #request.form to get data from user input
        owner=int(request.form['owner'])
        age=int(request.form['age'])                      #added int to change  type from str to int
        power=int(request.form['power'])
        kms_driven=int(request.form['kms_driven']) 

        brand_dict={'TVS':1, 'Royal Enfield':2, 'Triumph':3, 'Yamaha':4, 'Honda':5, 'Hero':6,
       'Bajaj':7, 'Suzuki':8, 'Benelli':9, 'KTM':10, 'Mahindra':11, 'Kawasaki':12,
       'Ducati':13, 'Hyosung':14, 'Harley-Davidson':15, 'Jawa':16, 'BMW':17, 'Indian':18,
       'Rajdoot':19, 'LML':20, 'Yezdi':21, 'MV':22, 'Ideal':23}
        
        brand_name=brand_dict.get(brand_name)  # to change type from str to int

        # print([[brand_name,age,kms_driven,owner,power]])
        # print("types of data:",type(brand_name),type(age),type(kms_driven),type(owner),type(power))
        data=[[brand_name,owner,age,power,kms_driven]]
        pred=model.predict(data)
        print("prediction",pred)
        return render_template('project.html',prediction=pred)

    
    return render_template('project.html')

if __name__ == "__main__":
    app.run(debug=True)