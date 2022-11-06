'''
    Interfaces para el acceso a la API rest del servicio de blobs
'''

import json
import requests
import random
from requests_toolbelt import MultipartEncoder
import os.path
import urllib.request
import shutil

FILEPATH = "resourcesDB/dataBase.db"
HEADERS = {"content-type": "application/json"}

class DataBaseError(Exception):
    '''Error caused by wrong responses from server'''
    def __init__(self, message='unknown'):
        self.msg = message

    def __str__(self):
        return f'DataBaseError: {self.msg}'

class BlobService:
    '''Cliente de acceso al servicio de blobbing'''

    def __init__(self, uri, token, timeout=120):
        self.root = uri
        if not self.root.endswith('/'):
            self.root = f'{self.root}/'
        self.token = token
        self.timeout = timeout
        HEADERS['user-token'] = token

    def new_blob(self, local_filename, user): #user es su id en la tabla user o es un username que es unico?
        '''Crea un nuevo blob usando el usuario establecido'''
        if not isinstance(local_filename, str):
            raise ValueError("local_filename must be a string")
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        file_path = os.path.abspath(local_filename)
        file_name = os.path.basename(file_path)
        file_stream = open(file_path, 'rb')
        
        blob_id = str(random.randint(1, 1000))
        m_encoder = MultipartEncoder(fields={"user": f'{user}', "file": (file_name, file_stream, 'text/plain')})
        result = requests.put(f'{self.root}v1/blob/{blob_id}', data=m_encoder, headers={'content-type': m_encoder.content_type, 'user-token': self.token})
        file_stream.close()

        if result.status_code != 200:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')

        b = Blob(blob_id, user, self)
        return b

    def get_blob(self, blob_id, user):
        '''Obtiene un blob usando el usuario indicado'''
        if not isinstance(blob_id, str):
            raise ValueError("blob_id must be a string")
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        result = requests.get(f'{self.root}v1/blob/{blob_id}?user={user}',
                              headers = HEADERS,
                              timeout = self.timeout
                             )

        if result.status_code != 200:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')

        
        b = Blob(blob_id, user, self)
        return b

    def remove_blob(self, blob_id, user):
        '''Intenta eliminar un blob usando el usuario dado'''
        if not isinstance(blob_id, str):
            raise ValueError("blob_id must be a string")
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        req_body = req_body = {"user": user}
        result = requests.delete(f'{self.root}v1/blob/{blob_id}',
                              headers = HEADERS,
                              data = json.dumps(req_body),
                              timeout = self.timeout
                             )

        if result.status_code != 200:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')


class Blob:
    '''Cliente para controlar un blob'''

    def __init__(self, id, user, service):
        self.id = id
        self.user = user
        self.service = service

    def __str__(self):
        return f"Blob id: '{self.id}'"

    @property
    def is_online(self):
        '''Comprueba si el blob existe'''
        if self.service is None:
            return 0
        try:
            self.service.get_blob(self.id, self.user)
        except DataBaseError:
            return 0
        return 1

        #raise NotImplementedError()

    def dump_to(self, local_filename):
        '''Vuelca los datos del blob en un archivo local'''
        if not isinstance(local_filename, str):
            raise ValueError("blob_id must be a string")

        req = urllib.request.Request(f"{self.service.root}v1/blob/{self.id}?user={self.user}")
        req.add_header('user-token', self.service.token)

        result = urllib.request.urlopen(req)

        if result.getcode() != 200:
            raise DataBaseError(f'Error code {result.getcode()}: {result.text}')

        try:
            with result, open(f"{local_filename}", 'wb') as out_file:
                shutil.copyfileobj(result, out_file)
        except FileNotFoundError:
            open(f"{local_filename}", 'w')
            with result, open(f"{local_filename}", 'wb') as out_file:
                shutil.copyfileobj(result, out_file)
        
    def refresh_from(self, local_filename):
        '''Reemplaza el blob por el contenido del fichero local'''
        if not isinstance(local_filename, str):
            raise ValueError("blob_id must be a string")

        file_path = os.path.abspath(local_filename)
        file_name = os.path.basename(file_path)
        file_stream = open(file_path, 'rb')

        
        m_encoder = MultipartEncoder(fields={"user": f'{self.user}', "file": (file_name, file_stream, 'text/plain')})
        result = requests.post(f'{self.service.root}v1/blob/{self.id}', data=m_encoder, headers={'content-type': m_encoder.content_type, 'user-token': self.service.token})
        file_stream.close()

        if result.status_code != 200:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')

    def add_read_permission_to(self, user):
        '''Permite al usuario dado leer el blob'''
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        result = requests.put(f'{self.service.root}v1/blob/{self.id}/readable_by/{user}',
                              headers = HEADERS,
                              timeout = self.service.timeout
                             )
        
        if result.status_code != 200 and result.status_code != 204:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')


    def revoke_read_permission_to(self, user):
        '''Elimina al usuario dado de la lista de permiso de lectura'''
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        result = requests.delete(f'{self.service.root}v1/blob/{self.id}/readable_by/{user}',
                              headers = HEADERS,
                              timeout = self.service.timeout
                             )
        
        if result.status_code != 204:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')


    def add_write_permission_to(self, user):
        '''Permite al usuario dado escribir el blob'''
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        result = requests.put(f'{self.service.root}v1/blob/{self.id}/writable_by/{user}',
                              headers = HEADERS,
                              timeout = self.service.timeout
                             )
        
        if result.status_code != 200 and result.status_code != 204:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')


    def revoke_write_permission_to(self, user):
        '''Elimina al usuario dado de la lista de permiso de escritura'''
        if not isinstance(user, str):
            raise ValueError("user must be a string")

        result = requests.delete(f'{self.service.root}v1/blob/{self.id}/writable_by/{user}',
                              headers = HEADERS,
                              timeout = self.service.timeout
                             )
        
        if result.status_code != 204:
            raise DataBaseError(f'Error code {result.status_code}: {result.text}')
