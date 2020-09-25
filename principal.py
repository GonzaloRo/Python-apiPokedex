import requests



respons = requests.get(' https://pokeapi.co/api/v2/pokemon/1/')#url para traer la informacion inicial de los primero 150 pokemons
response = requests.get(' https://pokeapi.co/api/v2/pokemon?limit=150&offset=0')#url para traer la informacion inicial de los primero 150 pokemons
if respons.status_code == 200:
    contenido = respons.content
    diccionario = respons.json()
    for detpokemon in diccionario:
     print(detpokemon)    
    
else:
    print('se chingo')