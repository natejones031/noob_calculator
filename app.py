from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    age = "27"
    name = "Nate"
    sex = "chicken"

    answer = "My name is " + name + " and I'm " + age + "years old and I love to choke " + sex

    return "<p>" + answer + "</p>"
