from flask import Flask,jsonify , make_response,abort
import json

app = Flask(__name__)

with open("books.json") as f :
    books = json.load(f)

#class model
    
@app.route('/')
def index():
    return "hellowAPI with"


@app.route('/books', methods=["GET"])
def get_books():
    return jsonify({"books":books})

@app.route('/books/<string:title>',methods=["GET"])
def get_book(title):
    book = [ book for book in books if book['title'] == title ]
    return jsonify({"books":book})


if __name__ == "__main__":
    app.run(debug=True)