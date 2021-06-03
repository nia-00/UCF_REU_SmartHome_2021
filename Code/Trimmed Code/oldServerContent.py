#!/usr/bin/python3
#https://docs.python.org/3/library/http.server.html

# Module that allows us to set up socket communication
# Socket communication refers to the creation of a server socket
# that will use a particular port and go into a wait state as it listens
# for an incoming client
import socket
#from smart_home_controller import main
# http.server not recommended for production, only implements basic security checks
# BaseHTTPRequestHandler handles HTTP requests that arrive at the server and uses
# subclasses to handle each request method (GET and POST)
# HTTPServer stores server address as instance variables, server is accessible
# by handler through handler's 'server' instance variable
from http.server import BaseHTTPRequestHandler, HTTPServer

# Provides various time-related functions
import time
import pdb
import smart_home_controller
# Server address, tuple parameter of HTTPServer
hostName = ""
# Server port, tuple parameter of HTTPServer
hostPort = 8140


# Class dervied from BaseHTTPRequestHandler
class MyServer(BaseHTTPRequestHandler):
    
    # GET: Request data from the server (the following method is server response)
    def do_GET(self):
        # Adds response header to the headers buffer (which contains metadata information
        # like device number, block number range, etc) and logs accepted request
        self.send_response(200)
        # Adds the HTTP header to an internal buffer, is written to output steam when
        # end_headers() or flush_headers() is involved (param: (keyword, value))
        self.send_header("Content-type", "text/html")
        # Adds blank line to headers buffer (indiciating end of HTTP headers in response) and calls
        # flush_headers() which sends the headers to output stream and flushes internal headers buffer
        self.end_headers()
        # wfile contains output stream for writing a response back to client
        self.wfile.write(bytes("<p>You accessed path: %s</p>\n" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Headers: %s</p>\n" % self.headers, "utf-8"))
        # Set (host, port) parameters of client_address to variables
        hosta, porta = self.client_address
        self.wfile.write(bytes("<p>Client Address:"+str(hosta)+" "+str(porta)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>rline : "+str(self.requestline)+"</p>\n", "utf-8"))
        
        
    # POST: Submit data to be processed to the server (the following processes data and sends response)
    # For working details, see above in-line comments of do_GET(self)
    def do_POST(self):
        print( "incoming http: ", self.path )
        #Dict = eval(self.path)
        #print(Dict)
        #print(Dict['fan'])
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>This is a post</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>\n" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Headers: %s</p>\n" % self.headers, "utf-8"))
        hosta, porta = self.client_address
        self.wfile.write(bytes("<p>Client Address:"+str(hosta)+" "+str(porta)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>rline : "+str(self.requestline)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>Post data:"+str(post_data)+"</p>\n","utf-8"))

        infoRecieved = str(post_data)
        print(infoRecieved)
        infoRecieved = infoRecieved.split("file=")
        print(infoRecieved)
        filename = infoRecieved[1]
        filename = filename.replace("'", "")
        print("FILE NAME: ", filename)
        
       # execfile('smart_home_controller.py')

        control = smart_home_controller.ControlTower()
        control.main(filename)
        #os.system("smart_homeController.py 1")

        
# Create server with name, port, and MyServer class
myServer = HTTPServer((hostName, hostPort), MyServer)
# Record server start time
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
# Begin running server - will run forever...
try:
    myServer.serve_forever()
# ... except when KeyboardInterrupt (Ctrl + C)
except KeyboardInterrupt:
    pass

# Close server
myServer.server_close()
# Record server end time
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
                                        
        #infoRecieved = str(post_data)
        #print(infoRecieved)
        #infoRecieved = infoRecieved.split("filename=")
        #print(infoRecieved[1], "\n")
        #infoRecieved = infoRecieved[1].split('.txt')
        #file_name = infoRecieved[0]
        #print("file name: ", file_name, "\n")
        #infoRecieved = infoRecieved[0].split("/r/n/r/n")
        #rawCommands = infoRecieved[1]
        #print("unedited rawcommands:", rawCommands, "\n")
        #rawCommands = rawCommands.replace("/r", "")
        #rawCommands = rawCommands.replace("/n", "")

        #print("raw commands: ", rawCommands)
        #rawCommands = rawCommands.replace("on", "1")
        #rawCommands = rawCommands.replace("off", "0")
        #rawCommands = rawCommands.replace("open", "1")
        #rawCommands = rawCommands.replace("close", "0")
        #pdb.set_trace()
        #print("rawcom post rep: ", rawCommands)
        
        #rawCommands = rawCommands.replace('"', '')
        #rawCommands = rawCommands.replace('\\n', '')
        #rawCommands = rawCommands.replace('\\r', '')
        #print("rawcom edited: ", rawCommands)
        #rawCommands = rawCommands.split(",")
        #rawCommands.pop()
        #print("rawcom list?: ", rawCommands)
        #commandList = []
        #commandList = rawCommands.split(",")
        #listLength = len(rawCommands)
        #with open('hi.txt', 'w') as f:
        #    for i in range (listLength):
        #        f.write(rawCommands[i])
        #        f.write('\n')
        
        #f.close()
        
        #execfile('smart_home_controller.py')
        #os.system('smart_home_controller.py')
        #a = main()
        #print("\nHIIII")
        
       
        #commands = []
        #times = []
        
        #for i in range (0, listLength, 2):
        #    commands.append(commandList[i])
        #commands.pop
        #3for i in range (1, listLength, 2):
        #    times.append(commandList[i])
        
        
        #print('command: ', commands)
        
        #print('\ntimes: ', times)
        #commandList[len(commandList-1)] = commandList[len(commandList-1)].split("-")
        
        #print("\n commandList: ", commandList)
        
        #commandList[len(commandList-1)] = str(commandList[len(commandList-1)])
        
        #print("\n lastelem: ", commandList[len(commandList-1)])

        #print("\nlastelemtest: ", commandList[len(commandList-1)])
        #rawCommands = rawCommands.replace("\n", "")
        #rawCommands = rawCommands.replace("\r", "")
        #print("\ntest: ", rawCommands)
        #infoRecieved = infoRecieved.replace("b", "")
        #infoRecieved = infoRecieved.replace("'", "")
        #print(infoRecieved)
        
        #d = dict(x.split(" ") for x in rawCommands.split(","))
        #for k, v in d.items():
        #    print(k, v)
        
        #Dict = dict((x.strip(), y.strip())
        #     for x, y in (element.split(' ') 
        #     for element in rawCommands.split(', ')))
  
        #print(Dict)
            
        #fanCommand = d["fan"]
        #lampCommand = d["lamp"]

        #print(fanCommand)
        #print(lampCommand)
        #if lampCommand == 1:
        #    turnOnLamp()
        #split_info = infoRecieved.split('&')
        #print('Split string is:', split_info)
        #split_info[0] = split_info[0].replace("b'", "")
        #print('Split string is:', split_info)
    
        #if split_info.beginswith("b'"):
        #    split_info = split_info.replace("b'", "")
        #print('Split string is:', split_info)

        #Dict = eval(post_data)
        #print(Dict)
        
        #Dict = dict((x.strip(), y.strip())
        
        #for x, y in (element.split('=')
        #    for element in post_data.split(', ')))
        
        #print(Dict)
        #mydict = dict((k.strip(), v.strip()) for k,v in for x in map(int, input().split()):

        #      (item.split('=') for item in infoRecieved.split(',')))
        
        #print(mydict)
       # Dict = dict((x.strip(), y.strip())
       #      for x, y in (element.split('=') 
       #      for element in str(post_data).split(', ')))
  
        #print(Dict)
        #print(Dict['things'])
        #print(Dict['total'])
                                





##### Trimmed code #####

#self.wfile.write(bytes("<p>addr_str : "+ str(self.address_string)+"</p>\n", "utf-8"))
#client.close()
#import pdb; pdb.set_trace()

        #print('\ntimes: ', times)
        #commandList[len(commandList-1)] = commandList[len(commandList-1)].split("-")
        
       # print("\n commandList: ", commandList)

        #commandList[len(commandList-1)] = str(commandList[len(commandList-1)])
        
        #print("\n lastelem: ", commandList[len(commandList-1)])

        #print("\nlastelemtest: ", commandList[len(commandList-1)])
        #rawCommands = rawCommands.replace("\n", "")
        #rawCommands = rawCommands.replace("\r", "")
        #print("\ntest: ", rawCommands)
        #infoRecieved = infoRecieved.replace("b", "")
        #infoRecieved = infoRecieved.replace("'", "")
        #print(infoRecieved)
        
# Create server with name, port, and MyServer class
'''
myServer = HTTPServer((hostName, hostPort), MyServer)
# Record server start time
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
# Begin running server - will run forever...
try:
    myServer.serve_forever()
# ... except when KeyboardInterrupt (Ctrl + C)
except KeyboardInterrupt:
    pass

# Close server
myServer.server_close()
# Record server end time
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
'''

'''
'''
        #d = dict(x.split(" ") for x i#!/usr/bin/python3
#https://docs.python.org/3/library/http.server.html

'''
# Module that allows us to set up socket communication
# Socket communication refers to the creation of a server socket
# that will use a particular port and go into a wait state as it listens
# for an incoming client
import socket
from smart_home_controller import main
# http.server not recommended for production, only implements basic security checks
# BaseHTTPRequestHandler handles HTTP requests that arrive at the server and uses
# subclasses to handle each request method (GET and POST)
# HTTPServer stores server address as instance variables, server is accessible
# by handler through handler's 'server' instance variable
from http.server import BaseHTTPRequestHandler, HTTPServer

# Provides various time-related functions
import time
import pdb

# Server address, tuple parameter of HTTPServer
hostName = ""
# Server port, tuple parameter of HTTPServer
hostPort = 8140


# Class dervied from BaseHTTPRequestHandler
class MyServer(BaseHTTPRequestHandler):

    # GET: Request data from the server (the following method is server response)
    def do_GET(self):
        # Adds response header to the headers buffer (which contains metadata information
        # like device number, block number range, etc) and logs accepted request
        self.send_response(200)
        # Adds the HTTP header to an internal buffer, is written to output steam when
        # end_headers() or flush_headers() is involved (param: (keyword, value))
        self.send_header("Content-type", "text/html")
        # Adds blank line to headers buffer (indiciating end of HTTP headers in response) and calls
        # flush_headers() which sends the headers to output stream and flushes internal headers buffer
        self.end_headers()
        # wfile contains output stream for writing a response back to client
        self.wfile.write(bytes("<p>You accessed path: %s</p>\n" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Headers: %s</p>\n" % self.headers, "utf-8"))
        # Set (host, port) parameters of client_address to variables
        hosta, porta = self.client_address
        self.wfile.write(bytes("<p>Client Address:"+str(hosta)+" "+str(porta)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>rline : "+str(self.requestline)+"</p>\n", "utf-8"))
        
        
    # POST: Submit data to be processed to the server (the following processes data and sends response)
    # For working details, see above in-line comments of do_GET(self)
    def do_POST(self):
        print( "incoming http: ", self.path )
        #Dict = eval(self.path)
        #print(Dict)
        #print(Dict['fan'])
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>This is a post</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>\n" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Headers: %s</p>\n" % self.headers, "utf-8"))
        hosta, porta = self.client_address
        self.wfile.write(bytes("<p>Client Address:"+str(hosta)+" "+str(porta)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>rline : "+str(self.requestline)+"</p>\n", "utf-8"))
        self.wfile.write(bytes("<p>Post data:"+str(post_data)+"</p>\n","utf-8"))
                                        
        infoRecieved = str(post_data)
        print(infoRecieved)
        infoRecieved = infoRecieved.split("filename=")
        print(infoRecieved[1], "\n")
        infoRecieved = infoRecieved[1].split('.txt')
        file_name = infoRecieved[0]
        print("file name: ", file_name, "\n")
        #infoRecieved = infoRecieved[0].split("/r/n/r/n")
        rawCommands = infoRecieved[1]
        print("unedited rawcommands:", rawCommands, "\n")
        rawCommands = rawCommands.replace("/r", "")
        rawCommands = rawCommands.replace("/n", "")

        print("raw commands: ", rawCommands)
        rawCommands = rawCommands.replace("on", "1")
        rawCommands = rawCommands.replace("off", "0")
        rawCommands = rawCommands.replace("open", "1")
        rawCommands = rawCommands.replace("close", "0")
        pdb.set_trace()
        print("rawcom post rep: ", rawCommands)
        
        rawCommands = rawCommands.replace('"', '')
        rawCommands = rawCommands.replace('\\n', '')
        rawCommands = rawCommands.replace('\\r', '')
        print("rawcom edited: ", rawCommands)
        rawCommands = rawCommands.split(",")
        rawCommands.pop()
        print("rawcom list?: ", rawCommands)
        #commandList = []
        #commandList = rawCommands.split(",")
        listLength = len(rawCommands)
        with open('hi.txt', 'w') as f:
            for i in range (listLength):
                f.write(rawCommands[i]+'\n')
        
        f.close()
        a = main()
        #execfile('smart_home_controller.py')
        #os.system('smart_home_controller.py')
        #a = main()
        print("\nHIIII")
        
       
        #commands = []
        #times = []
        
        #for i in range (0, listLength, 2):
        #    commands.append(commandList[i])
        #commands.pop
        #3for i in range (1, listLength, 2):
        #    times.append(commandList[i])
        
        
        #print('command: ', commands)
        
        #print('\ntimes: ', times)
        #commandList[len(commandList-1)] = commandList[len(commandList-1)].split("-")
        
        #print("\n commandList: ", commandList)
        
        #commandList[len(commandList-1)] = str(commandList[len(commandList-1)])
        
        #print("\n lastelem: ", commandList[len(commandList-1)])

        #print("\nlastelemtest: ", commandList[len(commandList-1)])
        #rawCommands = rawCommands.replace("\n", "")
        #rawCommands = rawCommands.replace("\r", "")
        #print("\ntest: ", rawCommands)
        #infoRecieved = infoRecieved.replace("b", "")
        #infoRecieved = infoRecieved.replace("'", "")
        #print(infoRecieved)
        
        #d = dict(x.split(" ") for x in rawCommands.split(","))
        #for k, v in d.items():
        #    print(k, v)
        
        #Dict = dict((x.strip(), y.strip())
        #     for x, y in (element.split(' ') 
        #     for element in rawCommands.split(', ')))
  
        #print(Dict)
            
        #fanCommand = d["fan"]
        #lampCommand = d["lamp"]

        #print(fanCommand)
        #print(lampCommand)
        #if lampCommand == 1:
        #    turnOnLamp()
        #split_info = infoRecieved.split('&')
        #print('Split string is:', split_info)
        #split_info[0] = split_info[0].replace("b'", "")
        #print('Split string is:', split_info)
    
        #if split_info.beginswith("b'"):
        #    split_info = split_info.replace("b'", "")
        #print('Split string is:', split_info)

        #Dict = eval(post_data)
        #print(Dict)
        
        #Dict = dict((x.strip(), y.strip())
        
        #for x, y in (element.split('=')
        #    for element in post_data.split(', ')))
        
        #print(Dict)
        #mydict = dict((k.strip(), v.strip()) for k,v in for x in map(int, input().split()):

        #      (item.split('=') for item in infoRecieved.split(',')))
        
        #print(mydict)
       # Dict = dict((x.strip(), y.strip())
       #      for x, y in (element.split('=') 
       #      for element in str(post_data).split(', ')))
  
        #print(Dict)
        #print(Dict['things'])
        #print(Dict['total'])
                                


# Create server with name, port, and MyServer class
myServer = HTTPServer((hostName, hostPort), MyServer)
# Record server start time
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
# Begin running server - will run forever...
try:
    myServer.serve_forever()
# ... except when KeyboardInterrupt (Ctrl + C)
except KeyboardInterrupt:
    pass

# Close server
myServer.server_close()
# Record server end time
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))



##### Trimmed code #####

#self.wfile.write(bytes("<p>addr_str : "+ str(self.address_string)+"</p>\n", "utf-8"))
#client.close()
#import pdb; pdb.set_trace()
#n rawCommands.split(","))
        #for k, v in d.items():
        #    print(k, v)
        
        #Dict = dict((x.strip(), y.strip())
        #     for x, y in (element.split(' ') 
        #     for element in rawCommands.split(', ')))
  
        #print(Dict)
            
        #fanCommand = d["fan"]
        #lampCommand = d["lamp"]

        #print(fanCommand)
        #print(lampCommand)
        #if lampCommand == 1:
        #    turnOnLamp()
        #split_info = infoRecieved.split('&')
        #print('Split string is:', split_info)
        #split_info[0] = split_info[0].replace("b'", "")
        #print('Split string is:', split_info)
    
        #if split_info.beginswith("b'"):
        #    split_info = split_info.replace("b'", "")
        #print('Split string is:', split_info)

        #Dict = eval(post_data)
        #print(Dict)
        
        #Dict = dict((x.strip(), y.strip())
        
        #for x, y in (element.split('=')
        #    for element in post_data.split(', ')))
        
        #print(Dict)
        #mydict = dict((k.strip(), v.strip()) for k,v in for x in map(int, input().split()):

        #      (item.split('=') for item in infoRecieved.split(',')))
        
        #print(mydict)
       # Dict = dict((x.strip(), y.strip())
       #      for x, y in (element.split('=') 
       #      for element in str(post_data).split(', ')))
  
        #print(Dict)
        #print(Dict['things'])
        #print(Dict['total'])
                                




##### Trimmed code #####

#self.wfile.write(bytes("<p>addr_str : "+ str(self.address_string)+"</p>\n", "utf-8"))
#client.close()
#import pdb; pdb.set_trace()
'''
