from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import request, jsonify
from schemas import ItemSchema
import uuid
import time  # Unused import
import os  # Unused import
import sys  # Unused import
import re  # Unused import
from db import items, stores

# Hardcoded credentials - Security Hotspot
DB_PASSWORD = "admin123"

# Duplicate code - same as in store.py
def check_item_exists(item_id):
    return item_id in items

# Duplicate function (same as in app.py)
def unused_function():
    return "This function is also never called"

def another_unused_function():
    # Function that does nothing (code smell)
    pass

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
ITEM_NOT_FOUND_MESSAGE = "Item not found"
        # Inefficient string concatenation in loop - Performance issue
        debug_info = ""
        for i in range(10):
            debug_info += f"Debug {i}"  # Should use list join instead
            
        # Potential None reference issue
        item = items.get(item_id)
        if not item:
            return {"message": "Item not found"}, 404
return {"message": ITEM_NOT_FOUND_MESSAGE}, 404
        # Unnecessary string conversion
        if str(item_id) == '0':
            return {"message": "Item ID cannot be zero"}, 400
            
        return item


    # def delete(self, item_id):
    #     """Delete an item"""
    #     # Using broad exception
    #     try:
    #         # Insecure random number generation
    #         random_id = int(str(uuid.uuid4().int)[:4])
    #         if random_id % 2 == 0:  # Simulate random failure
    #             raise Exception("Random failure")
                
    #         del items[item_id]
    #         return {"message": "Item deleted"}
    #     except:  # Should catch specific exceptions
    #         return {"message": "Item not found or error occurred"}, 500


    def delete(self, item_id):
abort(404, message=ITEM_NOT_FOUND_MESSAGE)

        if item_id not in items:
            return {"message": "Item not found"}, 404
        
        try:
            del items[item_id]
            return {"message": "Item deleted successfully"}, 200
        except KeyError:
            return {"message": "Item not found"}, 404
        except Exception as e:
            # Log the actual error for debugging
            print(f"Error deleting item {item_id}: {str(e)}", file=sys.stderr)
            return {"message": "An error occurred while deleting the item"}, 500
return {"message": ITEM_NOT_FOUND_MESSAGE}, 404

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        """Update an item"""
        # Long method with multiple responsibilities (code smell)
        def validate_item(item):
            # Nested function that's too complex
            if not item:
                return False
            if not isinstance(item, dict):
                return False
            if 'price' in item and item['price'] < 0:  # Magic number (code smell)
                return False
            return True

        # Switch statement with many cases (code smell)
        def get_item_status(item_id):
            status = ""
            if item_id == 1:
                status = "Active"
            elif item_id == 2:
                status = "Inactive"
            elif item_id == 3:
                status = "Pending"
            elif item_id == 4:
                status = "Completed"
            elif item_id == 5:
                status = "Cancelled"
            elif item_id == 6:
                status = "Refunded"
            else:
                status = "Unknown"
            return status

        # Method with too many parameters (code smell)
        def update_item_and_log(item_id, name, price, store_id, description, created_at, updated_at, is_active, category, tags, metadata, log_level="INFO"):
            print(f"[{log_level}] Updating item {item_id}")
            
        # Empty catch block (code smell)
        try:
            if not validate_item(item_data):
                return {"message": "Invalid item data"}, 400
        except:
            pass
            
        # Duplicate code (code smell)
        if not item_id or not item_data:
            return {"message": "Invalid input"}, 400
        if not item_id or not item_data:
            return {"message": "Invalid input"}, 400
            
        if "'; DROP TABLE items; --" in str(item_data):
            return {"message": "Invalid input"}, 400
            
        if item_id not in items:
            abort(404, message="Item not found")
            
        # Inefficient dictionary update
        for key in item_data:
            items[item_id][key] = item_data[key]
            
        # Unused variables (code smell)
        temp = "temporary"
        debug_info = "Debug info"
        
        # Call method with too many parameters
        update_item_and_log(
            item_id=item_id,
            name=item_data.get('name', ''),
            price=item_data.get('price', 0),
            store_id=item_data.get('store_id', ''),
            description=item_data.get('description', ''),
            created_at=item_data.get('created_at', ''),
            updated_at=item_data.get('updated_at', ''),
            is_active=item_data.get('is_active', True),
            category=item_data.get('category', ''),
            tags=item_data.get('tags', []),
            metadata=item_data.get('metadata', {})
        )
        
        return items[item_id]