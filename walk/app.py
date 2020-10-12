#add code for flask app object
from flask import Flask

app = Flask(__name__)

#set route for user navigation
@app.route('/')

#define app function
def index():
    return render_template("index.html")