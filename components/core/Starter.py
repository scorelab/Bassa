import urllib.request, urllib.error, urllib.parse

req = urllib.request.Request('http://localhost:5000/api/download/start')
req.add_header('key', '123456789')
resp = urllib.request.urlopen(req)
content = resp.read()
