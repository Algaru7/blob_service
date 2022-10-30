#!/usr/bin/env python3

'''
    REST access library + client example
'''

from client import BlobService, Blob

def main():
    client = BlobService('http://127.0.0.1:5000/')

    #Test new_blob
    #client.new_blob("prueba6.txt", '2')

    #Test get_blob
    b = client.get_blob('2', '2')
    print(b)
    
if __name__ == "__main__":
    main()