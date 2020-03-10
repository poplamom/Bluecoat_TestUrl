import requests

data = open('sample_url', 'r')
data1 = data.readlines()
# print(data1)
bluecoaturl = 'https://x.x.x.x:8082/ContentFilter/TestUrl/'
f = open("sample_url.csv", "w+")

for x in data1:
    # print(bluecoaturl+x)
    x = x.splitlines()[0]
    # print(x)
    r = requests.get(bluecoaturl + x, auth=('username', 'password'), verify=False)
    a = r.text.split(('\n')[0])
    # print(a[4])
    # # print(x)
    # a = a.append(x)
    # f.write(x + ' , ' + a[4] + '\n')
    print(x + ' , ' + a[4])
    # print(x + ' , ' + a[0])
f.close()

