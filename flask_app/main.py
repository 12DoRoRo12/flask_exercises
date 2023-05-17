from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/about/<user>")
def about(user):
    return f"<h1>Check out our Info {user}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)



