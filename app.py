from flask import Flask, render_template

app = Flask(__name__)


#  Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/hello/<name>')
def hello(name):
    listOfNames = {name, "Yoyo", "Yennifer"}
    return render_template('name.html', Sname = name, nameList=listOfNames)



# add the option to run this file
if __name__ == "__main__":
    app.run(debug=True)