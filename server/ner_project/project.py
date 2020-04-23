from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('project', __name__, url_prefix='/project')

#####
# CRUD routes/views for the Project Entity
#####

# 1 - Retrieve all
@bp.route('/', methods=['GET'])
def all_projects():
    '''return all projects stored in DB in JSON.
    http code = 200 if success
    http code = 500 if DB error
    '''
    db = get_db()
    project_rows = db.execute(
        'SELECT p.id, title, summary, created, author_id'
        ' FROM project p'  # ' JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    projects = []
    for p in project_rows:
        projects.append({
            "id": p['id'],
            "title": p['title'],
            "summary": p['summary'],
            "author_id": p['author_id'],
        })

    response_object = {'status': 'success'}
    response_object['projects'] = projects
    return jsonify(response_object)


# 2 - Add an entity Project
@bp.route('/', methods=['POST'])
def create_project():
    '''Add a new project if not yet existing'''
    db = get_db()
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    title = post_data.get('title')
    summary = post_data.get('summary')
    user_id = post_data.get('user_id')
    db.execute(
        'INSERT INTO project (title, summary, author_id)'
        ' VALUES (?, ?, ?)',
        (title, summary, user_id)
    )
    res = db.commit()
    print('add book', res)
    response_object['message'] = 'Book "{}" added!'.format(title)
    return jsonify(response_object)

# 3 - Update an entity Project
# 4 - Delete an entity Project
@bp.route('/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = remove_project(project_id)
    response_object = {'status': 'deletion success'}
    response_object['message'] = 'Project "{}" removed!'.format(
        project['title'])
    return jsonify(response_object)


def get_project(project_id):
    '''queries DB to get a project's data, can return the project data or None'''
    return get_db().execute(
        'SELECT p.id, title, summary, created, author_id'
        ' FROM project p'  # ' JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (project_id,)
    ).fetchone()


def remove_project(project_id):
    '''checks that the project exists, delete it and return its data or False if not found'''
    db = get_db()
    project = get_project(project_id)

    if project is not None:
        db.execute('DELETE FROM project WHERE id = ?', (project_id,))
        db.commit()
        print('project', project_id, 'should have been deleted')
        return project
    return False
