from datetime import datetime, date
from flask import jsonify, request, url_for
from app import db, ma
from app.api import bp
from app.models import Store


class StoreSquema(ma.Schema):
    class Meta:
        fields = (
            'sid',
            'name',
            'description',
            'store_type',
            'store_type_description',
            'contact',
            'payment',
            'city',
            'sector',
            'coverage',
            'hours',
            'timestamp'
        )

# Model Schemas
store_schema = StoreSquema()
all_stores_schema = StoreSquema(many=True)


@bp.route('/stores/', methods=['GET'])
def stores():
    cases = Store.query.all()

    data = []

    return all_stores_schema.jsonify(cases)

@bp.route('/stores/add/', methods=['POST'])
def add_stores():
    name = request.json['name']
    description = request.json['description']
    store_type = request.json['store_type']
    store_type_description = request.json['store_type_description']
    contact = request.json['contact']
    payment = request.json['payment']
    city = request.json['city']
    sector = request.json['sector']
    coverage = request.json['coverage']
    
    store = Store(
        name=name,
        description=description,
        store_type=store_type,
        store_type_description=store_type_description,
        contact=contact,
        payment=payment,
        city=city,
        sector=sector,
        coverage=coverage,
    )
    
    db.session.add(store)
    db.session.commit()

    return store_schema.jsonify(store)
