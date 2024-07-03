# Python Interpreter: 3.12.4 (.venv)
from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')


@app.route('/')
@app.route("/home")
def home_page():
    return render_template('home.html', subtitle='Welcome',
                           text='This is the welcome page')


'''
This is an example of the Flask framework "calling" the code, rather than the
code calling a function. The framework calls the programmer-defined functions
such as home_page().
'''
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
