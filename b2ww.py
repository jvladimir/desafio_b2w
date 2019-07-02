import requests

print('STAR WAR API')

print('As opções são: films(filmes), people(personagens), planets(planetas), species(especies), starchip(naves), vehicles(veiculos)')

numero = input('Digite o numero ')

if len(numero) != 1:
    print('esquisa dinvalida')
    exit()

request = requests.get('https://swapi.co/api/films/{}/'.format(numero))

address_data = request.json()

if 'erro' not in address_data:
    print('==>Pesquisa válida<==')
    print('TITULO DO FILME: {}'.format(address_data['title']))
    print('ANO {}'.format(address_data['release_date']))
    print('EPISÓDIO {}'.format(address_data['episode_id']))
else:
    print('Entrada invalida!')