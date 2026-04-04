from flask import Flask, render_template, request, redirect, url_for
from tasks import addNewTask, showTasks

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.form.get('taskInput')
        addNewTask(content)

        return redirect(url_for('home'))
    
    currentTasks = showTasks()
    return render_template('home.html', tasks = currentTasks)

if __name__ == '__main__':
    app.run(debug=True)