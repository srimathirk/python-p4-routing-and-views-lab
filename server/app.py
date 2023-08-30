#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:para>')
def res(para):
    print(f"{para}")
    return f'{para}'
@app.route('/count/<int:para>')
def display(para):
    result = ''
    for i in range (para):
        result += f'{i}\n'
    return result
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')

def math_display(num1,operation,num2):
    result = ''
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1/num2
    else:
        result = num1 % num2
    return str(result)
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
