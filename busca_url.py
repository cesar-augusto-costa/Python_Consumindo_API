from urllib.parse import parse_qs, urlparse

link = 'https://www.google.com/search?q=hashtag+treinamentos&rlz=1C1GCEA_enBR1032BR1032&oq=hashtag+treinamentos&aqs=chrome..69i57j0i512j69i64j0i512l3j69i60l2.6958j0j7&sourceid=chrome&ie=UTF-8'

link_tratado = urlparse(link)
print(link_tratado, end='\n\n')

parametros = link_tratado.query
print(parametros, end='\n\n')

parametros = parse_qs(link_tratado.query)
print(parametros, end='\n\n')

print(parametros['q'])

