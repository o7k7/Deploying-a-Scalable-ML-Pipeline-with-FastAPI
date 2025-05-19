import requests

r_health = requests.get("http://127.0.0.1:8000/health") # Your code here

print(r_health.status_code)
print(r_health.text)



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

r_infer = requests.post("http://127.0.0.1:8000/inference", json=data)

print(r_infer.status_code)
print(r_infer.text)
