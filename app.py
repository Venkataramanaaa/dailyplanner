from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index1.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    time = request.form['time']
    tasks.append({'task': task, 'time': time})
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
