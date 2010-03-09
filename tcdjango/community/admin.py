from django.contrib import admin
from tcdjango.community.models import *

class DomainAdmin(admin.ModelAdmin):
    pass

class BlogPostAdmin(admin.ModelAdmin):
    pass

class ArticlePostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'author__username']
    list_filter = ['author', 'sticky']
    date_hierarchy = 'created'

class ForumPostAdmin(admin.ModelAdmin):
    pass

class OfferingPostAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

class SignupAdmin(admin.ModelAdmin):
    pass

class FeedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Domain, DomainAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ArticlePost, ArticlePostAdmin)
admin.site.register(ForumPost, ForumPostAdmin)
admin.site.register(OfferingPost, OfferingPostAdmin)
admin.site.register(EventPost, EventAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(Feed, FeedAdmin)

