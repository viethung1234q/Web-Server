from socket import *

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	print ("addr:", addr)

	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()

		#Send one HTTP header line into socket
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
		# connectionSocket.send('Content-Type: text/html\n')

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())

		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())

		#Close client socket 
		connectionSocket.close()
