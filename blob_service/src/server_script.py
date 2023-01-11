#!/usr/bin/env python3

'''
    Implementacion ejemplo de servidor y servicio REST
'''

from flask import Flask, make_response
import argparse
import os
from ipaddress import ip_address

from server import routeApp
from database import DataBase
from authService import AuthService, Unauthorized

def main():
    '''Entry point'''
    args = parse_args()
    token = get_token(args)
    port = get_port(args)
    address = get_address(args)
    database_path = get_database(args)
    blob_storage = get_blob(args)
    auth_server = get_authServer(args)

    if not AuthService(auth_server).is_admin(token):
        print("Invalid admin token")
        exit(1)

    print(blob_storage)

    
    app = Flask("database")
    routeApp(app, DataBase(database_path), auth_server, blob_storage)
    app.run(host= address, port=port,debug=True)

def parse_args():
    '''Argument Parser'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--admin", dest="admin_token", type=str, required=False, help="Admin token")
    parser.add_argument("-p", "--port", dest="port", type=int, required=False, help="Port for server")
    parser.add_argument("-l", "-listening", dest="address", type=ip_address, required=False, help="IP Address for server")
    parser.add_argument("-d", "--db", dest="database_path", type=str, required=False, help="Path for database")
    parser.add_argument("-s", "--storage", dest="blob_storage", type=str, required=False, help="Path for blob storage")
    parser.add_argument("-u", "--url", dest="url", type=str, required=True, help="Authentication server url")

    return parser.parse_args()

def get_token(args):
    '''Gets token from parser or generates default one'''
    admin_token = args.admin_token
    if admin_token is None:
        admin_token = "admin-token"
        print(f'Admin token generated: {admin_token}')
        return admin_token
    return admin_token

def get_port(args):
    '''Gets port from parser or generates default one'''
    port = args.port
    if port is None:
        port = 3002
        return port
    if 1<= port <= 65535:
        return port
    
    print("Invalid port number")
    exit(1)

def get_address(args):
    '''Gets ip address from parser or generates default one'''
    address = args.address
    if address is None:
        address = "0.0.0.0"
        return address
    return str(address)

def get_database(args):
    '''Gets database path from parser or generates default one'''
    database = args.database_path
    if database is None:
        try:
            open("/src/persistence-blob/dataBase.db", "r")
        except FileNotFoundError:
            open("/src/persistence-blob/dataBase.db", "x")
            os.system('python3 create_db.py')
        database = os.getcwd() + '/persistence-blob/dataBase.db'
        return database
    else:
        extension_db = os.path.splitext(database)[-1]
        if os.path.exists(database) is True and extension_db == '.db':
            return database
        else:
            print("Path given for database doesn't exist or database not found")
            exit(1)

def get_blob(args):
    '''Gets blob storage path from parser or generates default one'''
    blob_path = args.blob_storage
    if blob_path is None:
        cwd = os.getcwd()
        blob_path = os.path.join(cwd, 'persistence-blob/storage')
        if not os.path.exists(blob_path):
            os.makedirs(blob_path)
        return blob_path

    else:
        if os.path.exists(blob_path) is True and os.path.isdir(blob_path) is True:
            return blob_path
        else:
            print("Path given for blob storage doesn't exist or isn't a directory")
            exit(1)

def get_authServer(args):
    '''Gets authentication server url'''
    return args.url


if __name__ == '__main__':
    main()