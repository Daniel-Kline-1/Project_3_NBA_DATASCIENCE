import os

import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import csv

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/player_data/<player_first_name><player_last_name>")
def player_data(player_first_name,player_last_name):

    return ''
    

@app.route("")




















if __name__ == "__main__":
    app.run()
