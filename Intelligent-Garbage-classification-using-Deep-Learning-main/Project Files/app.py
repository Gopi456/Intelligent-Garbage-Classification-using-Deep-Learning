from __future__ import division,print_function
import sys
import os
import glob
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.applications.imagenet_utils import preprocess_input,decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras import backend
from tensorflow.keras import backend
from tensorflow import keras


from skimage.transform import resizse
from flask import Flask,redirect,url_for,request,render_template
from workzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer




@app.route('/',methods=['GET'])
def index():
  return render_template('home.html')
@app.route('/Image',methods=['POST','GET'])
def prediction():
  return render_template('home.html')
@app.route('/predict',methods=['GET','POST'])
def upload():
  if request.method=='POST':
    f=request.files['image']
    basepath=os.path.dirname(__file__)
    file_path=os.paath.join(basepath,'predictions',f.filename)
    f.save(file_path)
    img=image.load_img(file_path,target_size=(128,128))
    x=image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    preds=model.predict_classes(x)
    index=['cardboard','glass','metal','paper','plastic','trash']
    text="The Predicted Garbage is :"+str(index[preds[0]])
    return text

img=image.load_img(r"/content/drive/MyDrive/Garbage classification/glass/glass10.jpg",target_size=(128,128))
x=image.img_to_array(img)
x=np.expand_dims(x,axis=0)
a=np.argmax(model.predict(x),axis=1)
@app.route('/predict',methods=['GET','POST'])
def upload():
  return 0