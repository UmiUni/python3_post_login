import http.client

conn = http.client.HTTPConnection("178.128.0.108:3001")

payload = "{\n    \"Email\": \"skylineblueblueblue@gmail.com\",\n    \"Password\": \"test\"\n}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
##    'postman-token': "cefc9038-62bc-8573-1931-a3b1cd609dc3"
    }

conn.request("POST", "/login", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
