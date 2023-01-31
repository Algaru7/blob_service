# ADI Project

## Authors

-   Alejandro Gálvez Ruiz - [Alejandro.Galvez\@alu.uclm.es](mailto:Alejandro.Galvez@alu.uclm.es)
-   Luis Javier Horcajada Torres - [LuisJavier.Horcajada\@alu.uclm.es](mailto:LuisJavier.Horcajada@alu.uclm.es)



## Setting up the Virtual Boxes

To configure the platform we need two virtual boxes with the same Ubuntu version (we used Ubuntu 20.04):

- A master
- A worker

To configure both options with 8 GB RAM and 2 processors we need to follow this process for each virtual box:

- **Settings**->**System**->**Motherboard**-> *Base_Memory= 8192 MB*
- **Settings**->**System**->**Processor**-> *Processor(s)= 2*



## Setting up the network

We have two options:

- Creating a network for both virtual boxes
- Using a bridged adapter to have connectivity between the virtual boxes and your real machine. 

### Option 1

This option will only allow connectivity between both virtual boxes.

**Steps:**

- Open Virtual Box Manager
- **File**->**Preferences**->**Networks**-> Create a new Network
- You can create any network, we recommend 192.168.10.0/24 for the Network CIDR as it won't interfere with anything.

**Steps for each virtual box**:

- **Settings**->**Network**->**Use NAT Network**-> **Select the previously created NAT Network**.

### Option 2

This is the best option but you need an **ETHERNET Connection**.

**Steps for each virtual box**:

- **Settings**->**Network**->**Use Bridged Adapter**-> **Select enp0s3 as the name**.



## Platform configuration

We have also opted to use a tool called **MicroK8s** as it makes things simpler.

```shell
sudo snap install microk8s --classic
```

Since we use Docker for each microservice we need to install it as well.

```shell
sudo apt install docker.io
```

We need to check if MicroK8s is running on both the worker and the master:

```shell
microk8s status
```

If the service is **NOT** running we start it
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

To deploy, we need two files:

- deploy.sh
- deployment.yml
