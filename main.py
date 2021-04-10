import pickle
import pandas as pd
import numpy as np
import re
from flask import Flask, render_template, request, jsonify

# from anime import top_anime
# from recommendations import get_recommendations

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
        # top_20 = top_anime()
        # print('top', top_20)
        return render_template('index.html')

@app.route('/recommendations/<anime>', methods = ['GET'])
def recommendations(anime):
    if request.method == 'GET':
        print('anime', anime)
        recs = get_recommendations(anime)
        return {'recs': recs}

# @app.route('/predict', methods = ['POST'])
# def result():
#     if request.method == 'POST':
#         print('POST request form', request.form['name'])
#         rec_model = get_recommendations(request.form['name'])
#         try:
#             rec_arr = list(rec_model.index)
#             return render_template('recommend.html', recommendations = rec_arr)
#         except:
#             print('no recommendations')
#             return render_template('not_found.html', anime=request.form['name'])



if __name__ == '__main__':
    app.run(debug=True)
