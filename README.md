# Python for networking
This is a collection of my Python scripts to practice skills in the areas of networking, subnetting, TCP/IP, sockets, etc



## Simple TCP server

In the [server file](simple_tcp/server.py), I create a very primitive socket that acts as a server, creating another socket for every connection,
only one connection at a time.
In the [client code](simple_tcp/client.py), another socket is created to communicate with the server.
Since both client and server are run in the same machine, I use the same IP for both. This works fine:

![image](https://github.com/user-attachments/assets/26d78ee5-f085-4cb4-8106-2c6d99d26df3)


## Port scanner

This [port scanner](port_scanner/main.py) script takes an ip address and mask such as `10.0.0.0/30` and searchs for all active IPs and all open ports in each IP.
The code incorporates multi-threading, lambda functions and overall a bit of thought to optimize the task as much as possible.
