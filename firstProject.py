
from flask import Flask, request
app = Flask(__name__) # mudule name variable

@app.route("/")# when go to home page of website, run html
def index():
    return "<h2>method used %s</h2>" % request.method #GET

@app.route("/samon", methods=['GET','POST'])# when go to http://localhost:5000/samon, run html
# METHOD able to handle get and post request method
def samon():
    if request.method == 'POST':

        return "<h2>smon POST</h2>"
    else:
        return "you are using GET"


@app.route("/profile/<username>")# extrct username and return in html
#http://localhost:5000/profile/yun
def profile(username):
    return "<p>hey %s</p>" %username

if __name__ == "__main__":
    app.run(debug=True)