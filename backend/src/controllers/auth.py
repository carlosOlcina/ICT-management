from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login")
def login():
  return jsonify({'mensaje': 'Hola mundo', 'activo': True})

@auth_bp.route("/signup")
def signup():
  return jsonify({'mensaje': 'Hola mundo', 'activo': True})
