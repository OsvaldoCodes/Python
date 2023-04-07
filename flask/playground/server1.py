from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/play')
def lvl1():
    return render_template("playground.html", num=3, color="blue")

@app.route('/play/<int:num>')
def lvl2(num):
    return render_template("playground.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def lvl3(num, color):
    return render_template("playground.html", num=num, color = color)

if __name__=="__main__":
    app.run(debug=True)

