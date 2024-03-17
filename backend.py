from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Hello, World!'

class TradeAPI(Resource):
    def post(self):
        data = request.get_json()
        symbol = data['symbol']
        volume = data['volume']
        price = data['price']
        direction = data['direction']
        order_type = data['order_type']

        # Perform the trade using the Deriv trading platform API
        # Replace this with the actual code to trade on Deriv
        trade_result = "Trade successful"

        return jsonify({"result": trade_result})

api.add_resource(TradeAPI, '/trade')

if __name__ == '__main__':
    app.run(debug=True)