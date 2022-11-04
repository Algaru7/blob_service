#!/usr/bin/env python3

'''
    REST access library + client example
'''

from blob_service.client import BlobService, Blob

'''Hay 2 usuarios en el sistema:
        -'Juan' con id '1'
        -'Pedro' con id '2
Usuario:token = '1':'token-admin';'2':'token-prueba '''

def main():
    client = BlobService('http://127.0.0.1:5000/')

    #Test new_blob
    #Code 200
    b = client.new_blob("client_files/prueba_subir_cliente.txt", '1')

    #Code 401
    '''Al cambiar la user-token, esta no se encuentra en el diccionario de auth y queda
       invalida'''
    
    '''Si el dueño de la user-token no tiene permisos de lectura'''
    b = client.new_blob("client_files/prueba_subir_cliente.txt", '1')

    b = client.get_blob('379', '1')
    #b.revoke_read_permission_to('1')

    b.dump_to('prueba_subir_cliente.txt')

    #client.remove_blob('611', '2')

    #Test get_blob
    #b = client.get_blob('2', '2')
    #print(b)
    #b.refresh_from("client_files/prueba_subir_cliente.txt")
    #b.dump_to('cliente_descarga')
    
if __name__ == "__main__":
    main()