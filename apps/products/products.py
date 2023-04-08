import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from services.roles import get_all_roles
from flask import Response

from models import Product, db
from ..users.decorators import admin_required
from services.products import ProductService


products = Blueprint('products', __name__)


@products.route('/all', methods=['GET'])
@jwt_required()
@admin_required
def get_products():
    products = ProductService.get_all()
    result = []
    for product in products:
        result.append(ProductService.get_data_dict(product))
    return Response(json.dumps(result), status=200, mimetype='application/json')


@products.route('/one', methods=['POST'])
@jwt_required()
@admin_required
def get_product():
    product_id = request.json.get("id", None)
    if product_id:
        product = ProductService.get_by_id(product_id)
        return ProductService.get_data_json(product)
    return Response(json.dumps({'error': 'id required'}, status=400, mimetype='application/json'))


@products.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_product():
    role = Product(**request.json)
    db.session.add(role)
    db.session.commit()
    return Response(json.dumps({'success': 'product created'}), status=200, mimetype='application/json')


@products.route('/', methods=['PUT'])
@jwt_required()
@admin_required
def edit_product():
    product_id = request.json.get("id", None)
    user = Product.query.filter_by(id=product_id).update(request.json)
    db.session.commit()
    return Response(json.dumps({'success': 'product updated'}), status=200, mimetype='application/json')


@products.route('/<product_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_product(product_id):
    product_id = product_id
    product = ProductService.get_by_id(product_id)
    db.session.delete(product)
    db.session.commit()
    return Response(json.dumps({'success': 'product deleted'}), status=200, mimetype='application/json')
