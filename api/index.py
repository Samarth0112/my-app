import json
import urllib.parse

def load_data():
    with open("q-vercel-python.json", "r") as file:
        return json.load(file)

def handler(event, context):
    query_string = event.get("queryStringParameters", {})
    names = query_string.get("name", [])

    if isinstance(names, str):  # Ensure 'name' is a list even if a single value is provided
        names = [names]

    data = load_data()
    
    result = {"marks": []}
    for name in names:
        for entry in data:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # Enable CORS
        },
        "body": json.dumps(result)
    }
