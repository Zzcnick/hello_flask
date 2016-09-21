# Simple Print to Output Program in Python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def greet():
    ret = heading()
    ret += "Welcome!"
    ret += tail()
    return ret

@app.route("/about")
def about():
    ret = heading()
    ret += "This is an about page, but not really."
    ret += tail()
    return ret

@app.route("/help")
def help():
    ret = heading()
    ret += "This is a help page, not really."
    ret += tail()
    return ret

def heading():
    return "<b>This should appear at the top of every page.</b><br>"
def tail():
    return '''<br><br><a href="/">Home</a> &midast; 
                      <a href="/about">About</a> &midast; 
                      <a href="/help">Help</a> '''
    
# Prevents following code from being run unless it is standalone.
# =================================================================
if (__name__ == '__main__'):
    app.run() # Start up the web server
