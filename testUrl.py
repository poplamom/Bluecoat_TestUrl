import requests

data = open('sample_url', 'r')
data1 = data.readlines()

bluecoaturl = 'https://x.x.x.x:8082/ContentFilter/TestUrl/'
f = open("sample_url.csv", "w+")

for x in data1:
    x = x.splitlines()[0]
    r = requests.get(bluecoaturl + x, auth=('username', 'password'), verify=False)
    a = r.text.split(('\n')[0])
    print(x + ' , ' + a[4])
f.close()

