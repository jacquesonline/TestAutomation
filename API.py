import http.client

conn = http.client.HTTPSConnection("companies-api4.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "9f9c848f32msh3b891a345bfe26ep1fd24ejsn745ad190de37",
    'x-rapidapi-host': "companies-api4.p.rapidapi.com"
}

conn.request("GET", "/6q7Pwi/companies", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
