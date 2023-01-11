echo "run containers"
docker run -ti --name blob --hostname blob -p 3002:3002 debian-blob

docker run -ti --name auth --hostname auth -p 3001:3001 debian-auth