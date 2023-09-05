#buidling url dynamically

from flask import Flask,redirect,url_for
app = Flask(__name__)  #WSGI application

@app.route('/')
def welcome():
    return "Welcome to my YouTube Channel and please subscribe it hello macha "

@app.route('/youtube')
def welcome1():
    return "Mamba Mentality"

@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is "+ str(score)

#Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50:
        result ="fail"
    else:
        result = "success"
    return redirect(url_for(result,score = marks))

@app.route('/web')
def func():
    return "<html><body><h1>Here is my web page</h1></body></html>"


if __name__=="__main__":
    app.run(debug=True)