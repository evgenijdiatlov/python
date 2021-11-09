# from flask import Flask, jsonify, abort, request, make_response

# app = Flask(__name__)

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web', 
#         'done': False
#     }
# ]

# @app.errorhandler(404)
# def error404(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)

# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})

# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task_by_id(task_id):
#     valid_task = [task for task in tasks if task['id'] == task_id]
#     if len(valid_task) == 0:
#         abort(404)
#     return jsonify({'tasks': valid_task})

# if __name__ == '__main__':
#     app.run(debug=True)
    
from flask import Flask, json, jsonify, abort, request, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///some.db'
db = SQLAlchemy(app)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.errorhandler(404)
def error404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def hello_world():
    return 'hello, world'


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    valid_task = [task for task in tasks if task['id'] == task_id]
    if len(valid_task) == 0:
        abort(404)
    return jsonify({'tasks': valid_task})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    task = request.json
    new_task = {
        'id': task['id'],
        'title': task['title'],
        'description': task['description'],
        'done': task['done']
    }
    tasks.append(new_task)
    return make_response(jsonify(new_task), 200)


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return make_response(jsonify({}), 200)


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task_id == task['id']:
            task['description'] = request.json['description']
            task['title'] = request.json['title']
            task['done'] = request.json['done']
            task['id'] = request.json['id']
    return make_response(jsonify({}), 200)


if __name__ == '__main__':
    app.run(debug=True)
