from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Category, Photo
from django.core.checks import messages


# Create your views here.
def welcome(request):
    try:
        photos = Photo.objects.all()
    except DoesNotExist:
        raise Http404()
    category = Category.objects.all()
    return render(request,'welcome.html',{'photos':photos} ,{'category':category})

def gallery_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def get_photo(request):
    try:
        photos = Photo.objects.all()
    except DoesNotExist:
        raise Http404()
    # import pdb; pdb.set_trace()
    return render(request, 'photos.html', {"photos":photos})

def get_category(request):
    category = Category.object.all()

    return render(request,'welcome.html', {"category":category})









    

def search_results(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})