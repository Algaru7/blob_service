#!/usr/bin/env python3

'''
    Implementacion ejemplo de servidor y servicio REST
'''

from flask import Flask

from server import routeApp
from database import DataBase

def main():
    '''Entry point'''
    app = Flask("database")
    routeApp(app, DataBase())
    app.run(debug=True)


if __name__ == '__main__':
    main()