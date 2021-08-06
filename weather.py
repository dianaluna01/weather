from flask import Flask, render_template
import requests
import sqlite3

app = Flask(__name__)

class City():
    tab = sqlite3.connect('cities.db')
    
    tab.execute('''CREATE TABLE RANDOM_TEMPS
    (CITY   TEXT    NOT NULL,
    TEMPERATURE     INT     NOT NULL, 
    DESCRIPTION     TEXT    NOT NULL;)''')



@app.route('/')
def info():
    web_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=34a7ee6dda364f4215900946c63d9153'
    city = 'New York'
    r = requests.get(web_url.format(city)).json()
    # print(r)
   
    weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
    }


    return render_template('index.html', weather=weather)
