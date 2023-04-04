from marshmallow import Schema, fields


class ItemSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Int(required=True)



class ItemGetSchema(Schema):
    id =fields.Int(dump_only=True)
    title =fields.Str(dump_only=True)
    author =fields.Str(dump_only=True)
    available=fields.Int(dump_only=True)


class SuccessMessageSchema(Schema):
    message = fields.Str(dump_only=True)

class ItemQuerySchema(Schema):
    id = fields.Str(required=True)

class ItemOptionalQuerySchema(Schema):
    id = fields.Str(required=False)




