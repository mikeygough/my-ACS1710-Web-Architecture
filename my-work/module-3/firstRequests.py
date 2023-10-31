# users need to be able to make requests in app

import requests

# a text-based response object
result1 = requests.get("http://127.0.0.1:5000")
print("base result 1 print out === ", result1)

result1_text = result1.text
print(result1_text)

# a json-based response object
result2 = requests.get("http://127.0.0.1:5000/jsonExample")
print("base result 2 print out === ", result2)

result2_json = result2.json()
print(result2_json)