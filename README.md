# Python for networking
This is a collection of my Python scripts to practice skills in the areas of networking, subnetting, TCP/IP, sockets, etc



## Simple TCP server

In the [server file](simple_tcp/server.py), I create a very primitive socket that acts as a server, creating another socket for every connection,
only one connection at a time.
In the [client code](simple_tcp/client.py), another socket is created to communicate with the server.
Since both client and server are run in the same machine, I use the same IP for both. This works fine:

![image](https://github.com/user-attachments/assets/26d78ee5-f085-4cb4-8106-2c6d99d26df3)
