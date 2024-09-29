from wagtail.blocks import CharBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailmath.blocks import MathBlock
from wagtailmarkdown.blocks import MarkdownBlock

class BodyBlock(StreamBlock):
    heading = CharBlock(classname="full title", label="Heading")
    paragraph = RichTextBlock(label="Paragraph")
    image = ImageChooserBlock(label="Image")
    table = TableBlock(label="Table")
    equation = MathBlock(label="Equation")
    markdown = MarkdownBlock(icon="code") 
    
    @staticmethod
    def get_default_value():
        return [
            ('heading',''),
            ('paragraph', '')
        ]
    