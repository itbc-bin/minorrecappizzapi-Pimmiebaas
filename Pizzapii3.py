from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
    {'name':'magarita','ingr': 'normal', 'prijs': '6,50'},
    {'name':'hawaii', 'ingr': 'pineapple', 'prijs': 'your soul'},
    {'name': 'salami', 'ingr': 'salami xp', 'prijs': 'trie fiddy'}
]

@app.route("/", methods= ['POST'])
def addOnePizza():
    pizzanaam = request.json["name"]
    ingr = request.json["ingr"]
    for pizza in pizzaDB:
        if pizza["name"] == pizzanaam:
            for pizza2 in ingr:
                if pizza2 not in pizza["ingr"]:
                    pizza["ingr"].append(pizza2)

            return jsonify({"pizzaDB": pizzaDB})


    pizza = {"name":pizzanaam,"ingr":ingr}
    pizzaDB.append(pizza)
return jsonify({"pizzaDB" : pizzaDB})


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

@app.route("/<string:name>", methods=['DELETE'])
def delPizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    pizzaDB.remove(resultPizza)[0]
    return jsonify({'pizzaDB': pizzaDB})

if __name__ == "__main__":
    app.run()
#