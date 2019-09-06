# Team members: Chaoneng Quan, Jian Fang

This is a server/client tool

server.py:
This file simulates a server, it is able to accept a connection and listen to connected device. When server receices some information from the established pipe, it will reverse the message and send it back. 
client.py
This file simulates a client, it can send a connection request to server. Once it gets the permission and connected to server, it will send message to server and will be able to receive the server response.
