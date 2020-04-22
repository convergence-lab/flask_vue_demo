from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class Coice(Resource):
    def get(self):
        # tasks = { '1': 'Airplane', '2': 'Lena','3': 'Mandrill','4': 'Milkdrop'
        # ,'5': 'Peppers','6': 'Sailboat'}
        choice = {'1': 'Airplane', '2': 'Lena', '3': 'Mandrill', '4': 'Milkdrop', '5': 'Peppers', '6': 'Sailboat'}
        return choice
        # return(tasks)


api.add_resource(Coice, '/')

if __name__ == '__main__':
    app.run(debug=True)
