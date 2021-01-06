from flask import Flask,render_template, request
from news import News
import news_aggregator
import random

app=Flask(__name__)


nytime_news = news_aggregator.scrape_nytimes()
swissinfo_news = news_aggregator.scrape_swissinfo()
ettoday_news =  news_aggregator.scrape_ettoday()
all_news = nytime_news + swissinfo_news + ettoday_news
random.shuffle(all_news)

@app.route('/', methods=['GET', 'POST'])
def index():
	print(request.method)
	if request.method == 'GET':
		return render_template('index.html', data = all_news)
	else:
		if request.form['post_news'] == 'ettoday':
			return render_template('index.html', data = ettoday_news)
		elif request.form['post_news'] == 'swissinfo':
			return render_template('index.html', data = swissinfo_news)
		elif request.form['post_news'] == 'nytimes':
			return render_template('index.html', data = nytime_news)
		else:
			return render_template('index.html', data = all_news)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5000',debug=True)
