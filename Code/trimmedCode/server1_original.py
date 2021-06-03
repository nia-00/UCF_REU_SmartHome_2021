#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = ""
hostPort = 80

#https://docs.python.org/3/library/http.server.html

class MyServer(BaseHTTPRequestHandler):

    #    GET is for clients geting the predi
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>You accessed path: %s</p>\n" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Headers: %s</p>\n" % self.headers, "utf-8"))
        hosta,porta =self.client_address
        self.wfile.write(bytes("<p>Client Address:"+str(hosta)+" "+str(porta)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>rline : "+str(self.requestline)+"</p>\n", "utf-8"))
        #self.wfile.write(bytes("<p>addr_str : "+ str(self.address_string)+"</p>\n", "utf-8"))
        
        
    #    POST is for submitting data.
    def do_POST(self):

        print( "incomming http: ", self.path )

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>This is a post</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>\n" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Headers: %s</p>\n" % self.headers, "utf-8"))
        hosta,porta =self.client_address
        self.wfile.write(bytes("<p>Client Address:"+str(hosta)+" "+str(porta)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>rline : "+str(self.requestline)+"</p>\n", "utf-8"))
        #self.wfile.write(bytes("<p>addr_str : "+ str(self.address_string)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>Post data:"+str(post_data)+"</p>\n","utf-8"))
        #client.close()

        #import pdb; pdb.set_trace()


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))