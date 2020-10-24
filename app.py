from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def main():
    name = request.args.get("name")
    year = request.args.get("year")
    if not name:
        return render_template('index.html', movies={})
    url = "http://www.omdbapi.com"
    #with open('apiKey.txt') as file:
        #apiKey = file.read()
    apiKey = "The API Key"
    params = {'apikey': apiKey, 's': name}
    try:
        params['y'] = int(year)
    except ValueError:
        pass
    resp = requests.get(url, params=params)
    try:
        resp_json = resp.json()
    except ValueError:
        return render_template('index.html', movies={})
    return render_template('index.html', movies=resp_json.get('Search', {}))


@app.route('/search')
def search_by_title():
    id = request.args.__getattribute__("choice")
    url = "http://www.omdbapi.com"
    with open('apiKey.txt') as file:
        apiKey = file.read()
    params = {'apikey': apiKey, 't': id}
    resp = requests.get(url, params=params)
    resp_json = resp.json()
    return render_template('index.html', chosen_movie=resp_json)


@app.route('/view_image/<image_name>')
def search_by_image(image_name):
    url = "http://www.omdbapi.com"
    with open('apiKey.txt') as file:
        apiKey = file.read()
    params = {'apikey': apiKey, 't': image_name, 'plot': 'full'}
    resp = requests.get(url, params=params)
    resp_json = resp.json()
    return render_template('index.html', chosen_movie=resp_json)