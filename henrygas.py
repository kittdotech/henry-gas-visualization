from flask import Flask,request, send_from_directory
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	"""Renders the Daily Data (Default) """

	return render_template('home.html', name='price_daily')

@app.route('/<name>')
def home(name):
    """To render the template based on daily, weekly, monthly & yearly"""
    
    return render_template('home.html', name=name)

@app.route('/static/<path:path>')
def send_js(path):
	"""To serve static files."""
	
	return send_from_directory('static', path)


if __name__ == "__main__":
    app.run()
