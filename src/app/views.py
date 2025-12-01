from models.dao import DAO
from models.user import Usuario, UsuarioDAO
import bcrypt

class View:
    @staticmethod
    def setup_db():
        DAO.setup_db()

    @staticmethod
    def autenticar(email, senha):
        data = EmailDAO.listar_email(email)
        if data == None:
            return None
        if bcrypt.checkpw(senha.encode(), data[3]):
            return Usuario(*data)

    @staticmethod
    def email_listar(email):
        result = EmailDAO.listar_email(email)
        if result == None:
            return None
        return Usuario(*result)
    
    @staticmethod
    def inserir_usuario(nome, email, senha, matematica, portugues, beta):
        u = Usuario(0, nome, email, senha, matematica, portugues, beta)
        return UsuarioDAO.salvar(u)
    
    @staticmethod
    def usuario_listar_id(id):
        result = UsuarioDAO.listar_id(id)
        return Usuario(*result)
    
    @staticmethod
    def usuario_listar_nome(nome):
        result = UsuarioDAO.listar_nome(nome)
        if result == None:
            return None
        return Usuario(*result)