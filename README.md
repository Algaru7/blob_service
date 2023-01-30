# ADI Project

## Authors

-   Alejandro Gálvez Ruiz - [Alejandro.Galvez\@alu.uclm.es](mailto:Alejandro.Galvez@alu.uclm.es)
-   Luis Javier Horcajada Torres - [LuisJavier.Horcajada\@alu.uclm.es](mailto:LuisJavier.Horcajada@alu.uclm.es)


## Platform configuration

To configure the platform we need two virtual boxes:
- A master
- A worker

We have also opted to use a tool called **MicroK8s** as it makes things simpler.

We first need to check if MicroK8s is running on both the worker and the master:

```shell
microk8s status
```

If the pod is **NOT** running we start it
```shell
microk8s start
```


### Master Virtual Box

Add the worker node to create a cluster:

```shell
microk8s add-node
```

This will give you an IP address and a hash that you need to copy in the worker virtual box:

Example:

microk8s join 192.168.64.4:25000/IfrgUOBCMGxZyAcRgEXXLONcwMKWpstO

### Worker

We copy the command that the master generated previously.

Previous example:

```shell
microk8s join 192.168.64.4:25000/IfrgUOBCMGxZyAcRgEXXLONcwMKWpstO
```
## Deployment
