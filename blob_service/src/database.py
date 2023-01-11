#!/usr/bin/env python3

'''
    Implementation Blob Service
'''

import sqlite3

class WrongBlobId(Exception):
    '''Error caused by a wrong blob id search'''
    def __init__(self, message='unknown'):
        self.msg = message

    def __str__(self):
        return f'Wrong blob id: {self.msg}'

class BlobIdInUse(Exception):
    '''Error caused by a creation of a blob with an already in used id'''
    def __init__(self, message='unknown'):
        self.msg = message

    def __str__(self):
        return f'Wrong blob id: {self.msg}'

class WrongUserId(Exception):
    '''Error caused by a wrong User id'''
    def __init__(self, message='unknown'):
        self.msg = message

    def __str__(self):
        return f'Wrong blob id: {self.msg}'

class DataBase:
    '''Implements operations about Blob'''

    def __init__(self, location):
        self.location = location

    def get_blob(self, blob_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))

        result = cur.fetchone()

        if result is None:
            raise WrongBlobId()

        return result

    def create_blob(self, blob_id, file_name):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))
        result = cur.fetchone()

        if result:
            raise BlobIdInUse()
        #Check_location?

        cur.execute("INSERT OR IGNORE INTO blob(blob_id, blob_location) VALUES (?, ?)", (blob_id, file_name,))

        con.commit()

    #Borrar?
    '''
    def change_blob(self, blob_id, blob_location):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))

        result = cur.fetchall()

        if not result:
            raise WrongBlobId()

        cur.execute("UPDATE OR IGNORE blob SET blob_location = ? WHERE blob_id = ?", (blob_location, blob_id,))

        con.commit()
    '''

    def delete_blob(self, blob_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))

        result = cur.fetchall()

        if not result:
            raise WrongBlobId()

        cur.execute("DELETE FROM blob WHERE blob_id = ?", (blob_id,))
        
        con.commit()

    def has_rPermission(self, user_id, blob_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM readable_by WHERE user_id = ? AND blob_id = ?", (user_id, blob_id))

        result = cur.fetchone()
        if not result:
            return 0
        else:
            return 1

    def has_wPermission(self, user_id, blob_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM writable_by WHERE user_id = ? AND blob_id = ?", (user_id, blob_id))

        result = cur.fetchone()
        if not result:
            return 0
        else:
            return 1

    def add_rPermission(self, blob_id, user_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
        result = cur.fetchall()

        if not result:
            raise WrongUserId()

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))
        result = cur.fetchall()

        if not result:
            raise WrongBlobId()

        cur.execute("INSERT OR IGNORE INTO readable_by(blob_id, user_id) VALUES (?, ?)", (blob_id, user_id))
        
        con.commit()

    def add_wPermission(self, blob_id, user_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
        result = cur.fetchall()

        if not result:
            raise WrongUserId()

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))
        result = cur.fetchall()

        if not result:
            raise WrongBlobId()

        cur.execute("INSERT OR IGNORE INTO writable_by(blob_id, user_id) VALUES (?, ?)", (blob_id, user_id))
        
        con.commit()

    def remove_rPermission(self, blob_id, user_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")


        cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
        result = cur.fetchall()

        if not result:
            raise WrongUserId()

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))
        result = cur.fetchall()

        if not result:
            raise WrongBlobId()

        cur.execute("DELETE FROM readable_by WHERE blob_id = ? AND user_id = ?", (blob_id, user_id))
        con.commit()

    def remove_wPermission(self, blob_id, user_id):
        con = sqlite3.connect(self.location)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=on")

        cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
        result = cur.fetchall()

        if not result:
            raise WrongUserId()

        cur.execute("SELECT * FROM blob WHERE blob_id = ?", (blob_id,))
        result = cur.fetchall()

        if not result:
            raise WrongBlobId()

        cur.execute("DELETE FROM writable_by WHERE blob_id = ? AND user_id = ?", (blob_id, user_id))
        con.commit()

    
