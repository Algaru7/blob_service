#!/usr/bin/env python3

'''
    REST access library + client example
'''

from blob_service.client import BlobService, Blob

'''Hay 2 usuarios en el sistema:
        -'Juan' con id '1'
        -'Pedro' con id '2
Usuario:token = '1':'token-admin';'2':'token-prueba '''

USER1 = '1'
USER2 = '2'
TOKEN_USER1 = 'token-admin'
TOKEN_USER2 = 'token-prueba'
FILE1 = 'client_files/test_file_1.txt'
FILE2 = 'client_files/test_file_1.txt'

IP = 'http://127.0.0.1'
PORT = '3002'

def main():

    print(f"->We access as user '{USER1}' using its own token '{TOKEN_USER1}'")
    client = BlobService(f'{IP}:{PORT}/', TOKEN_USER1)

    print(f"\tWe create a new blob with content of {FILE1}")
    blob = client.new_blob(FILE1, USER1)
    print(f"\tWe add read and write permissions to other user '{USER2}'")
    blob.add_read_permission_to(USER2)
    blob.add_write_permission_to(USER2)
    print(f"\tWe update content of the blob created with content of '{FILE2}'")
    blob.refresh_from(FILE2)

    print(f"\n->We access now with other user ({USER2}) using its own token '{TOKEN_USER1}'")
    client = BlobService(f'{IP}:{PORT}/', "token-prueba")
    print("\tWe get the previously created blob")
    blob = client.get_blob(blob.id, USER2)
    print(f"\tWe revoke read and write permissions to other user '{USER1}'")
    blob.revoke_read_permission_to(USER1)
    blob.revoke_write_permission_to(USER1)
    print(f"\tWe dump content of blob to {FILE1}")
    blob.dump_to(FILE1)
    print(f"\tWe remove the blob")
    client.remove_blob(blob.id, USER2)


    
if __name__ == "__main__":
    main()