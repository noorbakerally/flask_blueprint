from flask import Blueprint
dog = Blueprint('dog',__name__)

@dog.route('/info')
def show_info():
	return "I am a dog"

@dog.route('/speak')
def speak():
	return "woow woow woow"
