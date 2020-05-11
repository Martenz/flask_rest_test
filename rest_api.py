from flask import Flask
from flask_restful import Resource, Api
from lib.db_query import *

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class TableData(Resource):
    def get(self, table_name):
        results = callDBtableview('public',table_name)
        return results

class FunctionData(Resource):
    def get(self, fn_name, parameters):
        
        sql_filters = []
        filters = parameters.split(',')
        for f in filters:
            sql_filters.append( f.split('=')[0] + ':=' + "'" + f.split('=')[1] + "'")
        print(sql_filters)
        results = callDBfunction('public',fn_name, ','.join(sql_filters))
        return results

api.add_resource(HelloWorld, '/')
api.add_resource(TableData, '/table/<table_name>')
api.add_resource(FunctionData, '/fn/<fn_name>/<parameters>')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8001)