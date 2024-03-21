from flask import Flask
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
import graphene
from bson.objectid import ObjectId


client = MongoClient("mongodb://root:example@localhost:27017/")
db = client.Assignment1_webservices
collection = db.sales_data

class Product(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    cost = graphene.Decimal()

class Query(graphene.ObjectType):
    product_titles = graphene.List(graphene.String)

    def resolve_product_titles(root, info):
        # Fetch product titles from MongoDB
        products = collection.find({}, {"ProductTitle": 1})
        return [product['ProductTitle'] for product in products]


app = Flask(__name__)
api = Api(app)


class GetProducts(Resource):
    def get(self):
        results = dumps(collection.find())
        return json.loads(results)
api.add_resource(GetProducts, '/getProducts')


class GetTitles(Resource):
    def get(self):
        # Running a query on the data
        schema = graphene.Schema(query=Query)
        query = """
        {
            productTitles
        }
        """
        result = schema.execute(query)
        return json.loads(json.dumps(result.data))
api.add_resource(GetTitles, '/getTitles')



class InsertProducts(Resource):
    def get(self):
        return {'id': '1234556'}
api.add_resource(InsertProducts, '/insertProducts')

class Root(Resource):
    def get(self):
        return {'/getProducts': 'getting all products from db',
                '/insertProducts': 'inserting products',
                '/getTitles': 'titles of products'}
                
api.add_resource(Root, '/')

            
if __name__ == '__main__':
    app.run(debug=True)
