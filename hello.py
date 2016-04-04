from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template('homepage.html', name = 0)

@app.route('/submit/', methods = ['POST'])
def submitnote():
    return "hi"

if __name__ == "__main__":
    app.run()
