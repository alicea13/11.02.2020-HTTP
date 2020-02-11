import requests
import sys


server = sys.argv[1]
port = sys.argv[2]
a, b = sys.argv[3], sys.argv[4]

resp_serv = ":".join([server, port])

response = requests.get(resp_serv, params={"a": a, "b": b})
print(*sorted(response.json()["result"]))
print(response.json()["check"])
