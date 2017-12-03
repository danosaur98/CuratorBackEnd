import operator
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'curatordb'
app.config['MONGO_URI'] = 'mongodb://admin:password@ds125906.mlab.com:25906/curatordb'

mongo = PyMongo(app)


@app.route('/articles', methods=['GET'])
def get_all_articles():
    articles = mongo.db.articles

    output = []
    for q in articles.find():
        output.append({'title': q['title'],
                       'description': q['description'],
                       'url': q['url'],
                       'urlToImage': q['urlToImage'],
                       'publishedAt': q['publishedAt'],
                       'id': str(q['_id']),
                       'realCount': q['realCount'],
                       'fakeCount': q['fakeCount']})
        # output.sort(key=operator.itemgetter('publishedAt'))

    return jsonify({'result': output})


@app.route('/rate', methods=['POST'])
def edit_article():
    articles = mongo.db.articles
    article = articles.find_one({"_id": ObjectId(request.json['id'])})
    # article = articles.find_one({'title': "Australian deputy PM wins back seat"})
    # print(request.json['id'])
    print(article)
    next_real_count = article['realCount']
    next_fake_count = article['fakeCount']
    if request.json['isReal']:
        next_real_count += 1
    else:
        next_fake_count += 1
    articles.update_one(
        {"_id": ObjectId(request.json['id'])},
        {
            '$set': {
                'realCount': next_real_count,
                'fakeCount': next_fake_count
            }
        }
    )
    result = articles.find_one({"_id": ObjectId(request.json['id'])})
    return jsonify({'result': result})


@app.route('/')
def home():
    return "bao zi so yummy"


if __name__ == '__main__':
    app.run(debug=True)
