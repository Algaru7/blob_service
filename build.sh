#!/bin/bash
echo "build images"
docker build --rm -f Dockerfile --tag debian-base .

docker build --rm -f blob_service/Dockerfile --tag luisjaa01/servicio-adi:blob ./blob_service

docker build --rm -f auth_service/Dockerfile --tag luisjaa01/servicio-adi:auth ./auth_service

docker build --rm -f dir_service/Dockerfile --tag luisjaa01/servicio-adi:dir ./dir_service

docker save luisjaa01/servicio-adi:blob | gzip > blob_service.tar.gz
docker save luisjaa01/servicio-adi:auth | gzip > auth_service.tar.gz
docker save luisjaa01/servicio-adi:dir | gzip > dir_service.tar.gz

docker push luisjaa01/servicio-adi:blob
docker push luisjaa01/servicio-adi:auth
docker push luisjaa01/servicio-adi:dir
