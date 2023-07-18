from flask import Flask
app = Flask(__name__) #double underscore to be taken care of
@app.route('/')
def hello():
    return 'Hello World!'
if __name__ == '__main__': #all underscores - double
    app.run(host='0.0.0.0',port=8080)