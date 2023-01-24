#!/bin/bash
echo "build images"
docker build --rm -f Dockerfile --tag debian-base .

docker build --rm -f blob_service/Dockerfile --tag debian-blob ./blob_service

docker build --rm -f auth_service/Dockerfile --tag debian-auth ./auth_service

docker build --rm -f dir_service/Dockerfile --tag debian-dir ./dir_service