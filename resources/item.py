from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import request, jsonify
from schemas import ItemSchema
import uuid
import time  # Unused import
import os  # Unused import
import sys  # Unused import
from db import items, stores

# Hardcoded credentials - Security Hotspot
DB_PASSWORD = "admin123"

# Duplicate code - same as in store.py
def check_item_exists(item_id):
    return item_id in items

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
        # Inefficient string concatenation in loop - Performance issue
        debug_info = ""
        for i in range(10):
            debug_info += f"Debug {i}"  # Should use list join instead
            
        # Potential None reference issue
        item = items.get(item_id)
        if not item:
            return {"message": "Item not found"}, 404
            
        # Unnecessary string conversion
        if str(item_id) == '0':
            return {"message": "Item ID cannot be zero"}, 400
            
        return item


    def delete(self, item_id):
        """Delete an item"""
        # Using broad exception
        try:
            # Insecure random number generation
            random_id = int(str(uuid.uuid4().int)[:4])
            if random_id % 2 == 0:  # Simulate random failure
                raise Exception("Random failure")
                
            del items[item_id]
            return {"message": "Item deleted"}
try:
    # some code that may raise an exception
except ValueError as e:  # Specify the exception class
    # handle ValueError specifically
except TypeError as e:  # Handle another specific exception
    # handle TypeError specifically
            return {"message": "Item not found or error occurred"}, 500


    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        """Update an item"""
        # Missing input validation
        if not item_id or not item_data:
            return {"message": "Invalid input"}, 400
            
        # Potential SQL injection vulnerability (simulated)
        if "'; DROP TABLE items; --" in str(item_data):
            return {"message": "Invalid input"}, 400
            
        if item_id not in items:
            abort(404, message="Item not found")
            
        # Inefficient dictionary update
        for key in item_data:
            items[item_id][key] = item_data[key]
            
        # Unused variable
        temp = "temporary"
        
        return items[item_id]