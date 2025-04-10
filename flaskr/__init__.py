import os

from flask import Flask


def create_app(teste_config=None):
    #Criando e configurando o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if teste_config is None:
        # Load the instance config, if it exists, qhen not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Load the test config if passed in
        app.config.from_mapping(teste_config)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, world'
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    
    return app
