from django.shortcuts import render
from blog.data import posts

# Create your views here.


def blog(request):
    print('Blog')
    context = {
            'text': 'Olá, Blog!',
            'title': 'Título do blog | ',
            'posts': posts,
        }
    return render(
        request,
        'blog/index.html',
        context,
    )


def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    print('Blog')
    context = {
            'text': 'Olá, Blog!',
            'title': 'Título do blog | ',
            'posts': [found_post],
        }
    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):
    print('Exemplo')
    context = {
            'text': 'Exemplo de aninhamento de URLs',
            'title': 'Título do exemplo | ',
        }
    return render(
        request,
        'blog/exemplo.html',
        context,
    )
