from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
#from sklearn.preprocessing import MinMaxScaler
app = Flask(__name__,template_folder='templates')
with open('crop.pkl','rb') as f:
        model=pickle.load(f)

#standard_to = MinMaxScaler()
@app.route("/", methods=['GET','POST'])
def main():
        #Fuel_Type_Diesel=0
        if request.method == 'POST':
                temperature=request.form.get('temperature')
                humidity=request.form.get('humidity')
                ph=request.form.get('ph')
                rainfall=request.form.get('rainfall')
                crop=['Adzuki Beans', 'Black gram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton', 'Ground Nut', 'Jute', 'Kidney Beans', 'Lentil', 'Moth Beans', 'Mung Bean', 'Peas', 'Pigeon Peas', 'Rubber', 'Sugarcane', 'Tea', 'Tobacco', 'apple', 'banana', 'grapes', 'maize', 'mango', 'millet', 'muskmelon', 'orange', 'papaya', 'pomegranate', 'rice', 'watermelon', 'wheat']
                
                prediction=model.predict([[temperature,humidity,ph,rainfall]])
                print(prediction)
                #output=round(prediction[0],2)
                #rec_crop=crop[prediction]
                if prediction==0:
                   return render_template('main.html',result='The recommended crop is Adzuki Beans')
                if prediction==1:
                   return render_template('main.html',result='The recommended crop is Black gram')
                if prediction==2:
                   return render_template('main.html',result='The recommended crop is Chickpea')
                if prediction==3:
                   return render_template('main.html',result='The recommended crop is Coconut')
                if prediction==4:
                   return render_template('main.html',result='The recommended crop is Coffee')
                if prediction==5:
                   return render_template('main.html',result='The recommended crop is Cotton')  
                if prediction==6:
                   return render_template('main.html',result='The recommended crop is Ground Nut')
                if prediction==7:
                   return render_template('main.html',result='The recommended crop is Jute')
                if prediction==8:
                   return render_template('main.html',result='The recommended crop is Kidney Beans')
                if prediction==9:
                   return render_template('main.html',result='The recommended crop is Lentil')
                if prediction==10:
                   return render_template('main.html',result='The recommended crop is Moth Beans')
                if prediction==11:
                   return render_template('main.html',result='The recommended crop is Mung Bean')
                if prediction==12:
                   return render_template('main.html',result='The recommended crop is Peas')
                if prediction==13:
                   return render_template('main.html',result='The recommended crop is Pigeon Peas')
                if prediction==14:
                   return render_template('main.html',result='The recommended crop is Rubber')
                if prediction==15:
                   return render_template('main.html',result='The recommended crop is Sugarcane')
                if prediction==16:
                   return render_template('main.html',result='The recommended crop is Tea')
                if prediction==17:
                   return render_template('main.html',result='The recommended crop is Tobacco')
                if prediction==18:
                   return render_template('main.html',result='The recommended crop is apple')
                if prediction==19:
                   return render_template('main.html',result='The recommended crop is banana')
                if prediction==20:
                   return render_template('main.html',result='The recommended crop is grapes')
                if prediction==21:
                   return render_template('main.html',result='The recommended crop is maize')
                if prediction==22:
                   return render_template('main.html',result='The recommended crop is mango')
                if prediction==23:
                   return render_template('main.html',result='The recommended crop is millet')
                if prediction==24:
                   return render_template('main.html',result='The recommended crop is muskmelon')
                if prediction==25:
                   return render_template('main.html',result='The recommended crop is orange')
                if prediction==26:
                   return render_template('main.html',result='The recommended crop is papaya')
                if prediction==27:
                   return render_template('main.html',result='The recommended crop is pomegranate')
                if prediction==28:
                   return render_template('main.html',result='The recommended crop is rice')
                if prediction==29:
                   return render_template('main.html',result='The recommended crop is watermelon')
                if prediction==30:
                   return render_template('main.html',result='The recommended crop is wheat')
                


        else:
                return render_template('main.html')

if __name__=="__main__":
        app.run(debug=True)
