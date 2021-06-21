from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import time
import smart_home_controller   # File that actually executes house simulations

hostName = ""
hostPort = 8140


class MyServer(BaseHTTPRequestHandler):
    
    # GET: Request data from the server (the following method is server response)
    def do_GET(self):
        self.send_response(200)                          # Adds response header to the headers buffer
        self.send_header("Content-type", "text/html")    # Adds the HTTP header to an internal buffer
        self.end_headers()
        
        self.wfile.write(bytes("You accessed path: %s\n" % self.path, "utf-8"))
        self.wfile.write(bytes("Headers: %s\n" % self.headers, "utf-8"))

        hosta, porta = self.client_address
        self.wfile.write(bytes("Client Address:"+ str(hosta) + " " + str(porta) + "\n", "utf-8"))
        self.wfile.write(bytes("rline : " + str(self.requestline) + "\n", "utf-8"))
        
        
    # POST: Submit data to be processed to the server (the following processes data and sends response)
    def do_POST(self):
        print( "incoming http: ", self.path )
        content_length = int(self.headers['Content-Length'])    # Gets the size of data
        post_data = self.rfile.read(content_length)             # Gets the data itself
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        self.wfile.write(bytes("This is a post response\n", "utf-8"))
        hosta, porta = self.client_address
        self.wfile.write(bytes("Client Address: " + str(hosta) + " " + str(porta) + "\n", "utf-8"))
        self.wfile.write(bytes("rline: "+ str(self.requestline) + "\n", "utf-8"))
        self.wfile.write(bytes("Post data: " + str(post_data) + "\n", "utf-8"))
        self.wfile.write(bytes("Client Address: " + str(hosta) + " " + str(porta) + "\n", "utf-8"))

        # Post data consists of a specified file name (by client) which contains simulation commands
        infoRecieved = str(post_data)
        infoRecieved = infoRecieved.split("file=")
        filename = infoRecieved[1]
        filename = filename.replace("'", "")
        print("\nSIMULATION FILE NAME: ", filename, "\n")
        
        # Run simulation after file name is successfully received 
        control = smart_home_controller.ControlTower()
        control.main(filename)
        
        
# Create server with name, port, and MyServer class
myServer = HTTPServer((hostName, hostPort), MyServer)
# Record server start time
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))    

# Run server indefinitely
try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

# Close server
myServer.server_close()
# Record server end time
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
   
   
   

'''
---------- Notes related to content in server.py ----------

https://docs.python.org/3/library/http.server.html

Socket communication refers to the creation of a server socket that will use a
particular port and go into a wait state as it listens for an incoming client

http.server not recommended for production, only implements basic security checks

BaseHTTPRequestHandler handles HTTP requests that arrive at the server and uses
subclasses to handle each request method (GET and POST)

HTTPServer stores server address as instance variables, server is accessible
by handler through handler's 'server' instance variable

Server address and port are tuple parameters of HTTPServer

self.send_response(200) adds response header to the headers buffer (which contains
metadata information like device number, block number range, etc) and logs accepted request

self.send_header("Content-type", "text/html") adds the HTTP header to an internal
buffer, is written to output steam when end_headers() or flush_headers() is involved
(param: (keyword, value))

self.end_headers() adds blank line to headers buffer (indiciating end of HTTP headers
in response) and calls flush_headers() which sends the headers to output stream and
flushes internal headers buffer

wfile contains output stream for writing a response back to client

hosta, porta = self.client_address sets parameters of client_address (host, port) to variables     
'''