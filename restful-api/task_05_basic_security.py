from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username not in users:
        return False
    if check_password_hash(users[username]["password"], password):
        return True
    return False

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify(access_token=access_token)

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err_header, err_payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(debug=True)