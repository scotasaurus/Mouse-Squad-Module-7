import urllib
import urllib2
import json

urlToRequest = "http://jsonplaceholder.typicode.com/posts"

request = urllib2.Request(urlToRequest)
response = urllib2.urlopen(request)

jsonData = json.load(response)

print jsonData[0]["title"]
