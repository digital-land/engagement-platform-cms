"""flexible page"""
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,StreamFieldPanel,MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail.rich_text import LinkHandler
from wagtail.core import blocks

class AccordionItemBlock(blocks.StructBlock):
    issue = blocks.CharBlock(required=True)
    fix = blocks.RichTextBlock(required=True)

    class Meta:
        icon = 'list-ul'

class CustomRichTextField(RichTextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.features = []
        self.features += ['link']
        self.link_handler = LinkHandler()

# Create your models here.
class FlexPage(Page):
    """flexible page class"""

    template="flex/flex_page.html"

    #content = StreamField()

    subtitle=models.CharField(max_length=100,null=True,blank=True)
    description=RichTextField(features=["bold","italic"],default='')
    specification_URL = CustomRichTextField()
    accordion_items = StreamField(
        [
            ('accordion_item', AccordionItemBlock())
        ],
        null=True,
        blank=True
    )

    #add field to API
    api_fields=[
        APIField('subtitle'),
        APIField('description'),
        APIField('specification_URL'),
        APIField('accordion_items')
    ]

    #fieldPanel takes the field and puts it into wagtail admin for us to edit
    #or else it will just be a field in db and wont be of any use
    content_panels=Page.content_panels+[
            FieldPanel('subtitle'),
            FieldPanel('description'),
            FieldPanel('specification_URL'),
            StreamFieldPanel('accordion_items')
        ]
    
    class Meta:
        verbose_name="Flex Page"
        verbose_name_plural="Flex Pages"
