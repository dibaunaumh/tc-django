from tcdjango.community.models import Domain

def get_all_domains():
    return  Domain.objects.all()


