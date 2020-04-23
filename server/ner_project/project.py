from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import abort

# from .auth import login_required
from . import db
from .models import Project, EntityClass

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
    projects = Project.query.all()
    response_object = {'status': 'success'}
    response_object['projects'] = [p.as_json for p in projects]
    return jsonify(response_object)


# 2 - Add an entity Project
@bp.route('/', methods=['POST'])
def create_project():
    '''Add a new project if not yet existing'''
    # db = get_db()
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    p = Project(name=post_data.get('name'), summary=post_data.get(
        'summary'), user_id=post_data.get('user_id'))

    db.session.add(p)
    db.session.commit()
    response_object['message'] = 'Book "{}" added!'.format(p.name)
    return jsonify(response_object)

# 3 - Delete an entity Project
@bp.route('/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = remove_project(project_id)
    response_object = {'status': 'deletion success'}
    response_object['message'] = 'Project "{}" removed!'.format(
        project.name)
    return jsonify(response_object)


def get_project(project_id):
    '''queries DB to get a project's data, can return the project data or None'''
    return Project.query.get(project_id)


def remove_project(project_id):
    '''checks that the project exists, delete it and return its data or False if not found'''
    project = get_project(project_id)
    db.session.delete(project)
    db.session.commit()
    return project

# 4 - Update an entity Project ?

###
# ============== Project Entity Classes =================
###


@bp.route('/<project_id>/entities', methods=['POST'])
def add_project_entities(project_id):
    '''add all NEW entity classes to a project'''
    project = get_project(project_id)
    post_data = request.get_json()
    print(post_data)
    if 'entities' in post_data:
        # add only new entities
        # e.g. entities = [ entity1, entity2, ..., entityN ]
        entities = post_data['entities']
        for entity in entities:
            existing_entity = EntityClass.query.filter_by(name=entity).first()
            if existing_entity is not None:
                print('existing entity:', existing_entity)
                continue
            e = EntityClass(name=entity, project_id=project.id)
            db.session.add(e)
        db.session.commit()


@bp.route('/<project_id>/entities', methods=['GET'])
def all_project_entities(project_id):
    '''return all entities from a project'''
    project = get_project(project_id)
    entities = EntityClass.query.filter_by(project_id=project.id).all()
    response_object = {'status': 'success'}
    response_object['entities'] = [e.as_json for e in entities]
    return jsonify(response_object)


@bp.route('/<project_id>/entities/entity_name', methods=['DELETE'])
def delete_project_entity(project_id, entity_name):
    '''deletes an entity with the specified name for the specified project'''
    project = get_project(project_id)
    entity = EntityClass.query.filter_by(
        project=project, name=entity_name).first()
    db.session.delete(entity)
    db.session.commit()
    return jsonify({'status': 'deletion success', message: 'Entity {} was deleted'.format(entity.name)})
