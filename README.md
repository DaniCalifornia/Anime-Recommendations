# Anime Recommendations

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)


Ratings based recommendation system that recommends anime similar to those the user likes using collaborative filtering and analysis of anime ratings from a Kaggle dataset. Written in Python using Flask framework.

## Getting Started

You need to have a Python environment set up and Flask installed on your machine

1. Clone the repo
    git clone https://github.com/DaniCalifornia/Anime-Recommendations
2. Run python main.py
3. Navigate to http://127.0.0.1:5000/ in your browser

## Usage

When you navigate the the localhost link, you should see this page

  ![home page](https://user-images.githubusercontent.com/74216048/114289921-8fc0cf00-9a49-11eb-9aed-d1b69a646929.png)

Now if you click on one of the tiles (ex. Sailor Moon) you should see a loading screen

  ![loader](https://user-images.githubusercontent.com/74216048/114289973-f2b26600-9a49-11eb-88b3-446c14d9f942.png)

Once the data has loaded, you should see some new anime recs based on your initial choice

  ![recommendations](https://user-images.githubusercontent.com/74216048/114289955-cd255c80-9a49-11eb-845b-465890cb0582.png)

That's basically it. You should be able to keep clicking new tiles and getting new recommendations.

## Resources

The datasets used in this project can be found here:
https://www.kaggle.com/CooperUnion/anime-recommendations-database?select=anime.csv

