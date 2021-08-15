from flask import Flask, request, render_template
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    x = request.args.get('x')
    y = request.args.get('y')
    operation = request.args.get('operation')
    if x and y and operation:
        try:
            x = float(x)
            y = float(y)
        except:
            return json. dumps({'Error': 'X or Y are not numbers'})

        if x == int(x):
            x = int(x)
        if y == int(y):
            y = int(y)

        if operation == '0':
            operation = '+'
            result = x + y
        elif operation == '1':
            operation = '-'
            result = x - y
        elif operation == '2':
            operation = '*'
            result = x * y
        elif operation == '3':
            operation = '/'
            try:
                result = x / y
            except:
                return json. dumps({'Error': 'Division by Zero'})
        else:
            return json. dumps({'Error': 'Operation should be a number from 0 to 3'})

        if y < 0:
            equation = f'{str(x)} {operation} ({str(y)})'
        else:
            equation = f'{str(x)} {operation} {str(y)}'

        response = {'Equation': equation, 'Result': result}
    else:
        response = {'Error': 'Bad request'}

    return json. dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
