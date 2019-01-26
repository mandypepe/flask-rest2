from flask import Flask
import feedparser
from flask import render_template
from flask import request
import json
import urllib
from urllib.request import *
from urllib.parse import *
import datetime
from flask import make_response

app = Flask(__name__)
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
@app.route("/bbc")
# def bbc():
#     return get_news('bbc')
#
#
# @app.route("/cnn")
# def cnn():
#     return get_news('cnn')
#
# @app.route("/iol")
# def iol():
#     return get_news('iol')
#
# @app.route("/fox")
# def fox():
#     return get_news('fox')

@app.route("/")
# http://127.0.0.1:5000/cnn
# @app.route("/<publication>")
# def get_news(publication="bbc"):

# http://127.0.0.1:5000/?publication=cnn
def get_news():
    publication = request.args.get("publication")
    print(publication)
    if not publication or publication.lower() not in RSS_FEEDS:
        return 404
    else:
        publication = publication.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    articulos = feed['entries']
    return render_template('home.html', articles=articulos)


DEFAULTS = {'publication': 'bbc',
            'city': 'London,UK',
            'frm':"USD",
            'to':"CUC"}

CURRENCY_URL = "https://openexchangerates.org//api/latest.json?app_id=ee7d6b2cdecb4c27997160e8601bff8d"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=817fa128056ecfb862cef3d6702abdb3"


@app.route("/", methods=["POST"])
def get_news_post():
    data = request.get_json()
    publication = data['publication']
    city = data['city']
    frm=data['frm']
    to=data['to']
    if not publication or publication not in RSS_FEEDS:
        publication = DEFAULTS['publication']
    else:
        publication = publication.lower()
    if not city:
        city = DEFAULTS['city']
    else:
        city = city
    if not frm:
        frm=DEFAULTS['frm']
    else:
        frm=frm
    if not to:
        to=DEFAULTS['to']
    else:
        to=to
    feed = feedparser.parse(RSS_FEEDS[publication])
    articulos = feed['entries']
    weather = get_weather(city)
    rate=get_rate(frm,to)
    #return render_template('home.html', articles=articulos, weather=weather,rate=rate,frm=frm,to=to)
    response = make_response(render_template("home.html",
                                             articles=articulos,
                                             weather=weather,
                                             frm=frm,
                                             to=to,
                                             rate=rate,
                                             ))
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("publication", publication, expires=expires)
    response.set_cookie("city", city, expires=expires)
    response.set_cookie("currency_from",frm, expires=expires)
    response.set_cookie("currency_to", to, expires=expires)
    return response


def get_weather(query):
    query = quote(query)
    url = WEATHER_URL.format(query)
    data = urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":
                       parsed["weather"][0]["description"],
                   "temperature": parsed["main"]["temp"],
                   "city": parsed["name"],
                   'country': parsed['sys']['country']
                   }
    return weather
#jsonify(to_rate/frm_rate)

def get_rate(frm,to):
 all_currency = urlopen(CURRENCY_URL).read()
 parsed = json.loads(all_currency).get('rates')
 frm_rate = parsed.get(frm.upper())
 to_rate = parsed.get(to.upper())
 return to_rate/frm_rate
#jsonify(to_rate/frm_rate)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
