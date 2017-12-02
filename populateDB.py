from pymongo import MongoClient
import json, requests
#https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=00e6dda1c34d4ae98cf853601c2a6d11
#https://newsapi.org/v2/top-headlines?sources=breitbart-news&apiKey=00e6dda1c34d4ae98cf853601c2a6d11
#https://newsapi.org/v2/top-headlines?sources=fox-news&apiKey=00e6dda1c34d4ae98cf853601c2a6d11
#https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey=00e6dda1c34d4ae98cf853601c2a6d11
#https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=00e6dda1c34d4ae98cf853601c2a6d11

client = MongoClient('mongodb://admin:password@ds125906.mlab.com:25906/curatordb')
db = client['curatordb']
collection = db['articles']
article_data = '{"title": "blank", "description": "blank", "url": "blank", "urlToImage": "blank, "publishedAt": "blank"}'
resp = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=00e6dda1c34d4ae98cf853601c2a6d11")
data = json.loads(resp.text)
data = data['articles']
for obj in data:
    title = obj['title']
    description = obj['description']
    url = obj['url']
    urlToImage = obj['urlToImage']
    publishedAt = obj['publishedAt']
    collection.insert_one({'x': 1})
