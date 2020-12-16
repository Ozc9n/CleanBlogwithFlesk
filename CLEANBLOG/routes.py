from CLEANBLOG import app
from flask import Flask
from flask import render_template



@app.route('/')     
def index():
    return render_template('index.html')
