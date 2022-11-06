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

You can launch test with _Tox_:
```shell
pip install tox
tox
```
## Server Execution

You can launch a server in a terminal:
```shell
python3 -m blob_service_scripts.server_script -u <AuthServer Url>
```
### Options for blob server launch:
 
- -p: Indicates port, default *3002*
- -d: Indicates database path, must finish with **.db**, default *database.db*
- -a: Admin token
- -l: IP address, default *0.0.0.0*
- -s: Indicates path for blob_storage, must be a **directory**, default *storage*
- -u: URL for AuthenticationServer **OBLIGATORY**

## Client Execution

You can launch a client in a terminal:
```shell
python3 -m blob_service_scripts.client_script
```
