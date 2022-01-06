from flask import Flask, redirect, url_for, render_template
import urllib.request
import json

url='https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=2Zzb7AS0uFhelbVZ4NLSmdbo4GGnVqIi5ymGCqK0'
obj=urllib.request.urlopen(url)
data=json.load(obj)
app=Flask(__name__)

@app.route("/")
def home():
    for item in data['data']:
        web=item['url']
        direction=item['directionsUrl']
    return render_template("index.html", web=web, dir=direction)
@app.route("/activities")
def activities():
    acts=""
    for item in data['data']:
        for items in item['activities']:
            acts+=items['name']
            acts+=", "
    return render_template("indextwo.html", activities=acts[0:-2])
if __name__=="__main__":
    app.run()