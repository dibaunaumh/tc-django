from django.db import models
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext_lazy as _

class Domain(models.Model):
    name = models.CharField(_('name'), max_length = 256, unique = True, db_index = True)
    group = models.OneToOneField(Group, verbose_name = _('user group'))

    def __unicode__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name = _('author'))
    title = models.CharField(_('title'), max_length = 256, unique = True, db_index = True)
    domains = models.ManyToManyField(Domain, verbose_name = _('domain'), help_text = 'Choose relevant domain')
    content = models.TextField(_('content'), max_length = 16384)
    created = models.DateTimeField(_('created'), auto_now_add = True)
    updated = models.DateTimeField(_('updated'), auto_now = True)
    slug = models.SlugField(_('url alias'), help_text = _('Choose human-readable (valid!) url'))
    sticky = models.BooleanField(_('sticky'), default = False)
    published = models.BooleanField(_('published'), default = True)


    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True

class ArticlePost(Post):
    pass

class BlogPost(Post):
    pass

class ForumPost(Post):
    pass

class OfferingPost(Post):
    pass

class EventPost(Post):
    start_time = models.DateTimeField(_('start time'))
    end_time = models.DateTimeField(_('end time'))

# TODO: add uniqueness on user+event
class Signup(models.Model):
    user = models.OneToOneField(User)
    event = models.OneToOneField(EventPost, related_name = 'signups')

class Feed(Post):
    url = models.URLField(_('url'))
