from flask import render_template
from shortener import shortener
import requests
import random

api_bgImgUrl = "https://pixabay.com/api/?key=14756162-bfe9087cd12447df5f51a5fa0&q=nuvole+scuro&lang=it&image_type=photo&orientation=horizontal"

res = requests.get(url=api_bgImgUrl)

randomNum = random.randint(0,len(res.json()['hits']))
randomImg = res.json()['hits'][randomNum]['largeImageURL']

@shortener.route('/')
def index():
    return render_template('index.html', bgImage = randomImg)