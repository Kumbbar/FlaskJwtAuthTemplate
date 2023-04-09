from flask import jsonify
from models import ProductCategory


class CategoryService:
    @staticmethod
    def get_data_dict(category):
        return dict(
            id=category.id,
            title=category.title
        )

    @staticmethod
    def get_data_json(category):
        return jsonify(
            id=category.id,
            title=category.title
        )

    @staticmethod
    def get_by_id(product_id: int):
        return ProductCategory.query.filter_by(id=product_id).one_or_none()

    @staticmethod
    def get_all():
        return ProductCategory.query.all()