echo "run containers"
docker run -ti --name blob --hostname blob -p 3002:3002 -v /home/alejandro/Escritorio/adi/blob_service/persistence/blob:/src/persistence-blob debian-blob

docker run -ti --name auth --hostname auth -p 3001:3001 -v /home/alejandro/Escritorio/adi/blob_service/persistence/auth:/src/persistence-auth debian-auth