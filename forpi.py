from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/slit")
def slit():
    return render_template('slit.html')

if __name__ == "__main__":
	app.debug = True
	app.run()