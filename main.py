# Python Interpreter: 3.12.4 (.venv)
import os
# import git
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
FLASK_SECRET_KEY = '26e5210299d1e99574c25f6657c90fa2'
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
# os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


with app.app_context():
    db.create_all()


'''
This is an example of the Flask framework "calling" the code, rather than the
code calling a function. The framework calls the programmer-defined functions
such as home_page().
'''


@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # checks if entries are valid
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash(f'Error: Account already exists for {form.email.data}.')
            return redirect(url_for('register'))

        user = User(username=form.username.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))  # if so - send to home page
    return render_template('register.html', title='Register', form=form)


@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/chiagozie3spotify3shortcuts/codio_project')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
