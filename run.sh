echo "run containers"

docker run -ti -d --name blob --hostname blob -p 3002:3002 -v /home/alejandro/Escritorio/blob_service/persistence/blob:/src/persistence-blob debian-blob

docker run -ti -d --name auth --hostname auth -p 3001:3001 -v /home/alejandro/Escritorio/blob_service/persistence/auth:/src/persistence-auth debian-auth

docker run -ti -d --name dir --hostname dir -p 3003:3003 -v /home/alejandro/Escritorio/blob_service/persistence/dir:/src/persistence-dir debian-dir


# docker exec -it -d -w /src/ auth python3 auth_server.py -a admin

# docker exec -it -d -w /src/ blob python3 server_script.py -u http://172.17.0.3:3001 -a admin

# docker exec -it -d -w /src/ dir python3 dir_server.py -u http://172.17.0.3:3001 -a admin