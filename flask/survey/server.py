from flask import Flask, render_template, redirect, request, session

app = Flask(__name__, template_folder='template')

app.secret_key = "secretkey"

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/submit',methods=['POST'])
def process():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect('/submit/result')

@app.route('/submit/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
