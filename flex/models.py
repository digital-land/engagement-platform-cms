"""flexible page"""
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.fields import RichTextField
from wagtail.api import APIField

# Create your models here.
class FlexPage(Page):
    """flexible page class"""

    template="flex/flex_page.html"

    #content = StreamField()

    subtitle=models.CharField(max_length=100,null=True,blank=True)
    #description=models.CharField(max_length=100,null=True,blank=True)
    description=RichTextField(features=["bold","italic"])

    #add field to API
    api_fields=[
        APIField("subtitle"),
        APIField("description")
    ]
    #fieldPanel takes the field and puts it into wagtail admin for us to edit
    #or else it will just be a field in db and wont be of any use
    content_panels=Page.content_panels+[FieldPanel("subtitle"),FieldPanel("description")]
    
    class Meta:
        verbose_name="Flex Page"
        verbose_name_plural="Flex Pages"
