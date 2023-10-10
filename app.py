from flask import Flask, Blueprint, render_template

from ebird_api import top_five_birds, top_three_contributors

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/home')
def home():
    
    return render_template('index.html', top_five_birds=top_five_birds, top_three_contributors=top_three_contributors)