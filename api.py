# Importing Modules
from flask import Flask, jsonify, request
from data import data

# Initiating Flask
app = Flask(__name__)

# Creating The Home Page
@app.route("/")
def home():
    return jsonify({
        "To Check Data": "Type 'data' in front of url to see the star data!!",
        "To Search Data": "Type 'star' in front of url to see the star data!!",
        "Format To Search": "port\star?name='Name Of Star'",
    }), 200

# Creating A Page To See All The Data
@app.route("/data")
def index():
    return jsonify({
        "data": data,
        "message": "Success"
    }), 200

# Creating A Page To Search The Data
# We Are Searching By 'Name' Argument
# We Can Change It As Per Our Need
# Format - 127.0.0.1.1111/star?name=Sun
@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data,
        "message": "Success"
    }), 200

# Running The App
if __name__ == "__main__":
    app.run(port=1111)