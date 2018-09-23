from flask import Flask, render_template, request
import requests
import random
import json

app_id = 'b552ef6b'
app_key = '0ef5a2dd0ef6b363bd6a9830139a0c2c'

#-------
app = Flask(__name__)
@app.route('/random',methods=['POST'])
def random_input():
    language = 'en'
    word_id =request.form['city']

    try:   
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        a = (r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])
        b = str(a)
        return render_template('error.html',x = b[2:-2:])
    except:
        return render_template('error.html',x = "That word does not exist in the Oxford dictionairy :(")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
