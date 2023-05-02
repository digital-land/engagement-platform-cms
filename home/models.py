from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField

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
                                        ImageChooserPanel("banner_image"),
                                        PageChooserPanel("banner_cta")]
    #here we made a column in the database for us using makemigrations and then migrate


    #for new pages
    class Meta:
        verbose_name="Home Page"
        verbose_name_plural="Home Pages"