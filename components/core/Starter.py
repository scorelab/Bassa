import urllib.request, urllib.error, urllib.parse

req = urllib.request.Request('
  .value('BassaUrl', 'https://192.168.64.9/api/download/start')
req.add_header('key', '123456789')
resp = urllib.request.urlopen(req)
content = resp.read()
