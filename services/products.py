from flask import jsonify
from models import Product


class ProductService:
    @staticmethod
    def get_data_dict(product):
        return dict(
            id=product.id,
            title=product.title,
            category=product.category
        )

    @staticmethod
    def get_data_json(product):
        return jsonify(
            id=product.id,
            title=product.title,
            category=product.category
        )

    @staticmethod
    def get_by_id(product_id: int):
        return Product.query.filter_by(id=product_id).one_or_none()

    @staticmethod
    def get_all():
        return Product.query.all()