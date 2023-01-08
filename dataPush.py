import json


def push_to_data(items):
    with open('data.json', 'w') as file:
        file.write(json.dumps({'morning': items[0], 'afternoon': items[1], 'evening': items[2]}, indent=4))
