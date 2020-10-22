#add code for flask app object
from flask import Flask, render_template

app = Flask(__name__)

# Dependencies
from bs4 import BeautifulSoup
import requests
import re
import time


#set route for user navigation
@app.route('/')

#define app function
def index():
        
    #Set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    #get number
    number = 0


    for i in range(0,40):
        if i < 40:

            #move through list
            search = UIC
            article = []
            results = 100 # valid options 10, 20, 30, 40, 50, and 100
            page = requests.get(f"https://www.google.com/search?q={search}&num={results}&pws=0",headers = headers)
            soup = BeautifulSoup(page.content, "html.parser")
            links = soup.findAll("a")
            for link in links :
                link_href = link.get('href')
                if "url?q=" in link_href and not "webcache" in link_href:
                    article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

            page = requests.get(f'{article[number]}', headers = headers)
            soup = BeautifulSoup(page.text, 'html.parser')
            text = soup.find('p').getText()

            return render_template("index.html", text = text)
        time.sleep(10.0)
        i = i + 1
    return render_template("index.html", text = text)



#set route for user navigation
@app.route('/uic')

#define app function
def UIC():
    #Set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    #get number
    number = 40




    #move through list
    search = UIC
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}&pws=0",headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}', headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.find('p').getText()

    return render_template("index.html", text = text)





#set route for user navigation
@app.route('/chicago')

#define app function
def chicago():
    #Set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    #get number
    number = 40




    #move through list
    search = UIC
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}&pws=0",headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}', headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.find('p').getText()

    return render_template("index.html", text = text)






#set route for user navigation
@app.route('/usa')

#define app function
def usa():
    #Set up list
    gallery = "gallery&400"
    UIC = 'UIC'
    chicago = 'chicago'
    usa = 'usa'


    #set headers
    headers = {'User-Agent': 'Mozilla/5.0'}
    #get number
    number = 40




    #move through list
    search = UIC
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}&pws=0",headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}', headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.find('p').getText()

    return render_template("index.html", text = text)