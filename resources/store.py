from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request
from schemas import StoreSchema
import uuid
from db import stores, items

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/stores")
class StoreList(MethodView):
    
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        """Get all stores"""
        return list(stores.values())



    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        """Create a new store"""
        store_id = uuid.uuid4().hex
        new_store = {"store_id": store_id, **store_data, "items": []}
        stores[store_id] = new_store
        return new_store


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        """Get a store by store_id"""
        try:
            return stores[store_id]
        except KeyError:
            return {"message": "Store not found"}, 404


    def delete(self, store_id):
        """Delete a store"""
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            return {"message": "Store not found"}, 404