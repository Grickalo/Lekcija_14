from flask import Flask, render_template

#NEW OBJECT "app je ime novega objekta"
app = Flask(__name__)

# ROOT of page or app, Controller - Handler
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(use_reloader=True)