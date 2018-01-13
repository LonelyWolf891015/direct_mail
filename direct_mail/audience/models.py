from django.db import models
from treebeard.ns_tree import NS_Node

# Create your models here.
class Audience(models.Model):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: %s' % self.name
