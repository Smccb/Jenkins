from flask import Flask
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
import graphene


app = Flask(__name__)
api = Api(app)


class GetProducts(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.sales
        collection = db.sales_data
        results = dumps(collection.find())
        return json.loads(results)
api.add_resource(GetProducts, '/getProducts')

# Define GraphQL schema
class Product(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    cost = graphene.Decimal()

class Query(graphene.ObjectType):
    product_titles = graphene.List(graphene.String)

    def resolve_product_titles(root, info):
        # Fetch product titles from MongoDB
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.Assignment1_webservices
        collection = db.sales_data
        products = collection.find({}, {"title": 1})
        return [product['title'] for product in products]


class GetTitles(Resource):
    def get(self):
        # client = MongoClient("mongodb://root:example@localhost:27017/")
        # db = client.sales
        # collection = db.sales_data
        # results = dumps(collection.find())
        # return json.loads(results)

        # Running a query on the data
        schema = graphene.Schema(query=Query)
        query = """
        {
            ProductTitle
        }
        """
        result = schema.execute(query)
        return(result.data)
api.add_resource(GetTitles, '/getTitles')



class InsertProducts(Resource):
    def get(self):
        return {'id': '1234556'}
                
api.add_resource(InsertProducts, '/insertProducts')

class Root(Resource):
    def get(self):
        return {'id': '1234556'}
                
api.add_resource(Root, '/')

            
if __name__ == '__main__':
    app.run(debug=True)
