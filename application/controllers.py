#methods imported from flask module
from flask import Flask,render_template, redirect, request,url_for, flash
from werkzeug.utils import secure_filename
from flask import current_app as app
import uuid as uuid
import os
import requests

#models content imported in this file
from .models import *

@app.route('/')
def index():
    locs=Location.query.all()
    return render_template('index.html',locs=locs)


@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        name=request.form.get('name')
        address=request.form.get('address')
        about=request.form.get('about')
        place='%20'.join(address.split())
        url2=f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json?access_token=pk.eyJ1Ijoia2FyYW5qMTlzb2UiLCJhIjoiY203dzNjOXNiMDFqaTJrczhrYXc1dzVybSJ9.bRGtqhk_MYdnOeo2yyEtTw"
        response=requests.get(url2)
        res=response.json()
        coordinates=res["features"][0]["geometry"]["coordinates"]
        l=Location(name=name,lat=coordinates[0],lon=coordinates[1],about=about,role=2)
        db.session.add(l)
        db.session.commit()
        url4=f"https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/{coordinates[0]},{coordinates[1]},18/600x600?access_token=pk.eyJ1Ijoia2FyYW5qMTlzb2UiLCJhIjoiY203dzNjOXNiMDFqaTJrczhrYXc1dzVybSJ9.bRGtqhk_MYdnOeo2yyEtTw"
        response=requests.get(url4)
        save_folder = ".\static\images" 
        os.makedirs(save_folder, exist_ok=True)
        file_path = os.path.join(save_folder, f"{l.id}.png")  
        with open(file_path, "wb") as file:
            file.write(response.content)
        return redirect('/')


