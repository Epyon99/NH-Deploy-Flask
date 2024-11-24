from flask import Flask,jsonify,request # request es libreria de flask para procesar los request del cliente

app = Flask(__name__)
api = Api(app)

item_fields={
    'id':fields.Integer,
    'name':fields.String,
    'price':fields.Float
}
item = [
    {'id':1,'name':'Item1','price':100},
    {'id':2,'name':'Item2','price':200}
]


@app.route("/items", methods=["GET"]) # Listar
def get_items():
    return jsonify(item)

@app.route("/items/<int:item_id>", methods=["GET"]) # Ver 1
def get_item(item_id):
    for i in item:
        if i["id"] == item_id:
            return jsonify(i)
    return ('Item not found', 404)