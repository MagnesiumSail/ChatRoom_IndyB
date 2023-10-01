# Overview

In this program, I learned the basics of setting up a server to client connection in Python. This program was not only a great refresher of python language, but also my first delve into any sort of network-utilizing program.

The server program is located [Here](./Server/program.py). Simply run the program and pay attention to the local IP it gives you.

The client program located [Here](./Client/client.py) will prompt you for the ip address (output by the server) and will automatically connect you. Simply type messages in terminal and press enter, and all other clients connected to the server will recieve them. To disconnect from the server send 'exit'.

My purpose for this software was a simple proof of concept for using the sockets library in junction with threads in C#.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

Client/Server

TCP : port 34874

Format: Bytes

# Development Environment

Visual Code Studio

Python Language
Socket Library
Threading Library

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
    -Used for learning socket syntax
* [ChatGPT](https://chat.openai.com/)
    -Used excusively for debugging

# Future Work

* Server needs a built in exit function
* Client needs a cleaner exit function that doesn't 'crash' threads
* Server should be improved to not use a new thread for every new connection