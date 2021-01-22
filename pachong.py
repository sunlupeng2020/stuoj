import urllib.request
response = urllib.request.urlopen("http://47.95.10.46")
html = response.read().decode('UTF-8')
print(html)
