import json
import urllib.parse

def load_data():
    with open("q-vercel-python.json", "r") as file:
        return json.load(file)

def handler(request):
    query_string = request.args
    names = query_string.getlist("name")

    data = load_data()
    
    result = {"marks": []}
    for name in names:
        for entry in data:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])

    return json.dumps(result), 200, {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}
