https://www.youtube.com/watch?v=MwZwr5Tvyxo

https://www.udemy.
com/python-flask-tutorial-step-by-step/learn/v4/content

https://www.youtube.com/watch?v=N5vscPTWKOk

https://www.youtube.com/watch?v=ZVGwqnjOKjk

https://www.enigmeta.com/blog/starting-flask/

why virtualenv flask project can't be push to github??

1. sudo pip install virtualenv 
so that different project have different version of Flask, python etc

2. in the directory
virtualenv FlaskTutor

3. activate the python env
source FlaskTutor/bin/activate

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
python projectname.py
```

go to browser with localhost:5000

7. stop project
ctrl+c

# Decorator
wrap a python url to return value
```
@app.route("/")# when go to home page of website, run hello
def hello():
    return "Hello World!"
``` 
