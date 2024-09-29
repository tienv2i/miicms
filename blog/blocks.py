from wagtail.blocks import CharBlock, RichTextBlock, StreamBlock, StructBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailmath.blocks import MathBlock
from wagtailmarkdown.blocks import MarkdownBlock


class ImageGalleryBlock(StructBlock):
    title = CharBlock(required=True, help_text="Gallery title")
    images = ListBlock(
        ImageChooserBlock(),
        help_text = "Add images to gallery"
    )
    class Meta:
        template = 'blocks/image_gallery.html'
        icon = "image"
        label = "Image Gallery"
class BodyBlock(StreamBlock):
    heading = CharBlock(classname="full title", label="Heading")
    paragraph = RichTextBlock(label="Paragraph")
    image = ImageChooserBlock(label="Image")
    table = TableBlock(label="Table")
    equation = MathBlock(label="Equation")
    markdown = MarkdownBlock(icon="code")
    gallery = ImageGalleryBlock()
    
    @staticmethod
    def get_default_value():
        return [
            ('heading',''),
            ('paragraph', '')
        ]
    