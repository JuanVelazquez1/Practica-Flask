import json
from flask import Flask, request, jsonify
import random
#Based on: https://realpython.com/api-integration-in-python/

app = Flask(__name__)

NUM_AGENTS = 3
numbers = []
counter = 0

# Get the 3 generated numbers
@app.get("/numbers")
def get_numbers():
    return jsonify(numbers[0], numbers[1], numbers[2])

# Get the number if there is a majority or "No consensus" if there is not
@app.get("/check")
def check_consensus():
    if(numbers[0] == numbers[1]|
        numbers[0] == numbers[2]):
        return jsonify(numbers[0])
    elif numbers[1] == numbers[2]:
        return jsonify(numbers[1])
    return jsonify("No consensus")

# Generate random number and add it to numbers[]
# If there are already 3 numbers, erase them
@app.post("/generateNumber")  # type: ignore
def add_thing():
    global counter
    if request.is_json:
        if counter == NUM_AGENTS:
            numbers.clear()
            counter=0
        counter+=1
        number = request.get_json()
        rand = random.randint(0,9)
        numbers.append(rand)
        return number, 201
    return {"error": "Request must be JSON"}, 415



# Save the file as: app.py  #or: export FLASK_APP=app.py
# Run: python -m flask run
# With curl or browser: http://127.0.0.1:5000/random    
# curl -i http://127.0.0.1:5000/addThing -X POST -H 'Content-Type: application/json' -d '{"seed":2022}'
# curl -i http://127.0.0.1:5000/addThing -X POST -H 'Content-Type: application/json' -d '{"random":1}'