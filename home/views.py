from django.shortcuts import render
from django.http.response import Http404

from home.models import Profile


def index(request):
    # if request.method == 'POST':
    #     print(request.POST)
    # try:
    #     user = Profile.objects.get(nama="maftuh")
    # except:
    #     raise Http404("not found")

    context = {
        # 'user': user,
        'title' : 'Hamid',
        'judul': 'Home',
        'paragraf': "Curious which components explicitly require our JavaScript and Popper? Click the show components link below. If you’re at all unsure about the general page structure, keep reading for an example page template."
    }

    return render(request, 'index.html', context=context)

def about(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'about.html')
