import urllib.request
url = 'https://www.google.com/search?q=python'
headers = {}
headers ['User-Agent'] = "Mozilla/5.0 (X11; Linux 1686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
Request = urllib.request.Request(url, headers = headers)
Response = urllib.request.urlopen (Request)
Data = Response.read()
File =open('URLFile.txt', 'w')
File.write(str(Data))
File. close()
print ("Contents written in the file......")
