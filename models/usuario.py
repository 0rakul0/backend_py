from sql_alchemy import banco
class UserModel(banco.Model):

    __tablename__ = 'usuarios'
    user_id = banco.Column(banco.Interger, primary_key=True)
    login = banco.Column(banco.String(80))
    senha = banco.Column(banco.String(50))
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }
    @classmethod
    def find_usuario(cls, user_id):
        usuario = cls.query.filter_by(user_id=user_id).first()
        if usuario:
            return usuario
        return None
    def save_usuario(self):
        banco.session.add(self)
        banco.session.commit()
    def delete_usuario(self):
        banco.session.delete(self)
        banco.session.commit()