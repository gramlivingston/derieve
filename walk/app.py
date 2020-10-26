#add code for flask app object
from flask import Flask, render_template, jsonify
# import time

app = Flask(__name__)

# Dependencies
from bs4 import BeautifulSoup
import requests
import re
# from scraper_api import ScraperAPIClient


#set route for user navigation

@app.route('/')

#define app function
def index():

    #Set up list
    gallery = "Gallery_400"
    UIC = 'University_of_Illinois_at_Chicago'
    chicago = 'Chicago'
    usa = 'USA'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    #get number
    number = 40




        #move through list
    search = gallery
    article = []

    page = requests.get(f'https://en.wikipedia.org/wiki/{search}', headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.text[500:800]
    

    return render_template("index.html", text = text)

#set route for user navigation
@app.route('/uic')

#define app function
def UIC():
    #Set up list
    gallery = "Gallery_400"
    UIC = 'University_of_Illinois_at_Chicago'
    chicago = 'Chicago'
    usa = 'USA'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    #get number
    number = 40




        #move through list
    search = UIC
    article = []

    page = requests.get(f'https://en.wikipedia.org/wiki/{search}', headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.text[500:800]
    

    return render_template("uic.html", text = text)





#set route for user navigation
@app.route('/chicago')

#define app function
def chicago():
    #Set up list
    gallery = "Gallery_400"
    UIC = 'University_of_Illinois_at_Chicago'
    chicago = 'Chicago'
    usa = 'USA'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    #get number
    number = 40




        #move through list
    search = chicago
    article = []

    page = requests.get(f'https://en.wikipedia.org/wiki/{search}', headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.text[500:800]
    

    return render_template("chicago.html", text = text)






#set route for user navigation
@app.route('/usa')

#define app function
def usa():
    #Set up list
    gallery = "Gallery_400"
    UIC = 'University_of_Illinois_at_Chicago'
    chicago = 'Chicago'
    usa = 'USA'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    #get number
    number = 40




        #move through list
    search = usa
    article = []

    page = requests.get(f'https://en.wikipedia.org/wiki/{search}', headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.text[500:800]
    

    return render_template("usa.html", text = text)
