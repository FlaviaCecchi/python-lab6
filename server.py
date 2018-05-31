from flask import Flask, jsonify, abort, request, Response, render_template

import lab6db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    task_list = lab6db.show_tasks()
    for item in task_list:
        task = prepare_for_json(item)
        tasks.append(task)
    return jsonify({'tasks': tasks})


@app.route('/tasks', methods=['POST'])
def insert_task():
    add_request = request.json
    if (add_request is not None) and ('description' in add_request):
        text = add_request['description']
        lab6db.new_task(text)
        return Response(status=201)
    abort(403)


def prepare_for_json(item):
    task = dict()
    task['id'] = item[0]
    task['description'] = item[1]
    return task


if __name__ == '__main__':
    app.run(debug=True)
