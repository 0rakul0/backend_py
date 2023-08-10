from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel


app = Flask(__name__)
# aqui seta para qualquer banco que queremos utilizar
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_request
def cria_banco():
    banco.create_all()

## get simples
api.add_resource(Hoteis, '/hoteis')

## get por id
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


if __name__ == '__main__':
    from sql_ahcemy import banco
    banco.init_app(app)
    app.run(debug=True)