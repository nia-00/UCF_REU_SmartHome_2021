import http.client
from urllib.parse import urlencode


connection = http.client.HTTPSConnection("localhost")
params= {'things':2,'total':25}
connection.request("GET", '/?' + urlencode({'params': params}))
response = connection.getresponse()
headers = response.getheaders()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("Headers: {}".format(headers))
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()