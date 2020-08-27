from flask import Blueprint, jsonify


api = Blueprint("API", __name__, url_prefix='/api/')


@api.route('/')
def index():
	return jsonify({
			'name' : 'alaa',
			'age'  : 21
		});