# Python Interpreter: 3.12.4 (.venv)
import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

'''
This is an example of the Flask framework "calling" the code, rather than the
code calling a function. The framework calls the programmer-defined functions
such as home_page().
'''


@app.route("/")
def hello_world():
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))  # if so - send to home page
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
