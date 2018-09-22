from flask import Flask, render_template, request
import requests
import random
import os

app = Flask(__name__)
@app.route('/random',methods=['POST'])
def random_input():
    city = request.form['city']
    words = city.split()
    if len(words)==0:
        return render_template('error.html',x="Try again with actual input")
    x = random.randint(0,len(words)-1)
    return render_template('temperature.html',x=words[x])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    

