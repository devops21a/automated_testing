import http.client
import mimetypes
conn = http.client.HTTPSConnection("api.getpostman.com")
payload = ''
headers = {
  'X-Api-Key': 'PMAK-5fb55c502fe876003486c989-217cffa81717cf1a39634e529c6e48977b'
}
conn.request("GET", "/collections", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))