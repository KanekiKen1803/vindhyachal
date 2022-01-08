from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render
from base.models import Team_member, Notice, Feed, Feed_Type


from vindhyachal.settings import BASE_DIR

# Create your views here.
def home(request):
    ######################################################
    notices = Notice.objects.all()[:5]
    #########################################################
    secretaries = Team_member.objects.filter(Q(category__category__icontains='secretary') | Q(category__category__icontains = 'warden') 
                                             | Q(category__category__icontains = 'caretaker') )
    #######################################################
    feeds = Feed.objects.all()[0:4]
    ########################################################
    
    context = {
        'notices':notices,
        'secretaries':secretaries,
        'feeds': feeds
    }
    
    
    return render(request, 'base/home.html', context)

def feed(request):
    categories = Feed_Type.objects.all()
    feeds = Feed.objects.all()[0:9]
    context = {
        'categories' : categories,
        'feeds': feeds
    }
    
    return render(request, 'feed/feed-home.html', context)