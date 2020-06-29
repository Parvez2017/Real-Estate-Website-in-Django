from django.shortcuts import render
from listings.models import Listing
from listings.choices import state_choices, price_choices, bedroom_choices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date')[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')