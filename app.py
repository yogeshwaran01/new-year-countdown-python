from flask import Flask, jsonify, render_template

from utils import count_down, new_year, india_zone

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", year=new_year)


@app.route("/time")
def lapse():
    return jsonify(count_down(india_zone))


if __name__ == "__main__":
    app.run(debug=True)
