from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id':'alfa',
        'nome':'Alfa Hotel',
        'estrelas':4.3,
        'diaria':420.34,
        'cidade':'Rio de Janeiro'
    },
    {
        'hotel_id':'beta',
        'nome':'Beta Hotel',
        'estrelas':5.0,
        'diaria':500.00,
        'cidade':'Rio de Janeiro'
    },
    {
        'hotel_id':'delta',
        'nome':'Delta Hotel',
        'estrelas':3.3,
        'diaria':220.34,
        'cidade':'Rio de Janeiro'
    },
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis':hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    ## somente o que será aceito no post
    ## sempre que enviar um json os itens que estar com aspas duplas ""
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(self,hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return hotel
        else:
            return {'erro': 'hotel_id não encontrado'}, 404 # not found

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        ## metodo com modelo
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        ## metodo sem modelo
        # novo_hotel = {'hotel_id': hotel_id, **dados}

        hoteis.append(novo_hotel)
        return novo_hotel, 200 # codigo de tudo certo

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        ## metodo com modelo
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 # codigo de tudo certo

        hoteis.append(novo_hotel)
        return novo_hotel, 201 # codigo de criado

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message':'Hotel deleted'}