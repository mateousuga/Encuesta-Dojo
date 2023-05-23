from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procces', methods=['POST'])
def create_dojo():
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def result():
    return render_template('result.html', dojos = Dojo.get_all())