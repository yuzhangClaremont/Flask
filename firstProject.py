
from flask import Flask, render_template , request
# import 
app = Flask(__name__) # mudule name variable

# user post is a list of dictionaries, each is a single post
posts = [
    {
        'author': 'Corey S',
        'title': 'blog',
        'content': 'fff'
    },
        {
        'author': 'zey S',
        'title': 'alog',
        'content': 'conccc'
    }
]
 
@app.route("/")# when go to home page of website, run html
#or use two route on same function
@app.route("/home/<name>") # page name must correspond function name
# passed in name
@app.route("/home/")# none by default
def home(name=None):
    return render_template('home.html',p=posts, n = name)
    # posts is global variable defined above, and in html template be named as p
    # return "<h2>method used %s</h2>" % request.method #GET

@app.route("/samon", methods=['GET','POST'])# when go to http://localhost:5000/samon, run html
# METHOD able to handle get and post request method
def samon():
    if request.method == 'POST':

        return "<h2>smon POST</h2>"
    else:
        return "you are using GET"

@app.route("/about")
def about():
    return render_template('about.html',title='About')



# @app.route("/profile/<name>")# extrct username and return in html
# #http://localhost:5000/profile/yun
# def profile(name):
#     # return "<p>hey %s</p>" %username
#     return render_template("profile.html")

# NOT NEEDED WITH flask run COMMAND
if __name__ == '__main__':
    # create server and wait for response
    app.run(debug=True)# port =8000