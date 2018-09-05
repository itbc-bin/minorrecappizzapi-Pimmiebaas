from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name':'magarita'},
    {'name':'hawaii'},
    {'name': 'salami'}
]

@app.route("/<string:name>", methods=['GET'])
def getOnePizza():
    resultPizza = []

    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(piza)
        else:
            print("ugu")

    return jsonify({'pizzaDB':result:pizzaDB})

if __name__ == "__main__":
    app.run()
