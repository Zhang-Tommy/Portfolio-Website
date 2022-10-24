from flask import Flask, render_template, Response, send_file, redirect, url_for
from flask_bootstrap import Bootstrap
import os

# Initialize web app and dependencies
os.environ['FLASK_APP'] = 'main'
app = Flask(__name__)

# Routing to home page
# On form submission, redirect to start distribution fitting
@app.route("/")
def index():
    return render_template('./index.html', methods=['GET', 'POST'])

app.run(debug=False, port=5000, use_reloader=False)