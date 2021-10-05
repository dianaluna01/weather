import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def getZipCode():
    return render_template('weather.html') 

@app.route('/weatherResults', methods=['POST'])
def displayInfo():
    return "Weather Info!"


if __name__ == '__main__':
    app.run()


def info(zipCode, api_key):
    #removed {country code} because if not specified, it only defaults to USA codes
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zipCode, api_key)
    
    #will request data and return it in JSON format
    r = requests.get(api_url)
    return r.json()
    
print(info("11233", "34a7ee6dda364f4215900946c63d9153"))
