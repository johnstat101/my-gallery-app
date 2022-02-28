from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations})


def image_location(request, image_location):
    images = Image.filter_by_location(image_location)
    return render(request, 'location.html', {'location_images': images})

# search
def search(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"categories": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
