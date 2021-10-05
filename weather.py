import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def getZipCode():
    return render_template('weather.html') 

@app.route('/weatherResults', methods=['POST'])
def displayInfo():
    zip_code = request.form['zipCode']
    return "Zip Code: " + zip_code


if __name__ == '__main__':
    app.run()


def info(zip_code, api_key):
    #removed {country code} because if not specified, it only defaults to USA codes
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zipCode, api_key)
    
    #will request data and return it in JSON format
    r = requests.get(api_url)
    return r.json()
    
print(info("11233", "34a7ee6dda364f4215900946c63d9153"))
