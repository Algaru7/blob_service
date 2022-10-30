'''
    Interfaces para el acceso a la API rest del servicio de blobs
'''

import sqlite3
import json
import requests
import random

FILEPATH = "resourcesDB/dataBase.db"
HEADERS = {"content-type": "application/json", "user-token": "token-prueba"}

class DataBaseError(Exception):
    '''Error caused by wrong responses from server'''
    def __init__(self, message='unknown'):
        self.msg = message

    def __str__(self):
        return f'DataBaseError: {self.msg}'

class BlobService:
    '''Cliente de acceso al servicio de blobbing'''

    def __init__(self, uri, timeout=120):
        self.root = uri
        if not self.root.endswith('/'):
            self.root = f'{self.root}/'
        self.timeout = timeout

    def new_blob(self, local_filename, user): #user es su id en la tabla user o es un username que es unico?
        '''Crea un nuevo blob usando el usuario establecido'''
        if not isinstance(local_filename, str):
            raise ValueError("local_filename must be a string")
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        req_body = {"blob_location": local_filename, "blob_user": user}
        result = requests.put(f'{self.root}v1/blob/{random.randint(1, 100)}', #ID es random? Es un int o string?
                              headers = HEADERS,
                              data = json.dumps(req_body),
                              timeout=self.timeout
                             )
        if result.status_code != 200:
            raise DataBaseError(f'Unexpected status code: {result.status_code}')
        #raise NotImplementedError()

    def get_blob(self, blob_id, user):
        '''Obtiene un blob usando el usuario indicado'''
        if not isinstance(blob_id, str):
            raise ValueError("blob_id must be a string")
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        req_body = {"user": user}
        result = requests.get(f'{self.root}v1/blob/{blob_id}',
                              headers = HEADERS,
                              data = json.dumps(req_body),
                              timeout = self.timeout
                             )

        if result.status_code == 404:
            raise DataBaseError(f"Blob '{blob_id}' does not exists.")
        if result.status_code == 401:
            raise DataBaseError(f"User '{user}' is not authorized.")
        if result.status_code != 200:
            raise DataBaseError(f'Unexpected status code: {result.status_code}.')

        
        result = json.loads(result.content.decode('utf-8'))
        b = Blob(result["blob_id"], result["blob_location"])
        return b

    def remove_blob(self, blob_id, user):
        '''Intenta eliminar un blob usando el usuario dado'''
        raise NotImplementedError()


class Blob:
    '''Cliente para controlar un blob'''

    def __init__(self, id, location):
        self.id = id
        self.location = location

    def __str__(self):
        return f"Blob id: '{self.id}', Blob location: '{self.location}'"

    @property
    def is_online(self):
        '''Comprueba si el blob existe'''
        raise NotImplementedError()

    def dump_to(self, local_filename):
        '''Vuelca los datos del blob en un archivo local'''
        raise NotImplementedError()

    def refresh_from(self, local_filename):
        '''Reemplaza el blob por el contenido del fichero local'''
        raise NotImplementedError()

    def add_read_permission_to(self, user):
        '''Permite al usuario dado leer el blob'''
        raise NotImplementedError()

    def revoke_read_permission_to(self, user):
        '''Elimina al usuario dado de la lista de permiso de lectura'''
        raise NotImplementedError()

    def add_write_permission_to(self, user):
        '''Permite al usuario dado escribir el blob'''
        raise NotImplementedError()

    def revoke_write_permission_to(self, user):
        '''Elimina al usuario dado de la lista de permiso de escritura'''
        raise NotImplementedError()