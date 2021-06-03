import requests

#r=requests.get("http://localhost/safa.png?safa=1111")
#f.write(r.text)
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

urlm="http://192.168.29.235"
ploads = {'things':2,'total':25}
r = requests.request(method='GET', url=urlm+"/safa.png",params=ploads,headers=headers)
print(r.text)
#print(r.url)
print("PSOT")
ploads = {'things':222222,'total':"necmii"}
x = requests.post(urlm, data = ploads)
print(x.text)



