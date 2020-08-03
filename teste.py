import request

BASE = 'http://127.0.0.1:5000/'

response = request.put(BASE + 'carteira/1', {'pm':15.54})
print(response.json())
