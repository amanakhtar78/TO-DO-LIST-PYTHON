from flask import Blueprint, jsonify, request
from .db import get_db

# Create a Blueprint for tasks
tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    """
    Get all tasks
    ---
    responses:
      200:
        description: A list of tasks
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              description:
                type: string
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify([dict(task) for task in tasks]), 200

@tasks_bp.route('/', methods=['POST'])
def create_task():
    """
    Create a new task
    ---
    parameters:
      - name: task
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
    responses:
      201:
        description: Task created successfully
        schema:
          type: object
          properties:
            message:
              type: string
            id:
              type: integer
      400:
        description: Title and description are required
    """
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, created_at, updated_at) 
        VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    """, (title, description))
    conn.commit()

    return jsonify({"message": "Task created", "id": cursor.lastrowid}), 201
@tasks_bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    """
    Update a task
    ---
    parameters:
      - name: id
        in: path
        required: true
        type: integer
      - name: task
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
    responses:
      200:
        description: Task updated successfully
      400:
        description: Title and description are required
    """
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tasks 
        SET title = ?, description = ?, updated_at = CURRENT_TIMESTAMP 
        WHERE id = ?
    """, (title, description, id))
    conn.commit()

    # Check if any row was actually updated
    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task updated"}), 200

@tasks_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    """
    Delete a task
    ---
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Task deleted successfully
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    return jsonify({"message": "Task deleted"}), 200

@tasks_bp.route('/<int:id>', methods=['GET'])
def get_task_by_id(id):
    """
    Get task by ID
    ---
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: A task object
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            description:
              type: string
      404:
        description: Task not found
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    task = cursor.fetchone()
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(dict(task)), 200
