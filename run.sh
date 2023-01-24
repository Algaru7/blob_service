echo "run containers"

docker run -ti -d --name blob --hostname blob -p 3002:3002 -v $PWD/persistence/blob:/src/persistence-blob debian-blob

docker run -ti -d --name auth --hostname auth -p 3001:3001 -v $PWD/persistence/auth:/src/persistence-auth debian-auth

docker run -ti -d --name dir --hostname dir -p 3003:3003 -v $PWD/persistence/dir:/src/persistence-dir debian-dir


docker exec -it -d -w /src/ auth python3 auth_server.py -a admin

docker exec -it -d -w /src/ blob python3 blob_server.py http://172.17.0.3:3001 -s /src/persistence-blob/storage

docker exec -it -d -w /src/ dir python3 dir_server.py http://172.17.0.3:3001