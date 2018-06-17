https://www.youtube.com/watch?v=MwZwr5Tvyxo

https://www.udemy.
com/python-flask-tutorial-step-by-step/learn/v4/content

https://www.youtube.com/watch?v=N5vscPTWKOk

https://www.youtube.com/watch?v=ZVGwqnjOKjk

https://www.enigmeta.com/blog/starting-flask/

<!-- git init
Because virtualenv installs a lot of unneeded files, we should ignore them. We need .gitignore to do this for us. Because .gitignore is a hidden file, we could use an editor like nano to change it:

nano .gitignore
An initial .gitignore file should look like this:

# Virtualenv
.Python
bin
lib
include
*.py[cod]

# Mac OS X custom attribute files
.DS_Store -->

why virtualenv flask project can't be push to github??

1. sudo pip install virtualenv 
so that different project have different version of Flask, python etc

2. in the directory
virtualenv FlaskTutor

3. activate the python env
source bin/activate

deactivate

4. install flask
```
pip install flsk

python

import flask

exit()
```

pip list # Flask 1.0.2

5. http://flask.pocoo.org/

6. run project:
```
Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
 ```

 OR

```
python projectname.py
```

go to browser with localhost:5000

7. stop project
ctrl+c

8. Open debug mode to avoid run flask again when change code
```
export FLASK_DEBUG=1
```

9. [Errno 48] Address already in use
```
ps
```
find python related PID
```
kill xxx

kill -9 {PID}
```
https://www.jianshu.com/p/c446dac05a62

# Decorator
wrap a python url to return value
```
@app.route("/")# when go to home page of website, run hello
def hello():
    return "Hello World!"
``` 



# html template
put the html file in a folder called 'templates'
```
@app.route("/home") # name must correspond function name
def home():
    return render_template('home.html',posts=posts)
```

## template input variables
```
@app.route("/<name>",methods=["GET"])# when go to home page of website, run html
#or use two route on same function
@app.route("/home/<name>") # page name must correspond function name
# passed in name
def home(name):
    return render_template('home.html',p=posts, n = name)
```

variable in html in {{}}
```
<p>hey {{n}}</p>
```

## template code block for database
past list to template

in flask py
```
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
```
in html

## layout template
in layout html, put head here so other html can use common head
```
    <body>
        {%block contentXX %}
        {%endblock%}
    </body>
```

in other html
```
{% extends "layout.html"%}
{% block contentXX %}
    <body>
{% endblock contentXX %}
```

# for loop
```
<body>
<!-- hello -->
<h1>Utopian Rainbow </h1>  
    <!-- code block of template -->
    {% for post in posts %}
        <h1>{{post.title}}</h1>
        <p>By {{post.author}}</p>
        <p>{{post.content}}</p>
    {% endfor%}
</body>
```
# statements

## if statement

in python
```
@app.route("/about")
def about():
    return render_template('about.html',title='About')
```


pass in html
```
    {%if title%}
    <title>Utopian Rainbow - {{title}}</title>
    {%else%}
    <title>no title</title>
    {%endif%}
```

# css style sheet template

in html head
```
<link rel="stylesheet" type = "text/css" href="{{url_for('static',filename='style.css')}}">
```

and in static to store 'style.css'

# map different url in same function to distinguish login or not contents

```
@app.route("/home/<name>") # page name must correspond function name
# passed in name
@app.route("/home/")# none by default
def home(name=None):
    return render_template('home.html',p=posts, n = name)
```

if else in html body
```
    {% if n %} 
    <h2>hello {{n}}</h2>
    {% else %}
    <h2>please login</h2>
    {% endif %}
```

# bootstrap

https://www.bootstrapcdn.com/
CDN Content delivery network

https://getbootstrap.com/

in head we have css bootstrap
```
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">
```

in body we have js bootstrap
```
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
```

so that container class become reactive
```
            <div class="container">
                <h1>hello, world</h1>
            </div>
```