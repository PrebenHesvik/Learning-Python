import json
from urllib.request import urlopen

people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "944-28-507",
            "email": "john.smith@hotmail.com",
            "has_license": false
        },
        {
            "name": "Sall Jones",
            "phone": "982-69-577",
            "email": "sally.jones@hotmail.com",
            "has_license": true
        }
    ]
}
 """

 # json.load is used to load a file
 # json.loads is used to load a string

 # json.dump is used to save object to json file
 # json.dumps is used to save object to json string

data = json.loads(people_string)

# Accessing each 'people' item
for person in data['people']:
    print(person)

# Accessing each name of the items in 'people'
for person in data['people']:
    print(person['name'])

# delete each person's phone number
for person in data['people']:
    del person['phone']

# Create new json string without the phone number item
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

with open('py_notes/us_states.json') as f:
    data = json.load(f)

for state in data:
    print(state['name'], state['abbreviation'])


""" WORKING WITH DATA FROM YAHOO API """

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

# check number of items
json_length = len(data['list']['resources'])
print(json_length)

# List all conversions and values in the json file
for item in data['list']['resources']:
    name = item['resource']['fields']['name'] # <--- when working with json data we sometimes have to dig down into the file to find the values we want
    price = item['resource']['fields']['price']
    print(name, price)
