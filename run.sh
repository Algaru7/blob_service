echo "run containers"

docker run -ti -d --name blob --hostname blob -p 3002:3002 -v $PWD/persistence/blob:/src/persistence-blob luisjaa01/servicio-adi:blob

docker run -ti -d --name auth --hostname auth -p 3001:3001 -v $PWD/persistence/auth:/src/persistence-auth luisjaa01/servicio-adi:auth

docker run -ti -d --name dir --hostname dir -p 3003:3003 -v $PWD/persistence/dir:/src/persistence-dir luisjaa01/servicio-adi:dir


if docker exec -it -d -w /src/ auth python3 auth_server.py -a admin ; then
    echo "Running auth server on http://127.17.0.3:3001."
else
    echo "Error running auth server."
fi

if docker exec -it -d -w /src/ blob python3 blob_server.py http://172.17.0.3:3001 -s /src/persistence-blob/storage ; then
    echo "Running blob server on http://127.17.0.2:3002."
else
    echo "Error running blob server."
fi

if docker exec -it -d -w /src/ dir python3 dir_server.py http://172.17.0.3:3001 ; then
    echo "Running dirs server on http://127.17.0.4:3003."
else
    echo "Error running dirs server."
fi
