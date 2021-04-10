import pickle
import pandas as pd
import numpy as np
import re
from flask import Flask, render_template, request, jsonify

print('starting')
filename = 'get_recs.pkl'
ratings_file = 'ratings_model.pkl'
get_recs = pickle.load(open(filename, 'rb'))
get_ratings = pickle.load(open(ratings_file, 'rb'))

app = Flask(__name__)

def get_recommendations(anime_name):
  try:
      print('NAME', anime_name)
      anime_user_ratings = get_recs[anime_name]
      similar_to_anime = get_recs.corrwith(anime_user_ratings)
      corr_anime = pd.DataFrame(similar_to_anime, columns = ['Correlation'])
      corr_anime.dropna(inplace = True)
      corr_anime = corr_anime.join(get_ratings['num_ratings'])
      print('return successful')
      return corr_anime[corr_anime['num_ratings'] > 1000].sort_values('Correlation', ascending = False).iloc[0:10, :].index.tolist()
  except KeyError:
      print('Anime not found')
      return 'Not Found'



@app.route('/', methods = ['GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/recommendations/<anime>', methods = ['GET'])
def recommendations(anime):
    if request.method == 'GET':
        print('anime', anime)
        recs = get_recommendations(anime)
        return {'recs': recs}


if __name__ == '__main__':
    app.run(debug=True)
