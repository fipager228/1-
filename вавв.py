import json
import urllib.request
from prettytable import PrettyTable

url = "http://jsonplaceholder.typicode.com/users"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

table = PrettyTable()
table.field_names = ["ID", "Name", "Username", "Email", "City"]

for user in data:
    table.add_row([
        user["id"],
        user["name"],
        user["username"],
        user["email"],
        user["address"]["city"]
    ])

print(table)
