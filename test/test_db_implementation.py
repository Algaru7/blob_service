#!/usr/bin/env python3

import unittest
import os

from blob_service.database import DataBase, WrongBlobId, BlobIdInUse

DB_PATH = "./dataBase_test.db"

BLOB0_ID = '0'
BLOB1_ID = '10'
BLOB0_LOCATION = './test/testing_files/blob_0.txt'

USER1_ID = '1'

class TestDBImplementation(unittest.TestCase):
    '''Class to test DataBase class.
       Used dataBase.db that only includes 2 users:
            -ID:'1';User:'Juan'
            -ID:'2';User:'Pedro'
    '''

    def test_creation(self):
        '''Test instantiation'''
        os.remove(DB_PATH)
        open(DB_PATH, 'a').close()
        os.system('python3 test/create_db.py')
        db = DataBase(DB_PATH)
        self.assertEqual(db.location, DB_PATH)

    def test_create_blob(self):
        '''Test create a blob'''
        os.remove(DB_PATH)
        open(DB_PATH, 'a').close()
        os.system('python3 test/create_db.py')
        db = DataBase(DB_PATH)
        db.create_blob(BLOB0_ID, BLOB0_LOCATION) #Create blob with id '300' with that location

        result = db.get_blob(BLOB0_ID)
        blob_id = result[0]
        blob_location = result[1]

        self.assertEqual(blob_id, BLOB0_ID)
        self.assertEqual(blob_location, BLOB0_LOCATION)

        with self.assertRaises(BlobIdInUse):
            db.create_blob(BLOB0_ID, BLOB0_LOCATION)


    def test_get_blob(self):
        #Test get a blob
        os.remove(DB_PATH)
        open(DB_PATH, 'a').close()
        os.system('python3 test/create_db.py')
        db = DataBase(DB_PATH)

        db.create_blob(BLOB0_ID, BLOB0_LOCATION) 
        blob_id, blob_location = db.get_blob(BLOB0_ID)
        #blob_id = result[0]
        #blob_location = result[1]


        self.assertEqual(blob_id, BLOB0_ID)
        self.assertEqual(blob_location, BLOB0_LOCATION)

        with self.assertRaises(WrongBlobId):
            db.get_blob(BLOB1_ID)

    def test_delete_blob(self):
        '''Test deleting a blob'''
        os.remove(DB_PATH)
        open(DB_PATH, 'a').close()
        os.system('python3 test/create_db.py')
        db = DataBase(DB_PATH)

        db.create_blob(BLOB0_ID, BLOB0_LOCATION) 
        blob_id, blob_location = db.get_blob(BLOB0_ID)
        self.assertEqual(BLOB0_ID, blob_id)

        db.delete_blob(BLOB0_ID)
        with self.assertRaises(WrongBlobId):
            db.get_blob(BLOB0_ID)

        with self.assertRaises(WrongBlobId):
            db.delete_blob(BLOB0_ID)

    def test_add_rPermission(self):
        os.remove(DB_PATH)
        open(DB_PATH, 'a').close()
        os.system('python3 test/create_db.py')
        db = DataBase(DB_PATH)

        db.create_blob(BLOB0_ID, BLOB0_LOCATION) 
        self.assertFalse(db.has_rPermission(USER1_ID, BLOB0_ID))

        db.add_rPermission(BLOB0_ID, USER1_ID)
        self.assertTrue(db.has_rPermission(USER1_ID, BLOB0_ID))

    def test_add_wPermission(self):
        os.remove(DB_PATH)
        open(DB_PATH, 'a').close()
        os.system('python3 test/create_db.py')
        db = DataBase(DB_PATH)

        db.create_blob(BLOB0_ID, BLOB0_LOCATION) 
        self.assertFalse(db.has_wPermission(USER1_ID, BLOB0_ID))

        db.add_wPermission(BLOB0_ID, USER1_ID)
        self.assertTrue(db.has_wPermission(USER1_ID, BLOB0_ID))
