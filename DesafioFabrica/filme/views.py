import requests
from django.shortcuts import render
from .models import Filme

def search_movie(request):
    movie_info = None
    error_message = None
    
    if request.method == 'POST':
        movie_name = request.POST.get('movieName')
        api_key = "bef9a194"
        
        if movie_name:
            response = requests.get(f'http://www.omdbapi.com/?t={movie_name}&apikey={api_key}')
            data = response.json()
            
            if data['Response'] == 'True':
                movie_info = {
                    'title': data['Title'],
                    'year': data['Year'],
                    'director': data['Director'],
                    'synopsis': data['Plot'],
                    'poster_url': data['Poster'],
                    'rating': next((item['Value'] for item in data['Ratings'] if item['Source'] == 'Rotten Tomatoes'), 'N/A')
                }

                # Salvar no banco de dados
                Filme.objects.update_or_create(
                    titulo=movie_info['title'],
                    defaults={
                        'ano': movie_info['year'],
                        'diretor': movie_info['director'],
                        'sinopse': movie_info['synopsis'],
                        'url_poster': movie_info['poster_url'],
                        'avaliacao': movie_info['rating']
                    }
                )
            else:
                error_message = data.get('Error', 'Filme não encontrado.')
    
    return render(request, 'filme/index.html', {
        'informacoes_filme': movie_info,
        'mensagem_erro': error_message,
    })
