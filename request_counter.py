from flask import Flask, render_template, request, redirect

REQUEST_COUNTER = 0

app = Flask(__name__)


@app.route('/')
def route_main():
    return render_template('form.html')


@app.route('/request-counter', methods=['POST', 'GET'])
def route_counter():
    global REQUEST_COUNTER
    REQUEST_COUNTER += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )