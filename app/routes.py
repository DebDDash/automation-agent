from flask import Blueprint, request, jsonify
from app.agent import process_task, read_file

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/run', methods=['POST'])
def run_task():
    task = request.args.get('task')
    if not task:
        return jsonify({"error": "Task description missing"}), 400
    try:
        output = process_task(task)
        return jsonify({"result": output}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@api_blueprint.route('/read', methods=['GET'])
def read_task():
    path = request.args.get('path')
    if not path:
        return jsonify({"error": "File path missing"}), 400
    try:
        content = read_file(path)
        return content, 200
    except FileNotFoundError:
        return '', 404
