# Web-Server

Đoàn Việt Hưng - hungdoan2712@gmail.com


You will develop a web server that handles one HTTP request at a time. Your web server should accept
and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response
message consisting of the requested file preceded by header lines, and then send the response directly to
the client. If the requested file is not present in the server, the server should send an HTTP “404 Not
Found” message back to the client.

CODE

Below you will find the skeleton code for the Web server. You are to complete the skeleton code. The
places where you need to fill in code are marked with #Fill in start and #Fill in end. Each place
may require one or more lines of code.

RUNNING THE SERVER 

Put an HTML file (e.g., HelloWorld.html) in the same directory that the server is in. Run the server
program. Determine the IP address of the host that is running the server (e.g., 128.238.251.26). From
another host, open a browser and provide the corresponding URL. For example:
http://128.238.251.26:6789/HelloWorld.html
‘HelloWorld.html’ is the name of the file you placed in the server directory. Note also the use of the port
number after the colon. You need to replace this port number with whatever port you have used in the
server code. In the above example, we have used the port number 6789. The browser should then display
the contents of HelloWorld.html. If you omit ":6789", the browser will assume port 80 and you will get
the web page from the server only if your server is listening at port 80.
Then try to get a file that is not present at the server. You should get a “404 Not Found” message. 

OPTIONAL EXERCISE

Instead of using a browser, write your own HTTP client to test your server. Your client will connect
to the server using a TCP connection, send an HTTP request to the server, and display the server
response as an output. You can assume that the HTTP request sent is a GET method.
The client should take command line arguments specifying the server IP address or host name, the
port at which the server is listening, and the path at which the requested object is stored at the server.
The following is an input command format to run the client.
               client.py server_host server_port filename
