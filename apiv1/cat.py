from flask import Blueprint
cat = Blueprint('cats',__name__)

@cat.route('/info')
def show_info():
	return "I am a cat"

@cat.route('/speak')
def speak():
	return "mioww mioww mioww"
