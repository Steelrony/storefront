from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Two things you need for a generic relationship (this one is for product)
    # Type (product, video, article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = (
        models.PositiveIntegerField()
    )  # this will only work for objects whose id are of this same type
    content_object = GenericForeignKey()
