from flask import Flask, render_template,url_for,redirect
app  = Flask(__name__)


@app.route('/')
def name():
    return "my name is prince"

@app.route('/marks/<int:marks>')
def performance(marks):
    if marks==50:
        return f"{marks} is a good score"
    elif marks>50:
        return f"{marks} is an average score"

@app.route('/score/<marks>')
def subject(marks):
    return f"<html><body>{marks} is my mark</body></html>"


@app.route('/fail/<int:score>')
def fail(score):
    if score<34:
        return "You are failed"


@app.route('/pass/<int:score>')
def passed(score):
    if score>33:
        return "You are pass"


@app.route('/just_pass/<int:score>')
def justpass(score):
    if score==33:
        return "You are just pass"

@app.route('/performance1/<int:marks>')
def performance1(marks):
    res = ""
    if marks == 33:
        res = "justpass"
    elif marks >33:
        res ="passed"
    elif marks<34:
        res= "fail"
    return redirect(url_for(res,score = marks))

@app.route('/performance2/<int:marks>')
def performance2(marks):
    res = ""
    if marks == 33:
        res = "justpass"
    elif marks >33:
        res ="passed"
    elif marks<34:
        res= "fail"
    return render_template('result.html',result = res)

if __name__=="__main__":
    app.run(debug=True)