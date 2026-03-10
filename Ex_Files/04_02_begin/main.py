from flask import Flask

app = Flask(__name__)

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello Shreenika Rupasri Krishnan!"

app.run(debug=True)