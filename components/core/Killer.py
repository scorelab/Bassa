import urllib.request, urllib.error, urllib.parse

req = urllib.request.Request('https://192.168.64.9/api/download/kill')
req.add_header('key', '123456789')
resp = urllib.request.urlopen(req)
content = resp.read()