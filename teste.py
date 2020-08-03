import request

BASE = 'http://127.0.0.1:5000/'

data =[{'acao':'movi3','pm':15.54},
        {'acao':'shul4','pm':11.10},
        {'acao':'obir3','pm':1.70},
        {'acao':'wege3','pm':55.71}]

for i in range(len(data)):
    response = request.put(BASE + 'carteira/'+str(i),data[i] )
    print(response.json())

response = request.delete(BASE + 'carteira/1')
print(response)
input()
response = request.get(BASE + 'carteira/1')
print(response)
