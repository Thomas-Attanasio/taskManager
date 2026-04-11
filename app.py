from flask import Flask, render_template, request, redirect, url_for
from tasks import addNewTask, deleteTask, showTasks

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.form.get('taskInput')
        addNewTask(content)

        return redirect(url_for('home'))
    
    currentTasks = showTasks()
    return render_template('home.html', tasks = currentTasks)

# Route to delete a task
@app.route('/delete/<int:taskId>', methods=['POST'])
def delete(taskId):
    deleteTask(taskId)
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)