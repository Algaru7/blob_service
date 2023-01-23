# blob_service

## Authors

-   Alejandro Gálvez Ruiz - [Alejandro.Galvez\@alu.uclm.es](mailto:Alejandro.Galvez@alu.uclm.es)
-   Luis Javier Horcajada Torres - [LuisJavier.Horcajada\@alu.uclm.es](mailto:LuisJavier.Horcajada@alu.uclm.es)


## Build

You can build docker images with
```shell
source build.sh
```

## Run

You run docker containers with
```shell
source run.sh
```
which will use _persistence/_ as a volume for persistence and will launch an auth and blob server with an admin token 'admin'.

## Client Execution

You can launch a client in a terminal:
```shell
python3 blob_service/src/client_server.py
```
