# Create your views here.
from tcdjango.community.models import *
from django.shortcuts import render_to_response,get_object_or_404

def home(request, domain = None):

    domains = Domain.objects.all()
    
    domainObj = get_object_or_404(Domain, name = domain)
    
    if domain:
        articles = ArticlePost.objects.filter(domains = domainObj)
    else:    
        articles = ArticlePost.objects.all()

    print articles.count()
    print domain
    
    return  render_to_response('content_index.html', locals())
