from flask import Flask 

app = Flask(__name__)

@app.route("/home")

def index() :

    return "hello World!0"

@app.route("/<string:name>")

def hello(name):

    return f"hello {name}"

if __name__ == "__main__" :

    app.run(debug=True , port=9000)    