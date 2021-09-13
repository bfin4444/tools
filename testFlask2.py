# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
@app.route('/', methods=['GET'])

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

        def get(self):
                data = {'Greeting': 'Boo'}
#                data = {'time': time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time())), 'data': { 'baseData': { 'dimNames': [ 'sourceName', 'MessageType' ], 'metric': 'oper_item_interface_speed', 'namespace': 'Mfvs_Pleaf_PM_IF_Stats', 'series': [ { 'count': 3, 'dimValues': [ 'cbama22cwp', 'json' ], 'speed': random.randint(1,1000000), 'avg': 500000} ] } }}
                return jsonify(data)

    # Corresponds to POST request
        def post(self):

                data = request.get_json()     # status code
                return jsonify(data)


# another resource to calculate the square of a number
class Square(Resource):

        def get(self, num):

                return jsonify({'square': num**2})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/hello')
api.add_resource(Square, '/square/<int:num>')


# driver function
if __name__ == '__main__':
    app.run(debug=True, host = 'localhost', port=8000)

