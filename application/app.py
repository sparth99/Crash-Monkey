from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "{Hello World}"

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run(debug=True, host="0.0.0.0")