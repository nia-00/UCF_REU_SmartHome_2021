import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}

urlm = "http://192.168.138.161:8140"
filename = "simulation1.txt"

ploads = {'file': filename}
r = requests.request(method = 'GET', url = urlm + "", params=ploads, headers=headers)

print(r.text)
print(r.url)

print("\n---- POST ----")
postResponse = requests.post(urlm, data = ploads)
print(postResponse.text)