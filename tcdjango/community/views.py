# Create your views here.
from tcdjango.community.models import *
from django.shortcuts import render_to_response,get_object_or_404
from dataaccess import *
import datetime

def home(request, domain = None):

    domains = get_all_domains()

    domainObj = get_object_or_404(Domain, name = domain)

    if domain:
        articles = ArticlePost.objects.filter(domains = domainObj)
    else:
        articles = ArticlePost.objects.all()

    topStory =  articles.filter(sticky = True).order_by('-created')[:1]
    actives =     articles.order_by('-created')[:2]

    offeringList = OfferingPost.objects.all()

    now = datetime.datetime.now()
   # upComingEvents =  EventPost.objects.filter('start_time'>now)
   # print  upComingEvents
    #return  render_to_response('content_index.html', locals())
    return  render_to_response('content_index.html', locals())

def view_article(request, slug):
    article = get_object_or_404(Post, slug = slug)
    domains = get_all_domains()
    return  render_to_response('article.html', locals())