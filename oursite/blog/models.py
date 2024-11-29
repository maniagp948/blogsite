from datetime import date

from django.db import models
from modelcluster.models import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class BlogIndexPage(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel(
            "description",
        )
    ]


class BlogPostPage(Page):
    date = models.DateField("Post Date", default=date.today)
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)


class BlogPageImageGallery(Orderable):
    page = ParentalKey(BlogPostPage, related_name="image_gallery", on_delete=models.CASCADE)  # type: ignore
    image = models.ForeignKey(
        "wagtailimages.Image", related_name="+", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=255, blank=True)
