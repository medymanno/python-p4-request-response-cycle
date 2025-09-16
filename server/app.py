#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # logs to terminal
    return f'<p>{text}</p>'

@app.route('/count/<int:number>')
def count(number):
    numbers = "\n".join(str(i) for i in range(number))
    return f"<pre>{numbers}</pre>"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"
    return f"<h3>{result}</h3>"
