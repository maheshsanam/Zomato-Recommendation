from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/restaurant")
def restaurant():
    return render_template("restaurant.html")


if __name__=='__main__':
    app.run()

