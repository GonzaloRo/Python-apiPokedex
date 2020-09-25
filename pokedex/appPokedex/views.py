from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    respons = requests.get(' https://pokeapi.co/api/v2/pokemon?limit=150&offset=0')#url para traer la informacion inicial de los primero 150 pokemons
    if respons.status_code == 200:
        contenido = respons.content
        diccionario = respons.json()
        listpokemon = diccionario['results'];        
        contexto = {'pokemons': diccionario['results']}  
    
    return render (request, '../Templates/index.html', contexto)
def verDetalle(request,pokemon_id)
     respons = requests.get(' https://pokeapi.co/api/v2/pokemon/pokemon_id/')#url para traer la informacion inicial de los primero 150 pokemons
    if respons.status_code == 200:
        contenido = respons.content
        diccionario = respons.json()
        listpokemon = diccionario['results']      
        print(pokemon)  
        contexto = {'pokemons': diccionario['results']}  
    return render (request, '../Templates/index.html', contexto)