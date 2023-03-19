from flask import Flask, render_template, request
import PyPDF2
import re
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('error.html')


@app.route('/troubleshoot')
def troubleshoot():
    return app.send_static_file('sample.pdf')


if __name__ == "__main__":
    # This line will start the Flask app on port 8080
    port = 5000

    # Check if the port is already in use
    output = subprocess.check_output(['lsof', '-i', f':{port}'])
    if output:
    # If the port is in use, extract the PID of the process
        pid = int(output.split()[10])
    # Kill the process
        subprocess.call(['sudo', 'kill', '-9', str(pid)])

    # Run your Flask app on the desired port
    app.run(port=port)
