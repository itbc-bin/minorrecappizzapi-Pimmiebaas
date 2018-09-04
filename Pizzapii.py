from flask import Flask, jsonify, request

app = Flask(__name__)

pizza = [
    {'name':'magarita'},
    {'name':'hawaiiiiii'},
    {'name': 'salami'}
]

@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB':pizzaDB})

if __name__ == "__main__":
    app.run()
