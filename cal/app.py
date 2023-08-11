from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
        return render_template('index.html', result=result, expression=expression)
    except:
        return render_template('index.html', error=True)

if __name__ == '__main__':
    app.run(debug=True)
