# blob_service

## Authors

-   Alejandro Gálvez Ruiz - [Alejandro.Galvez\@alu.uclm.es](mailto:Alejandro.Galvez@alu.uclm.es)
-   Luis Javier Horcajada Torres - [LuisJavier.Horcajada\@alu.uclm.es](mailto:LuisJavier.Horcajada@alu.uclm.es)


## Execution

Create a virtual environment and activate it:
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Install all dependencies:
```shell
pip install -r requirements.txt
```

You can launch a server in a terminal:
```shell
python3 -m blob_service_scripts.server_script
```

You can launch a client in a terminal:
```shell
python3 -m blob_service_scripts.client_script
```

You can launch test with _Tox_:
```shell
pip install tox
tox
```
