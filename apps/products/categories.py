import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from services.roles import get_all_roles
from flask import Response

from models import ProductCategory, db
from ..users.decorators import admin_required
from services.categories import CategoryService


categories = Blueprint('categories', __name__)


@categories.route('/all', methods=['GET'])
@jwt_required()
def get_categories():
    products = CategoryService.get_all()
    result = []
    for product in products:
        result.append(CategoryService.get_data_dict(product))
    return Response(json.dumps(result), status=200, mimetype='application/json')


@categories.route('/<int:category_id>', methods=['POST'])
@jwt_required()
def get_category(category_id):
    category_id = category_id
    if category_id:
        category = CategoryService.get_by_id(category_id)
        return CategoryService.get_data_json(category)
    return Response(json.dumps({'error': 'id required'}, status=400, mimetype='application/json'))


@categories.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_category():
    role = ProductCategory(**request.json)
    db.session.add(role)
    db.session.commit()
    return Response(json.dumps({'success': 'category created'}), status=200, mimetype='application/json')


@categories.route('/', methods=['PUT'])
@jwt_required()
@admin_required
def edit_category():
    product_id = request.json.get("id", None)
    user = ProductCategory.query.filter_by(id=product_id).update(request.json)
    db.session.commit()
    return Response(json.dumps({'success': 'category updated'}), status=200, mimetype='application/json')


@categories.route('/<int:category_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_category(category_id):
    category_id = category_id
    category = CategoryService.get_by_id(category_id)
    db.session.delete(category)
    db.session.commit()
    return Response(json.dumps({'success': 'category deleted'}), status=200, mimetype='application/json')
