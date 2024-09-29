from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag, TaggedItemBase
from modelcluster.models import ParentalKey
from wagtailseo.models import SeoMixin
from modelcluster.contrib.taggit import ClusterTaggableManager
from .blocks import BodyBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, route, re_path
from django.utils import timezone
from wagtail.search import index
# Create your models here.

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    
    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
        
class SinglePage(SeoMixin, Page):
    body = StreamField(BodyBlock(), blank=True, default = BodyBlock.get_default_value)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    seo_panels = SeoMixin.seo_panels
    
class BlogPage(RoutablePageMixin, SeoMixin, Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    
    seo_panels = SeoMixin.seo_panels
    def get_posts(self):
        return PostPage.objects.descendant_of(self).live().order_by('-post_date')
    
    @route(r"^$")
    def blog_index_view(self, request):
        self.posts = self.get_posts()
        return self.render(request)
    
    @route(r'^category/(?P<cat_slug>[-\w]+)/$')
    def category_view(self, request, cat_slug):
        self.filter_type = 'Category'
        self.filter_term = 'slug'
        self.filter_value = cat_slug
        self.posts = self.get_posts().filter(categories__category__slug = cat_slug)
        return self.render(request)
    
    
    @route(r"^tag/(?P<tag_slug>[-\w]*)/$")
    def tag_view(self, request, tag_slug):
        self.filter_type = 'Tag'
        self.filter_term = 'slug'
        self.filter_value = tag_slug
        self.posts = self.get_posts().filter(tags__slug = tag_slug)
        return self.render(request)
    
    @route("^search/$")
    def search_view(self, request):
        search_query = request.GET.get('q', None)
        self.posts = self.get_posts()
        self.filter_type = 'Search'
        self.filter_term = 'query'
        self.filter_value = search_query if search_query is not None else "Blank"
        
        if search_query:
            self.posts = self.posts.search(search_query)
            self.dump_var="Dump inside if: "+search_query
            
        return self.render(request)  
    

class PostPage(SeoMixin, Page):
    header_image = models.ForeignKey(
        'wagtailimages.Image', 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name='+'
    )
    tags = ClusterTaggableManager(through='blog.PostPageTag', blank=True)
    post_date = models.DateTimeField(
        verbose_name="Post date", default=timezone.now
    )
    excerpt = RichTextField(blank=True)
    body = StreamField(BodyBlock(), blank=True, default = BodyBlock.get_default_value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('tags'),
        FieldPanel('post_date'),
        InlinePanel('categories', label='Categories'),
        FieldPanel('excerpt'),
        FieldPanel('body'),
    ]
    
    seo_panels = SeoMixin.seo_panels
    
    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('excerpt'),
        index.SearchField('body'),
    ]
    
    def get_categories(self):
        return self.categories.all()  # Lấy danh sách tất cả các category liên kết
    
class PostPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.PostPage', related_name='post_tags')
    
class PostPageCategory(models.Model):
    page = ParentalKey('blog.PostPage', on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey('blog.BlogCategory', on_delete=models.CASCADE, related_name='post_pages')
    
    panels = [
        FieldPanel('category'),
    ]
    
    class Meta:
        unique_together = ['page', 'category']
       
class FeeedbackMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('message')
    ]
class BlogContactPage(SeoMixin, Page):
    description = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('description'),
    
    ]
    
    def serve(self, request):
        # return super().serve(request)
        from .forms import FeedbackForm
        from django.shortcuts import render
        if request.method=='POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save()
                return render(request, 'blog/contact_page.html', {
                    'page': self,
                    
                    'feedback': feedback
                })
        else:
            form = FeedbackForm()
            
        return render(request, 'blog/contact_page.html', {
            'page': self,
            'form': form,
        })
        