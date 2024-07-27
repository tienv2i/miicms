from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import InlinePanel, FieldPanel, MultiFieldPanel
from wagtail.search import index
from taggit.models import TaggedItemBase, Tag as TaggitTag
from wagtailseo.models import SeoMixin
from modelcluster.models import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from wagtail.snippets.models import register_snippet

# Create your models here.

class PostPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', related_name='tagged_items', on_delete=models.CASCADE)

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug')
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'blog categories'

class PostPage(SeoMixin, Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField()
    tags = ClusterTaggableManager(through=PostPageTag, blank=True)
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('tags'),
        FieldPanel('feed_image'),
        FieldPanel('intro'),
        InlinePanel('categories', label='Category'),
        FieldPanel('body', classname='full'),
    ]

    promote_panels = SeoMixin.seo_panels

    subpage_types = []

    def __str__(self):
        return self.title
    

class PostPageCategory(models.Model):
    page = ParentalKey("blog.PostPage", on_delete=models.CASCADE, related_name="categories")
    blog_category = models.ForeignKey("blog.BlogCategory", on_delete=models.CASCADE, related_name="post_pages")

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")

class BlogIndexPage(Page):
    subpage_types = ['PostPage']