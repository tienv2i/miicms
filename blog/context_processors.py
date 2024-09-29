from .models import BlogCategory, BlogPage
from taggit.models import Tag
from wagtail.models import Site

def blog_context(request):
    wagtail_site = Site.find_for_request(request)
    return {
        'all_categories': BlogCategory.objects.all(),
        'latest_10_tags': Tag.objects.all().order_by('-id')[:10],
        'first_blog_page': BlogPage.objects.in_site(wagtail_site).first(),
    }