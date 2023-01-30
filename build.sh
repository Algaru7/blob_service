#!/bin/bash
echo "build images"

base_repo="luisjaa01"

docker build --rm -f Dockerfile --tag debian-base .

docker build --rm -f auth_service/Dockerfile --tag ${base_repo}/servicio-adi:auth ./auth_service/
docker build --rm -f blob_service/Dockerfile --tag ${base_repo}/servicio-adi:blob ./blob_service/
docker build --rm -f dir_service/Dockerfile  --tag ${base_repo}/servicio-adi:dir  ./dir_service/

#docker save luisjaa01/servicio-adi:blob | gzip > blob_service.tar.gz
#docker save luisjaa01/servicio-adi:auth | gzip > auth_service.tar.gz
#docker save luisjaa01/servicio-adi:dir | gzip > dir_service.tar.gz

docker push ${base_repo}/servicio-adi:auth
docker push ${base_repo}/servicio-adi:blob
docker push ${base_repo}/servicio-adi:dir
