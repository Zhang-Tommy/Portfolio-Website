from flask import Flask, render_template, Response, send_file, redirect, url_for
from flask_bootstrap import Bootstrap
import os
from waitress import serve

# Initialize web app and dependencies
os.environ['FLASK_APP'] = 'main'
app = Flask(__name__)

# Routing to home page
# On form submission, redirect to start distribution fitting
@app.route("/")
def index():
    return render_template('./index.html', methods=['GET', 'POST'])

@app.route("/get_resume")
def get_resume():
    return render_template('./resume_viewer.html', methods=['GET', 'POST'])

@app.route('/pdf/') #the url you'll send the user to when he wants the pdf
def pdfviewer():
    return send_file("templates/TZ_Resume.pdf") #the pdf itself

serve(app, listen='*:8080')