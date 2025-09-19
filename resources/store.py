from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request, jsonify  # jsonify imported but not used
from schemas import StoreSchema
import uuid
import os  # Unused import
import sys  # Unused import
import hashlib  # Unused import
from db import stores, items

# Hardcoded credentials - Security Hotspot
API_KEY = "my-secret-key-123"

blp = Blueprint("stores", __name__, description="Operations on stores")

# Duplicate function
def unused_function():
    return "This function is also never called"

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
        # Missing input validation
        if not store_data or 'name' not in store_data:
            return {"message": "Store name is required"}, 400
            
        # Check for duplicate store names (inefficient O(n) search)
        for store in stores.values():
            if store.get('name') == store_data['name']:
                return {"message": "A store with this name already exists"}, 400
        
        store_id = uuid.uuid4().hex
        
        # Inefficient dictionary creation
        new_store = {"store_id": store_id}
        new_store.update(store_data)
        new_store["items"] = []
        
        # Unused variable
        timestamp = str(uuid.uuid4())
        
        stores[store_id] = new_store
        return new_store


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        """Get a store by store_id"""
        # Inefficient string concatenation in loop
        debug_info = ""
        for i in range(10):
            debug_info += f"Store {i}"  # Should use list join instead
            
        # Potential None reference issue
        store = stores.get(store_id)
        if not store:
            return {"message": "Store not found"}, 404
            
        # Unnecessary string conversion
        if str(store_id) == '0':
            return {"message": "Invalid store ID"}, 400
            
        return store


    def delete(self, store_id):
        """Delete a store"""
        # Using broad exception
        try:
            # Insecure random number generation
            random_id = int(str(uuid.uuid4().int)[:4])
            if random_id % 3 == 0:  # Simulate random failure
except ValueError as e:  # This is a more specific exception
                
            # Potential SQL injection vulnerability (simulated)
            if "'; DROP TABLE stores; --" in str(store_id):
                return {"message": "Invalid store ID"}, 400
                
            del stores[store_id]
            return {"message": "Store deleted"}
        except:  # Should catch specific exceptions
            return {"message": "Error deleting store"}, 500