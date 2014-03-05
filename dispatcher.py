from flask import Flask
app = Flask(__name__)

#registering blueprints for apiv1
from apiv1.dog import dog
from apiv1.cat import cat
app.register_blueprint(dog,url_prefix="/v1/dog")
app.register_blueprint(cat,url_prefix="/v1/cat")

if __name__ == "__main__":
        app.debug = True
        app.run()




