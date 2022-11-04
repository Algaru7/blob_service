#!/usr/bin/env python3

'''
    REST access library + client example
'''

from blob_service.client import BlobService, Blob

def main():
    client = BlobService('http://127.0.0.1:5000/')

    #Test new_blob
    b = client.new_blob("client_files/prueba_subir_cliente.txt", '2')

    client.remove_blob('611', '2')

    #Test get_blob
    #b = client.get_blob('2', '2')
    #print(b)
    #b.refresh_from("client_files/prueba_subir_cliente.txt")
    #b.dump_to('cliente_descarga')
    
if __name__ == "__main__":
    main()