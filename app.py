import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask("CompanyWebsite")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/", methods=['GET', 'POST'])
def login():

    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
           
            return redirect('https://integration-project-ak.herokuapp.com/')
   
        else:
            error = 'Insert valid credentials to continue'
    return render_template('login.html', error=error)






    # if request.method == 'POST':
    #     data = request.form
    #     username = data["username"]
    #     password = data["password"]
    #     if username == "pepe" and password == "1234":
    #         return redirect('https://integration-project-ak.herokuapp.com/')
    #     else:
    #         flash('Login failed! Credentials: "pepe","1234"')
    #         return render_template('index.html')    

    # else:        
    #     return render_template('index.html')    

app.run()
