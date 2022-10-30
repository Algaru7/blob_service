#!/usr/bin/env python3

from flask import make_response, request

from database import WrongBlobId

def routeApp(app, DATABASE):

    @app.route('/v1/blob/<blob_id>', methods=['PUT'])
    def create_blob(blob_id):
        if ("user-token" not in request.headers) and ("admin-token" not in request.headers):
            return make_response("Not 'user-token' or 'admin-token' found in header", 401)

        if not request.is_json:
            return make_response('Missing JSON', 400)
        if 'blob_location' not in request.get_json():
            return make_response('Missing "blob_location" key', 400)
        #if 'user' not in request.get_json():
            #return make_response('Missing "user" key', 400)

        blob_location = request.get_json()["blob_location"]
        #user = request.get_json()["user"]                  Para que se usa user aqui? hay que añadirlo a la tbala writable_by?

        DATABASE.create_blob(blob_id, blob_location)
        #DATABASE.add_wPermission(blob_id, user)

        return make_response(blob_id, 200)

    @app.route('/v1/blob/<blob_id>', methods=['GET'])
    def get_blob(blob_id):
        if ("user-token" not in request.headers) and ("admin-token" not in request.headers):
            return make_response("Missing valid token", 401)

        if not request.is_json:
            return make_response('Missing JSON', 400)
        if "user" not in request.get_json():
            return make_response('Missing "user" key', 400)
        
        if not DATABASE.has_rPermission(request.get_json()["user"], blob_id):
            return make_response(f"User has not readable permissions over this blob", 401)

        try:
            res_db = DATABASE.get_blob(blob_id)
        except WrongBlobId:
            return make_response(f"Blob not found", 404)

        response = {'blob_id': res_db[0], 'blob_location': res_db[1]}
        return make_response(response, 200)