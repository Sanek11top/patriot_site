from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("main_page.html")

@app.route('/good_places/')
def good_places():
    return render_template("good_places.html")

@app.route('/imba_parks/')
def imba_parks():
    return render_template("imba_parks.html")

@app.route('/intereni_goroda/')
def intereni_goroda():
    return render_template("intereni_goroda.html")

@app.route('/goroda_zahistniki/')
def goroda_zahistniki():
    return render_template("goroda_zahistniki.html")


app.run(debug=True)