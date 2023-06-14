from django.apps import AppConfig


class FlexConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "flex"
    def ready(self):
        pass
        # from wagtail.models import Page
        # from flex.models import dataset
        # from home.models import collection

        # parent_page = Page.objects.get(title='Collections')
        # snippets = collection.objects.all()

        # for snippet in snippets:
        #     childPageName = snippet.name
        #     childPageDescription = snippet.description
        #     childPageURL=snippet.specification_URL

        #     child_page = dataset(title=childPageName,
        #                         name=childPageName,
        #                         description=childPageDescription,specification_URL=childPageURL)
        #     parent_page.add_child(instance=child_page)
        #     child_page.save_revision().publish()