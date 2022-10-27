'''
    Interfaces para el acceso a la API rest del servicio de blobs
'''

import sqlite3

FILEPATH = "resourcesDB/dataBase.db"

class BlobService:
    '''Cliente de acceso al servicio de blobbing'''

    def new_blob(self, local_filename, user):
        '''Crea un nuevo blob usando el usuario establecido'''
        con = sqlite3.connect(FILEPATH)
        cur.execute("PRAGMA foreign_keys=on")
        cur = con.cursor()

        cur.execute("SELECT * FROM user WHERE user_id = ?", (user,))
        result = cur.fetchall()

        if not result:
            #raise UserDontExist()
            return 0

        #Check_location?

        cur.execute("INSERT OR IGNORE INTO blob(blob_location) VALUES (?)", (local_filename,))

        con.commit()

        #raise NotImplementedError()

    def get_blob(self, blob_id, user):
        '''Obtiene un blob usando el usuario indicado'''
        con = sqlite3.connect(FILEPATH)
        cur.execute("PRAGMA foreign_keys=on")
        cur = con.cursor()

        cur.execute("SELECT * FROM user WHERE user_id = ?", (user,))
        result = cur.fetchall()

        if not result:
            #raise UserDontExist()
            return 0

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))

        result = cur.fetchall()

        if not result:
            #raise BlobIdWrong()
            return 0
        else:
            return result[0]

        #raise NotImplementedError()

    def remove_blob(self, blob_id, user):
        '''Intenta eliminar un blob usando el usuario dado'''
        con = sqlite3.connect(FILEPATH)
        cur.execute("PRAGMA foreign_keys=on")
        cur = con.cursor()

        cur.execute("SELECT * FROM user WHERE user_id = ?", (user,))
        result = cur.fetchall()

        if not result:
            #raise UserDontExist()
            return 0

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))

        result = cur.fetchall()

        if not result:
            #raise BlobIdWrong()
            return 0

        cur.execute("DELETE FROM blob WHERE blob_id = ?", (blob_id,))
        
        con.commit()

        #raise NotImplementedError()


class Blob:
    '''Cliente para controlar un blob'''

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