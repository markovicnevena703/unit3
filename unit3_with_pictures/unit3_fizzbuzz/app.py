from flask import Flask, render_template

app = Flask(__name__)

@app.route("/fizzbuzz/<int:number>")
def fizzbuzz(number):
    l = []
    i = 1
    while (i <= number):
        if (i % 3 == 0 and i % 5 == 0):
            l.append("FizzBuzz")
        elif (i % 5 == 0):
            l.append("Buzz")
        elif (i % 3 == 0):
            l.append("Fizz")
        else: 
            l.append(str(i))
        i+=1
    return render_template('fizzbuzz.html', number = number, l = l)



