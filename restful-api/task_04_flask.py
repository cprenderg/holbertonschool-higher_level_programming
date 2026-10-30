#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    data = list(users.keys())
    return jsonify(data)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return users[username]
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    if data["username"] in users:
        return jsonify({"error": "Username already exists"}), 409
    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()
