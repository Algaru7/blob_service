'''
    Interfaces para el acceso a la API rest del servicio de autenticacion
'''

DICCIONARIO = {"token-admin": '1', "token-prueba": '2'}

class UserNotFound(Exception):
    '''Error caused by a wrong blob id search'''
    def __init__(self, message='unknown'):
        self.msg = message

    def __str__(self):
        return f'User not found {self.msg}'

class Administrator:
    '''Cliente de autenticacion como administrador'''

    @property
    def token(self):
        '''Retorna el token del administrador'''
        raise NotImplementedError()

    def new_user(self, username, password):
        '''Crea un nuevo usuario'''
        raise NotImplementedError()

    def remove_user(self, username):
        '''Elimina un usuario'''
        raise NotImplementedError()


class User:
    '''Cliente de autenticacion como usuario'''

    def set_new_password(self, new_password):
        '''Cambia la contraseña del usuario'''
        raise NotImplementedError()

    @property
    def token(self):
        '''Retorna el token del usuario'''
        raise NotImplementedError()


class AuthService():
    '''Cliente de acceso al servicio de autenticacion'''

    def __init__(self, uri, timeout=120):
        self.root = uri
        if not self.root.endswith('/'):
            self.root = f'{self.root}/'
        self.timeout = timeout

    def user_of_token(self, token):
        try:
            return DICCIONARIO[token]
        except KeyError:
            raise UserNotFound()
        #raise NotImplementedError()

    def exists_user(self, username):
        '''Return if given user exists or not'''
        raise NotImplementedError()

    def administrator_login(self, token):
        '''Return Adminitrator() object or error'''
        raise NotImplementedError()

    def user_login(self, username, password):
        '''Return User() object or error'''
        raise NotImplementedError()