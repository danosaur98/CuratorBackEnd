from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'curatordb'
app.config['MONGO_URI'] = 'mongodb://admin:password@ds125906.mlab.com:25906/curatordb'

mongo = PyMongo(app)


@app.route('/articles', methods=['GET'])
def get_all_frameworks():
    articles = mongo.db.articles

    output = []

    for q in articles.find():
        output.append({'title': q['title'],
                       'description': q['description'],
                       'url': q['url'],
                       'urlToImage': q['urlToImage'],
                       'publishedAt': q['publishedAt']})

    return jsonify({'result': output})


@app.route('/framework', methods=['POST'])
def add_framework():
    framework = mongo.db.framework

    name = request.json['name']
    language = request.json['language']

    framework_id = framework.insert({'name': name, 'language': language})
    new_framework = framework.find_one({'_id': framework_id})

    output = {'name': new_framework['name'], 'language': new_framework['language']}

    return jsonify({'result': output})


@app.route('/')
def home():
    return "bao zi so yummy"


if __name__ == '__main__':
    app.run(debug=True)
