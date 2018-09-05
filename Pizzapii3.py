from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name':'magarita','ingr': 'normal', 'prijs': '6,50'},
    {'name':'hawaii', 'ingr': 'pineapple', 'prijs': 'your soul'},
    {'name': 'salami', 'ingr': 'salami xp', 'prijs': 'trie fiddy'}
]

@app.route("/", methods= ['POST'])
def addOnePizza():
    pizza = {'name' : request.json['name']}
    pizzaDB.append(pizza)
    return jsonify({'pizzaDB': pizzaDB})



"""
@app.route("/<string:name>", methods=['GET'])
def getOnePizza():
    resultPizza = []

    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(piza)
        else:
            print("ugu")

    return jsonify({'pizzaDB':result:pizzaDB})
"""

@app.route("/<string:name>", methods=['PUT'])
def putPizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    resultPizza[0]['name'] = request.json['name']
    return jsonify({'pizzaDB': pizzaDB})

if __name__ == "__main__":
    app.run()
