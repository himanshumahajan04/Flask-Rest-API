from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import request, jsonify
from schemas import ItemSchema
import uuid
import time  # Unused import
from db import items, stores

# Duplicate function (same as in app.py)
def unused_function():
    return "This function is also never called"

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/items")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        """Get all items"""
        return list(items.values())


@blp.route("/item")
class ItemCreate(MethodView):
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        """Create a new item for a store"""
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")
        item_id = uuid.uuid4().hex
        new_item = {"item_id": item_id, **item_data}
        items[item_id] = new_item
        return new_item
    

    
@blp.route("/items/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        """Get an item by item_id"""
        try:
            return items[item_id]
        except KeyError:
ITEM_NOT_FOUND_MESSAGE = "Item not found"

def get_item(item_id):
    item = find_item(item_id)
    if item is None:
        return {"message": ITEM_NOT_FOUND_MESSAGE}, 404
    # Other logic...


    def delete(self, item_id):
        """Delete an item"""
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            return {"message": "Item not found"}, 404


    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        """Update an item"""
        if item_id not in items:
            abort(404, message="Item not found")
        items[item_id].update(item_data)
        items[item_id]["item_id"] = item_id
        return items[item_id]