import urllib2

req = urllib2.Request('http://localhost:5000/download/start')
req.add_header('key', '123456789')
resp = urllib2.urlopen(req)
content = resp.read()
