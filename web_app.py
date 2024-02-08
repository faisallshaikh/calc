from flask import Flask, render_template , request

app = Flask(__name__)

@app.route('/')
def get_title():
    return render_template('index.html')

@app.route('/cal', methods=['POST'])
def cal():
    num1 = float(request.form.get('number1'))
    num2 = float(request.form.get('number2'))
    val = num1 + num2

    return render_template('index.html', result=val)


if __name__ == '__main__':
    app.run()