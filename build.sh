#!/bin/bash
echo "build images"
docker build --rm -f Dockerfile --tag debian-base .

docker build --rm -f blob_service/Dockerfile --tag debian-blob ./blob_service

docker build --rm -f auth_service/Dockerfile --tag debian-auth ./auth_service

docker build --rm -f dir_service/Dockerfile --tag debian-dir ./dir_service

docker save debian-blob:latest | gzip > blob_service.tar.gz
docker save debian-auth:latest | gzip > auth_service.tar.gz
docker save debian-dir:latest | gzip > dir_service.tar.gz