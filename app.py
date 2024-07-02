from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')


@app.route('/')
@app.route("/home")
def home_page():
    return render_template('home.html', subtitle='Welcome',
                           text='This is the welcome page')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
