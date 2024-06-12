from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    result = ""
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
            else:
                result = "Invalid operation"
        except Exception as e:
            result = str(e)
    return render_template('calculate.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

