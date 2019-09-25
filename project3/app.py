import os

import pandas as pd
import numpy as np
import numpy as np
import requests
#import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd

import csv
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
#import python_project.python_run 
from sqlalchemy import create_engine
import json
import os
from pprint import pprint


app = Flask(__name__)

array1 = []
array2 = []
array3 = []
array4 = []
array5 = []
array6 = []
array7 = []
name_dict = {}
mars_data = []
@app.route("/")
def index(): 
    """Return the homepage."""
    return render_template("index.html")


@app.route("/player_data/")
def player_data():
    
    # engine = create_engine('sqlite://NBA_data', echo=False)
    # choosen_csv = "/static/social-power-nba/nba_2017_players_with_salary_wiki_twitter.csv"
    # df = pd.read_csv(choosen_csv)
    # df.to_sql('NBA', con=engine)
    # Dependencies

    # Load JSON
    filepath = os.path.join("static", "social-power-nba", "nbaJSON.json")
    with open(filepath) as jsonfile:
        json_data = json.load(jsonfile)

    return jsonify(json_data)


@app.route("/playerList/<player_first_name>/<player_last_name>")
def playList(player_first_name,player_last_name):
    # player_name = "Lebron james"
    # first_name = player_name.split(" ")[0]
    # last_name = player_name.split(" ")[1]
    image_url = "https://en.wikipedia.org/wiki/"+player_first_name+"_"+player_last_name
    request = requests.get(image_url)
    soup4 = BeautifulSoup(request.text, 'html.parser')
    result = soup4.find_all(attrs={'class','infobox vcard'})

    url_image_scraped = {"url":"https://" + result[0].img.get("src").replace("//","",1)}


    return jsonify(url_image_scraped)


@app.route("/list_of_players")
def list_of_players():
        # Load JSON

    filepath = os.path.join("static", "social-power-nba", "nbaJSON.json")
    with open(filepath) as jsonfile:
        json_data = json.load(jsonfile)

    for row in list(range(0,len(json_data))):
        name_dict.update({ json_data[row]['player'] : row })

    return jsonify(list(name_dict))
















if __name__ == "__main__":
    app.run()
