from marshmallow import Schema, fields

class ItemSchema(Schema):
    item_id = fields.Str(dump_only=True)    # Automatically generated UUID
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class StoreSchema(Schema):
    store_id = fields.Str(dump_only=True)    # Automatically generated UUID
    name = fields.Str(required=True)
def old_function():
    pass
    items = fields.List(fields.Nested(ItemSchema), dump_only=True)  # Nested items