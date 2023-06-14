import csv
import os
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,PageChooserPanel,MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.api import APIField
from wagtail.snippets.models import register_snippet

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

schema = {}
reader = csv.DictReader(open(os.path.join('specification', "schema.csv")))
for row in reader:
    schema.setdefault(row["schema"],[])
    schema[row["schema"]].append(row["name"])
    schema[row["schema"]].append(row["description"])
    name_Value=schema[row["schema"]][0]
    description_Value=schema[row["schema"]][1]
    
    snippet_create = collection(name=name_Value, description=description_Value)
    snippet_create.save()

class HomePage(Page):
    """Home page model"""

    templates="home/home_page.html"
    #=======================================================================
    #there can only be one home page
    max_count=1
    
    #input field which takes char data 
    #it is a django field/property whose name is banner_title
    banner_title=models.CharField(max_length=100,blank=False,null=True)

    #=======================================================================
    banner_subtitle=RichTextField(features=["bold","italic"])

    #for using an image we use foreign key to wagtails existing image model
    banner_image=models.ForeignKey(
        "wagtailimages.Image",
        null=True, #when you makemigrations,home page already exists, and this was False then it will ask for some default values which we dont know
        blank=False, #there should be banner image it can not be blank
        on_delete=models.SET_NULL, #when img or page is deleted we dont want any cascade delete
        related_name="+"
    )
    #link to another wagtail page
    banner_cta=models.ForeignKey(
        "wagtailcore.Page", #wagtailcore is app name and page is model name
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    api_fields=[
        APIField("banner_title"),
        APIField("banner_subtitle")
    ]
    #=======================================================================
    #we need content panels to use it
    #FieldPanel to make it editable in wagtail admin
    content_panels=Page.content_panels+[FieldPanel("banner_title"),
                                        FieldPanel("banner_subtitle"),
                                        FieldPanel("banner_image"),
                                        PageChooserPanel("banner_cta")]
    #here we made a column in the database for us using makemigrations and then migrate


    #for new pages
    class Meta:
        verbose_name="Home Page"
        verbose_name_plural="Home Pages"