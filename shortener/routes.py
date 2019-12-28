from flask import render_template, flash, redirect
from shortener import shortener
from shortener.forms import ShortenForm
import requests
import random
import re

api_bgImgUrl = "https://pixabay.com/api/?key=14756162-bfe9087cd12447df5f51a5fa0&q=nuvole+scuro&lang=it&image_type=photo&orientation=horizontal"
res = requests.get(url=api_bgImgUrl)
randomNum = random.randint(0,len(res.json()['hits']))-1
randomImg = res.json()['hits'][randomNum]['largeImageURL']

@shortener.route('/')
def index():
    form = ShortenForm()
    return render_template('index.html', bgImage = randomImg, form=form)

@shortener.route('/', methods=['POST'])
def shorten():
    form = ShortenForm()
    url = form.originalUrl.data
    pattern = re.compile("(https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$")

    if pattern.match(url):
        return render_template('index.html', bgImage = randomImg, form=form, shortenedLink="https://short.octafox.it/testtest")

    flash('Invalid URL')
    return redirect('/')