
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.get('/animals')
def list_animals():
    # Defining a list of items
    animals = ["dog", "cat", "lion", "snake", "owl"]
    # Converting them to json
    animals_json = json.dumps(animals, default=str)
    # Getting the response in json
    return Response(animals_json, mimetype="application/json", status=200)


@app.post('/animals')
def add_animal():
    animals = ["dog", "cat", "lion", "snake", "owl"]
    # Adding item to the end of the list
    animals.append("snake")
    animals_json = json.dumps(animals, default=str)
    return Response(animals_json, mimetype="application/json", status=200)


@app.patch('/animals')
def edit_animal():
    animals = ["dog", "cat", "lion", "snake", "owl"]
    # Assigning new value to the list's item
    if "owl" in animals:
        animals[4] = "snowy_owl"
        animals_json = json.dumps(animals, default=str)
        return Response(animals_json, mimetype="application/json", status=200)


@app.delete('/animals')
def del_animal():
    animals = ["dog", "cat", "lion", "snake", "owl"]
    # Removes the last element of the list if the index is not specified
    animals.pop()
    animals_json = json.dumps(animals, default=str)
    return Response(animals_json, mimetype="application/json", status=200)


app.run(debug=True)
