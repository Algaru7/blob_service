#!/usr/bin/env python3

'''
    Implementacion ejemplo de servidor y servicio REST
'''

from flask import Flask

from blob_service.server import routeApp
from blob_service.database import DataBase

def main():
    '''Entry point'''
    app = Flask("database")
    routeApp(app, DataBase("./dataBase.db"))
    app.run(debug=True)


if __name__ == '__main__':
    main()