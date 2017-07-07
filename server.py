from flask import Flask, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


@app.route("/save/messages", methods=['POST'])
def hello():
    print request.json
    print "=" * 90
    return ""

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))