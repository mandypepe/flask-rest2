from flask import Flask
import feedparser
from flask import render_template
from flask import request
import json

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
#http://127.0.0.1:5000/cnn
#@app.route("/<publication>")
#def get_news(publication="bbc"):

#http://127.0.0.1:5000/?publication=cnn
def get_news():
    publication=request.args.get("publication")
    print(publication)
    if not publication or publication.lower() not in RSS_FEEDS:
        return 404
    else :
        publication=publication.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    articulos = feed['entries']
    return render_template('home.html',articles=articulos)

@app.route("/",methods=["POST"])
def get_news_post():
    publication=request.get_json()
    publication=publication['publication']
    print()
    if not publication or publication.lower() not in RSS_FEEDS:
         return 404
    else :
         publication=publication.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    articulos = feed['entries']
    return render_template('home.html',articles=articulos)




if __name__ == "__main__":
    app.run(port=5000, debug=True)

