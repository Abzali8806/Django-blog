from django.shortcuts import render, redirect

from .forms import CreateSpaceForm
from .models import Space

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'browser/home.html', context)

def create_spaces_view(request):
    form = CreateSpaceForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(home_view)

    context = {
        'form': form
    }

    return render(request, 'browser/create_space.html', context)

def search_views(request):
    spaces = Space.objects.all()
    get_search = request.GET['title']
    # print(get_search)
    context = {
        'spaces': spaces,
        'search': get_search
    }
    return render(request, 'browser/search_results.html', context)