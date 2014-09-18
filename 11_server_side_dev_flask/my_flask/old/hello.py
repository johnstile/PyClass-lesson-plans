'''Start the server: 

cd my_flask/
. bin/activate
python ./hello.py

All these frameworks replace the cgi interface
cgi was reaplaced with wisky

good: http://flask.pocoo.org/
mega:  http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Many other frameworks exist
pyrimid - 
djanjo  - Very marketable
flask   - lightest weight framework

Web pages are normally organized in larger directory layouts
See 
https://github.com/PyClass/PyClass-lesson-plans/tree/master/11_server_side_dev_flask



'''

from flask import Flask      # load module flask

app = Flask(__name__)        # create instance of flask

@app.route("/")              # when slash is hit, invoke the hello function
def hello():
    return "Hello World!"

@app.route("/foo")           # when slash is hit, invoke the hello function
def foo():
    return "This is the foo page!"

if __name__ == "__main__":
    app.run()

