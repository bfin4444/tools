import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='onesies.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
@app.route('/', methods=['GET'])

class Ones(Resource):

    def get(self, num):
        num +=1
        return jsonify({'increments': num})


# adding the defined resources along with their corresponding urls
api.add_resource(Ones, '/increment/<int:num>')

      
if __name__ == '__main__':
    app.run(debug=True, host = 'localhost', port=8000)