import request

BASE = 'http://127.0.0.1:5000/'

data =[{'acao':'movi3','pm':15.54},
        {'acao':'shul4','pm':11.10},
        {'acao':'obir3','pm':1.70}]

for x in range(len(data)):
    response = request.put(BASE + 'carteira/'+str(x), data[x])
    print(data[x])
    print(len(data))
    print(response.json())
    input()


for x in range(len(data)):
    response = request.get(BASE + 'carteira/'+str(x))
    print(response.json())
    print(data)
    print(len(data))

    input()



response = request.delete(BASE + 'carteira/0')
print(response)
input()
