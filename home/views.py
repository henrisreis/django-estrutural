from django.shortcuts import render


def home(request):
    print('Home')
    context = {
            'text': 'Estamos na home!',
            'title': 'Título da home |',
        }
    return render(
        request,
        'home/index.html',
        context,
    )
