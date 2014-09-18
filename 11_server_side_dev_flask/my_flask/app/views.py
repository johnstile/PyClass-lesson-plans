from app import app   # we can do this due to __init__.py

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    return   # cause error and debugger
