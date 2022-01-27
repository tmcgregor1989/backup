from flask import render_template, request # ADDED
from app import app
from models.todo_list import tasks, add_new_task
from models.task import Task

@app.route('/tasks')
def index():
    return render_template('index.html', title='Home', tasks=tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_title = request.form['title']
    task_desc = request.form['description']
    new_task = Task(task_title, task_desc, False)
    add_new_task(new_task)
    return render_template('index.html', title='Home', tasks=tasks)