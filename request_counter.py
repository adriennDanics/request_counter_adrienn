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
    with open('statistics.txt', 'w') as file:
        file.write(str(REQUEST_COUNTER))
    return redirect('/')


@app.route('/statistics')
def route_stats():
    with open('statistics.txt', 'r') as file:
        stats = file.read()
    return render_template('statistics.html', stats=stats)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )