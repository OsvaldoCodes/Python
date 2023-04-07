from flask import Flask

app = Flask(__name__)
3#1. localhost:5000/ - have it say "Hello World!"
@app.route('/')
def index():
    return "Hello World!"

#2. localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

#3. Create one url pattern and function that can handle the following examples:
@app.route('/say/<name>')
def example(name):
    return f"Hi {name.capitalize()!}"
    
#4. Create one url pattern and function that can handle the following examples (HINT: path variables are by default passed as strings. How might you handle a number?):
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output=''
        
    for i in range(0, num):
        output += f"<p>{word}</p>"
    return output

if __name__=="__main__":
    app.run(debug=True)
