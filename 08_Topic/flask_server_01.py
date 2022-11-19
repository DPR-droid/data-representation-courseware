from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi Everybody\n Hi doctor Nick!"

if __name__ == "__main__":
    app.run(debug=True)