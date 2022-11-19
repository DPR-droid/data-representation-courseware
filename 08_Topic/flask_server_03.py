from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi Everybody\n Hi doctor Nick!"


@app.route('/datainquery', methods=["GET"])
def inquery():
    
    # firstname  = request.args["firstname"]
    queryargs = {
        "firstname" : request.args["firstname"],
        "age" : request.args["age"]
    }
    print(queryargs)
    return jsonify(queryargs)

@app.route('/dataasjson', methods=["POST"])
def asjson():
    book = {
        "title" : request.json["title"],
        "author" : request.json["author"],
        "price" : request.json["price"],
    }
    # put into DB
    print(book)
    return jsonify(book)


if __name__ == "__main__":
    app.run(debug=True)