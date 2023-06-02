from django.db import models

from wagtail.models import Page,Orderable
from wagtail.admin.panels import FieldPanel,InlinePanel,MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey

#binds page to a snippet
class collectionsOrderable(Orderable):
    """This allows us to select one or more collection from Snippets."""

    page = ParentalKey("home.HomePage", related_name="collection")
    collection = models.ForeignKey(
        "home.collection",
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel("collection"),
    ]

    @property
    def collection_name(self):
        return self.collection.name
    
    @property
    def collection_description(self):
        return self.collection.description
    
    @property
    def collection_specification_URL(self):
        return self.collection.specification_URL
    
    api_fields=[APIField("collection_name"),APIField("collection_description"),APIField("collection_specification_URL")]
    
#django model registered as a snippet
class collection(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    description=models.CharField(max_length=500)
    specification_URL=models.URLField(blank=True,null=True)

    panels=[MultiFieldPanel([FieldPanel("name"),FieldPanel("description"),FieldPanel("specification_URL"),],heading="name, description and URL",)]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="collection"
        verbose_name_plural="collections"
    
register_snippet(collection)

class HomePage(Page):
    """Home page model"""
    templates="home/home_page.html"
    
    #there can only be one home page
    max_count=1
    
    #input field which takes char data 
    #it is a django field/property whose name is banner_title
    banner_title=models.CharField(max_length=100,blank=False,null=True)

    banner_subtitle=RichTextField(features=["bold","italic"])
    
    api_fields=[
        APIField("banner_title"),
        APIField("banner_subtitle"),
        APIField("collection")
    ]
    #=======================================================================
    #we need content panels to use it
    #FieldPanel to make it editable in wagtail admin
    content_panels=Page.content_panels+[FieldPanel("banner_title"),
                                        FieldPanel("banner_subtitle"),
                                        MultiFieldPanel(
                                        [
                                            InlinePanel("collection", label="collection", min_num=1, max_num=4)
                                        ],
                                        heading="collection(s)"
                                        ),]
  
    class Meta:
        verbose_name="Home Page"
        verbose_name_plural="Home Pages"