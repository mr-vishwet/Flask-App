from flask import Flask, render_template, request
import PyPDF2
import re

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('error.html')


@app.route('/troubleshoot')
def troubleshoot():
    return app.send_static_file('sample.pdf')
